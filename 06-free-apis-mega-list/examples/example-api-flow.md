# Example API Flow: "Smart Document Scanner"

A full integration walkthrough for a project that scans documents, extracts text, summarizes content, stores results, and emails a report. This is the kind of multi-API project that wins hackathons.

---

## The Project

**SmartDoc Scanner** lets users upload a photo of a document (receipt, contract, medical form, etc.). The app:
1. Scans the image for text (OCR)
2. Categorizes the document type
3. Extracts key fields (dates, amounts, names)
4. Generates a plain-English summary
5. Stores everything in a database
6. Emails a formatted report to the user

**Stack:** Next.js + Supabase + Vercel

---

## API Flow Diagram

```
User uploads image
        ↓
[Tier 1] Google Cloud Vision API → OCR text extraction
        ↓
[Tier 2] OpenAI GPT-4o-mini → categorize + extract fields + summarize
        ↓
[Tier 3] Supabase → store document + extracted data
        ↓
[Tier 4] Resend → email formatted report to user
```

---

## Step 1: Google Cloud Vision API — OCR Text Extraction

**Why this API:** Best-in-class OCR. Free tier: 1,000 requests/month. No credit card required for free tier.

**Setup:**
1. Create a Google Cloud project
2. Enable Cloud Vision API
3. Create an API key (restrict to Cloud Vision only)
4. Store key as `GOOGLE_CLOUD_VISION_API_KEY` in `.env.local`

**The actual code:**

```typescript
// lib/ocr.ts
export async function extractText(imageBase64: string): Promise<string> {
  const apiKey = process.env.GOOGLE_CLOUD_VISION_API_KEY;
  const url = `https://vision.googleapis.com/v1/images:annotate?key=${apiKey}`;

  const response = await fetch(url, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({
      requests: [
        {
          image: { content: imageBase64 },
          features: [{ type: "TEXT_DETECTION", maxResults: 1 }],
        },
      ],
    }),
  });

  const data = await response.json();

  if (data.responses?.[0]?.error) {
    throw new Error(`OCR failed: ${data.responses[0].error.message}`);
  }

  return data.responses?.[0]?.fullTextAnnotation?.text || "";
}
```

**Error handling:**

```typescript
// What can go wrong and how to handle it

// 1. Image too large (>4MB)
// Solution: Resize before sending
import sharp from "sharp";

async function compressImage(base64: string): Promise<string> {
  const buffer = Buffer.from(base64, "base64");
  const resized = await sharp(buffer)
    .resize(2000, 2000, { fit: "inside" })
    .jpeg({ quality: 80 })
    .toBuffer();
  return resized.toString("base64");
}

// 2. Rate limit (1,000 requests/month free)
// Solution: Cache results by image hash
import crypto from "crypto";

function hashImage(base64: string): string {
  return crypto.createHash("md5").update(base64).digest("hex");
}

// Check cache before calling API
const imageHash = hashImage(imageBase64);
const cached = await supabase
  .from("ocr_cache")
  .select("text")
  .eq("image_hash", imageHash)
  .single();

if (cached.data) {
  return cached.data.text; // Skip API call
}

// 3. No text found in image
// Solution: Return a clear error, not empty string
const text = data.responses?.[0]?.fullTextAnnotation?.text;
if (!text || text.trim().length === 0) {
  throw new Error("No text found in image. Please upload a clearer photo.");
}
```

**Rate limit considerations:**
- Free tier: 1,000 requests/month
- At a hackathon, you'll use maybe 20-50 requests for testing
- For production: cache by image hash (shown above), implement a queue
- Fallback: Tesseract.js (runs in browser, no API needed, slightly worse accuracy)

---

## Step 2: OpenAI GPT-4o-mini — Categorize + Extract + Summarize

**Why this API:** Fast, cheap ($0.15/1M input tokens), excellent at structured extraction. GPT-4o-mini is the sweet spot for hackathon use.

**Setup:**
1. Create an OpenAI account
2. Generate an API key
3. Store as `OPENAI_API_KEY` in `.env.local`
4. Install: `npm install openai`

**The actual code — three chained calls:**

```typescript
// lib/ai.ts
import OpenAI from "openai";

const openai = new OpenAI({ apiKey: process.env.OPENAI_API_KEY });

// Step 2a: Categorize the document
async function categorizeDocument(text: string): Promise<{
  category: string;
  confidence: number;
}> {
  const response = await openai.chat.completions.create({
    model: "gpt-4o-mini",
    messages: [
      {
        role: "system",
        content: `You are a document classifier. Categorize the document into exactly one category:
        receipt, contract, medical_form, invoice, letter, resume, other.
        Return JSON: { "category": "...", "confidence": 0.0-1.0 }`,
      },
      {
        role: "user",
        content: `Categorize this document:\n\n${text.substring(0, 3000)}`,
      },
    ],
    response_format: { type: "json_object" },
  });

  return JSON.parse(response.choices[0].message.content || "{}");
}

// Step 2b: Extract key fields
async function extractFields(
  text: string,
  category: string
): Promise<Record<string, string>> {
  const fieldSchemas: Record<string, string> = {
    receipt:
      "date, store_name, total_amount, items (comma-separated), payment_method",
    contract:
      "parties_involved, start_date, end_date, key_terms, total_value",
    medical_form:
      "patient_name, doctor_name, date, diagnosis, treatment, medications",
    invoice:
      "vendor, invoice_number, due_date, total_amount, line_items",
    letter:
      "sender, recipient, date, subject, key_points",
    resume:
      "name, email, phone, skills, experience_years, education",
    other: "title, date, key_entities, summary",
  };

  const response = await openai.chat.completions.create({
    model: "gpt-4o-mini",
    messages: [
      {
        role: "system",
        content: `You are a data extraction specialist. Extract the following fields from the document:
        ${fieldSchemas[category] || fieldSchemas.other}
        Return as JSON with snake_case keys. Use "N/A" for fields not found.`,
      },
      {
        role: "user",
        content: `Extract fields from this ${category}:\n\n${text.substring(0, 3000)}`,
      },
    ],
    response_format: { type: "json_object" },
  });

  return JSON.parse(response.choices[0].message.content || "{}");
}

// Step 2c: Generate summary
async function generateSummary(
  text: string,
  category: string,
  fields: Record<string, string>
): Promise<string> {
  const response = await openai.chat.completions.create({
    model: "gpt-4o-mini",
    messages: [
      {
        role: "system",
        content: `You are a document summarizer. Write a 2-3 sentence plain-English summary of this ${category}.
        Be specific. Include key numbers, dates, and names. No jargon.`,
      },
      {
        role: "user",
        content: `Document text:\n${text.substring(0, 3000)}\n\nExtracted fields:\n${JSON.stringify(fields, null, 2)}`,
      },
    ],
  });

  return response.choices[0].message.content || "Summary unavailable.";
}
```

**Error handling:**

```typescript
// 1. OpenAI rate limit (Tier 1: 500 RPM, 200K TPM)
// Solution: Add retry with exponential backoff
async function withRetry<T>(
  fn: () => Promise<T>,
  maxRetries = 3
): Promise<T> {
  for (let i = 0; i < maxRetries; i++) {
    try {
      return await fn();
    } catch (error: any) {
      if (error?.status === 429 && i < maxRetries - 1) {
        await new Promise((r) => setTimeout(r, 1000 * 2 ** i));
        continue;
      }
      throw error;
    }
  }
  throw new Error("Max retries exceeded");
}

// 2. Invalid JSON response
// Solution: Parse with fallback
function safeParseJSON(text: string): Record<string, any> {
  try {
    return JSON.parse(text);
  } catch {
    // Try to extract JSON from markdown code blocks
    const match = text.match(/```json\n([\s\S]*?)\n```/);
    if (match) return JSON.parse(match[1]);
    return {};
  }
}

// 3. Token limit exceeded (4,096 tokens for gpt-4o-mini)
// Solution: Truncate input intelligently
function truncateForTokens(text: string, maxChars = 3000): string {
  if (text.length <= maxChars) return text;
  // Cut at last complete sentence within limit
  const truncated = text.substring(0, maxChars);
  const lastPeriod = truncated.lastIndexOf(".");
  return lastPeriod > maxChars * 0.8
    ? truncated.substring(0, lastPeriod + 1)
    : truncated + "...";
}
```

**Token usage per document:**
- OCR text (input): ~1,500 tokens average
- Categorization call: ~200 tokens output
- Extraction call: ~300 tokens output
- Summary call: ~100 tokens output
- **Total per document: ~2,100 tokens**
- **Cost per document: ~$0.0003 (fraction of a penny)**

---

## Step 3: Supabase — Store Document + Extracted Data

**Why this API:** Free tier gives you 500MB database, 1GB file storage, auth, and real-time. Perfect for hackathons.

**Setup:**
1. Create a Supabase project
2. Create tables via SQL editor
3. Store `SUPABASE_URL` and `SUPABASE_ANON_KEY` in `.env.local`

**The database schema:**

```sql
CREATE TABLE documents (
  id UUID DEFAULT gen_random_uuid() PRIMARY KEY,
  user_id TEXT NOT NULL,
  original_image_url TEXT,
  ocr_text TEXT,
  category TEXT,
  confidence NUMERIC(3,2),
  extracted_fields JSONB,
  summary TEXT,
  created_at TIMESTAMPTZ DEFAULT NOW()
);

-- Index for fast lookups
CREATE INDEX idx_documents_user_id ON documents(user_id);
CREATE INDEX idx_documents_category ON documents(category);
```

**The actual code:**

```typescript
// lib/database.ts
import { createClient } from "@supabase/supabase-js";

const supabase = createClient(
  process.env.SUPABASE_URL!,
  process.env.SUPABASE_ANON_KEY!
);

export async function saveDocument(doc: {
  userId: string;
  imageUrl: string;
  ocrText: string;
  category: string;
  confidence: number;
  extractedFields: Record<string, string>;
  summary: string;
}) {
  const { data, error } = await supabase
    .from("documents")
    .insert({
      user_id: doc.userId,
      original_image_url: doc.imageUrl,
      ocr_text: doc.ocrText,
      category: doc.category,
      confidence: doc.confidence,
      extracted_fields: doc.extractedFields,
      summary: doc.summary,
    })
    .select()
    .single();

  if (error) throw new Error(`Database error: ${error.message}`);
  return data;
}

export async function uploadImage(
  file: Buffer,
  filename: string
): Promise<string> {
  const { data, error } = await supabase.storage
    .from("documents")
    .upload(`uploads/${filename}`, file, {
      contentType: "image/jpeg",
      upsert: true,
    });

  if (error) throw new Error(`Upload error: ${error.message}`);

  const {
    data: { publicUrl },
  } = supabase.storage.from("documents").getPublicUrl(`uploads/${filename}`);

  return publicUrl;
}
```

**Error handling:**
- **Row-level security (RLS):** Enable RLS on the `documents` table so users can only see their own documents. For hackathon MVP, you can use a simple user_id check.
- **Storage limits:** Free tier is 1GB. A JPEG is ~200KB. That's ~5,000 images. Plenty for a hackathon.
- **Connection pooling:** Supabase handles this automatically. No configuration needed.

---

## Step 4: Resend — Email Formatted Report

**Why this API:** Free tier: 3,000 emails/month. Simple API. Beautiful HTML emails. No SMTP configuration.

**Setup:**
1. Create a Resend account
2. Generate an API key
3. Verify your domain (or use their default for hackathons)
4. Store as `RESEND_API_KEY` in `.env.local`

**The actual code:**

```typescript
// lib/email.ts
import { Resend } from "resend";

const resend = new Resend(process.env.RESEND_API_KEY);

export async function sendReport(
  to: string,
  doc: {
    category: string;
    summary: string;
    extractedFields: Record<string, string>;
    confidence: number;
    imageUrl: string;
  }
) {
  const fieldsHtml = Object.entries(doc.extractedFields)
    .map(
      ([key, value]) =>
        `<tr><td style="padding:8px;border-bottom:1px solid #eee;font-weight:bold;">${key.replace(/_/g, " ")}</td><td style="padding:8px;border-bottom:1px solid #eee;">${value}</td></tr>`
    )
    .join("");

  await resend.emails.send({
    from: "SmartDoc <noreply@yourdomain.com>",
    to,
    subject: `📄 ${doc.category.replace(/_/g, " ").toUpperCase()} — Scanned Document Report`,
    html: `
      <div style="font-family:sans-serif;max-width:600px;margin:0 auto;">
        <h2 style="color:#333;">Document Scan Complete</h2>
        <p style="color:#666;">${doc.summary}</p>

        <h3 style="color:#333;">Extracted Fields</h3>
        <table style="width:100%;border-collapse:collapse;">
          ${fieldsHtml}
        </table>

        <p style="color:#999;font-size:12px;margin-top:20px;">
          Confidence: ${(doc.confidence * 100).toFixed(0)}% |
          <a href="${doc.imageUrl}">View Original</a>
        </p>
      </div>
    `,
  });
}
```

**Error handling:**
- **Resend free tier:** 3,000 emails/month. For a hackathon demo, you'll send maybe 10-20. No issues.
- **Email delivery:** Resend handles SPF/DKIM automatically. No configuration needed.
- **Fallback:** If Resend fails, fall back to `nodemailer` with Gmail SMTP (but this requires app passwords and is more setup).

---

## The Full Pipeline — Putting It All Together

```typescript
// app/api/scan/route.ts
import { extractText } from "@/lib/ocr";
import { categorizeDocument, extractFields, generateSummary } from "@/lib/ai";
import { saveDocument, uploadImage } from "@/lib/database";
import { sendReport } from "@/lib/email";

export async function POST(request: Request) {
  try {
    const { imageBase64, userEmail } = await request.json();

    // Compress if needed
    const compressed = await compressImage(imageBase64);

    // Step 1: OCR
    const ocrText = await extractText(compressed);
    if (!ocrText) {
      return Response.json(
        { error: "No text detected in image" },
        { status: 400 }
      );
    }

    // Step 2: AI Analysis
    const { category, confidence } = await categorizeDocument(ocrText);
    const extractedFields = await extractFields(ocrText, category);
    const summary = await generateSummary(ocrText, category, extractedFields);

    // Step 3: Store
    const imageUrl = await uploadImage(
      Buffer.from(compressed, "base64"),
      `${Date.now()}.jpg`
    );
    const doc = await saveDocument({
      userId: userEmail,
      imageUrl,
      ocrText,
      category,
      confidence,
      extractedFields,
      summary,
    });

    // Step 4: Email
    await sendReport(userEmail, {
      category,
      summary,
      extractedFields,
      confidence,
      imageUrl,
    });

    return Response.json({ success: true, documentId: doc.id });
  } catch (error: any) {
    console.error("Scan pipeline error:", error);
    return Response.json(
      { error: error.message || "Internal server error" },
      { status: 500 }
    );
  }
}
```

---

## Rate Limit Cheat Sheet

| API | Free Tier | Your Hackathon Usage | Buffer |
|---|---|---|---|
| Google Cloud Vision | 1,000 req/month | ~50 requests | 95% unused |
| OpenAI GPT-4o-mini | Tier 1 (500 RPM) | ~150 requests | 70% unused |
| Supabase DB | 500MB storage | ~5MB | 99% unused |
| Supabase Storage | 1GB | ~10MB | 99% unused |
| Resend Email | 3,000 emails/month | ~30 emails | 99% unused |

**You won't hit any rate limits at a hackathon.** But always implement caching and retry logic anyway — judges notice production-ready code.

---

## Fallback Strategy

| If this fails... | Do this instead... |
|---|---|
| Google Cloud Vision | Use Tesseract.js (runs in browser, no API key needed) |
| OpenAI API | Use a simpler regex-based extraction for known document types |
| Supabase | Use localStorage for demo (hackathon judges won't care about persistence for MVP) |
| Resend | Show the report on-screen instead of emailing it |
| Any API is slow | Add a loading spinner + optimistic UI update |

**The hackathon rule:** Always have a plan B for every external dependency. If an API goes down during your demo, you should be able to switch to the fallback in under 2 minutes.
