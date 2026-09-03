# Example Vercel Deployment Walkthrough: TrackIntern

This is a real deployment session with actual error messages, debugging steps, and fixes. Follow along to see how a typical hackathon deployment goes — including the parts that go wrong.

---

## Step 1: Connect the Repository (2 minutes)

1. Go to [vercel.com/new](https://vercel.com/new)
2. Click "Import Git Repository"
3. Select the GitHub repo: `yourname/trackintern`
4. Vercel auto-detects Next.js. Framework preset: **Next.js**. Build command: `next build`. Output directory: `.next`.
5. Click "Deploy"

**What happens:** Vercel clones your repo, runs `npm install`, then `next build`. You see a live build log.

**First deploy result:** ✅ Build succeeded in 47 seconds. Vercel assigns a random URL: `trackintern-a3k2f9.vercel.app`.

**But wait** — the app loads but shows an error page. That's expected. We haven't set up environment variables yet.

---

## Step 2: Environment Variables (5 minutes)

Go to your project → Settings → Environment Variables.

Add these one by one:

| Variable | Value | Notes |
|----------|-------|-------|
| `DATABASE_URL` | `postgresql://user:pass@db.supabase.co:5432/trackintern` | Your Supabase connection string |
| `NEXTAUTH_URL` | `https://trackintern.vercel.app` | Must match your deployment URL exactly |
| `NEXTAUTH_SECRET` | `a3k2f9x7b1m4...` | Generate with `openssl rand -base64 32` |
| `GOOGLE_CLIENT_ID` | (leave empty for now) | We're not using Google OAuth in the demo |
| `GOOGLE_CLIENT_SECRET` | (leave empty for now) | Same |

**Critical detail:** Set each variable for **Production**, **Preview**, AND **Development**. Vercel treats these as separate environments. If you only set Production, your preview deployments (which happen on every PR) will break.

After adding all variables, click "Redeploy" → "Redeploy with existing Build Cache" unchecked.

---

## Step 3: First Real Deploy (3 minutes)

**Build log output:**
```
[14:23:01] Cloning repository...
[14:23:05] Installing dependencies...
[14:23:32] Running build command...
[14:23:45] ▲ Next.js 14.2.5
[14:23:45] Creating an optimized production build...
[14:24:01] Compiled successfully
[14:24:03] Linting and checking validity of types...
[14:24:08] Collecting page data...
[14:24:12] Generating static pages (0/5)...
[14:24:15] Error: prisma/generated/client not found
```

**The error:** Prisma client wasn't generated during the build. This happens when `prisma generate` isn't in your build script.

**Fix:** In `package.json`, update the build script:
```json
"build": "prisma generate && next build"
```

Commit, push, Vercel auto-redeploys.

**Second build result:** ✅ Build succeeded. App loads. Login page works. Dashboard shows data from Supabase. 

---

## Step 4: Custom Domain Setup (10 minutes)

We wanted a clean URL for the demo: `trackintern.app`

### Option A: Buy a domain through Vercel
1. Project → Settings → Domains
2. Type `trackintern.app` → Click "Buy"
3. Vercel charges ~$12/year for `.app` domains
4. DNS is configured automatically — no extra steps

### Option B: Use a domain you already own
1. Project → Settings → Domains
2. Enter your domain → Click "Add"
3. Vercel shows you DNS records to configure:

```
Type: A
Name: @
Value: 76.76.21.21

Type: CNAME
Name: www
Value: cname.vercel-dns.com
```

4. Go to your domain registrar (Namecheap, Google Domains, etc.)
5. Add those DNS records
6. Wait 5-30 minutes for propagation

**We went with Option A** because it was faster. Domain was live in under 2 minutes.

**SSL:** Vercel provisions a free SSL certificate automatically via Let's Encrypt. No configuration needed. Your site is `https://` by default.

---

## Step 5: Performance Optimization (15 minutes)

After deploying, we ran Lighthouse to check performance.

**First Lighthouse score:** 72/100 (not great)

**Issues found and fixes:**

### Issue 1: Large bundle size
```
First Contentful Paint: 2.8s
Total Blocking Time: 850ms
```
**Diagnosis:** We were importing all of `@prisma/client` in client components.

**Fix:** Moved all Prisma queries to API routes. Client components only fetch from `/api/...` endpoints. Rebuilt.

**After fix:** FCP dropped to 1.4s, TBT dropped to 320ms.

### Issue 2: Unoptimized images
```
Properly size images: potential savings of 120 KiB
```

**Diagnosis:** The hero section had a decorative SVG that was 200KB (exported from Figma at full resolution).

**Fix:** Ran the SVG through [svgomg.net](https://svgomg.net). File went from 200KB to 18KB. Also converted it to an inline SVG component instead of an `<img>` tag.

### Issue 3: No font loading optimization
```
Ensure text remains visible during webfont load
```

**Diagnosis:** Google Fonts import was blocking render.

**Fix:** Added `font-display: swap` via the Next.js `next/font` module:
```tsx
import { Inter } from 'next/font/google'
const inter = Inter({ subsets: ['latin'], display: 'swap' })
```

**Final Lighthouse score:** 96/100 ✅

---

## Step 6: When Things Break — A Debugging Session

### The Midnight Crash

At 11 PM the night before submission, the app started returning 500 errors. Here's the actual debugging session:

**11:00 PM — Error reported:**
```
POST /api/internships 500 Internal Server Error
```

**11:02 PM — Checked Vercel function logs:**
```
RuntimeError: PrismaClientKnownRequestError:
Invalid `prisma.internship.create()` invocation

Unique constraint failed on the fields: (`id`)
```

**11:05 PM — Diagnosis:** We were generating IDs manually with `crypto.randomUUID()` but Prisma was also trying to auto-generate IDs. Conflict.

**11:08 PM — Fix:** Removed the manual ID generation from the API route. Let Prisma handle it.

```diff
- const id = crypto.randomUUID()
- const internship = await prisma.internship.create({
-   data: { id, company, role, ... }
- })
+ const internship = await prisma.internship.create({
+   data: { company, role, ... }
+ })
```

**11:10 PM — Pushed fix. Vercel auto-deployed.**

**11:12 PM — New error:**
```
Error: Can't reach database server at `db.supabase.co:5432`
```

**11:14 PM — Diagnosis:** Supabase free tier pauses databases after 7 days of inactivity. We hadn't accessed it in 3 days.

**11:16 PM — Fix:** Went to Supabase dashboard → Database → clicked "Restore". Database came back online in 30 seconds.

**11:18 PM — Final test:** All endpoints working. Saved the Supabase restore URL as a bookmark for future reference.

**Total debug time:** 18 minutes. If we hadn't committed hourly, finding the ID bug would've taken much longer.

---

## Step 7: Monitoring Setup (5 minutes)

Even for a hackathon, basic monitoring helps you catch issues before judges see them.

### Vercel Analytics (free)
1. Project → Analytics → Enable
2. Tracks: page views, web vitals, visitors
3. Useful for showing judges real usage numbers during your pitch

### Vercel Logs (free tier)
1. Project → Logs → Runtime Logs
2. Shows serverless function invocations, errors, and latency
3. Set up a filter for `500` errors so you see them instantly

### Simple Health Check
We added a `/api/health` endpoint:
```typescript
export default async function handler(req, res) {
  try {
    await prisma.$queryRaw`SELECT 1`
    res.status(200).json({ status: 'ok', db: 'connected' })
  } catch (e) {
    res.status(500).json({ status: 'error', db: 'disconnected' })
  }
}
```

Checked this every 30 minutes during the hackathon. Caught the Supabase pause issue 2 hours before our demo.

---

## Quick Reference: Deployment Checklist

```
□ Build script includes `prisma generate`
□ All env vars set for Production + Preview + Development
□ NEXTAUTH_URL matches deployment URL exactly
□ Database is cloud-based (not local)
□ Custom domain configured (if using)
□ SSL working (automatic on Vercel)
□ Lighthouse score > 90
□ /api/health endpoint exists
□ Console.logs removed from production code
□ README updated with live URL
□ Team members can access Vercel dashboard
```

---

## Time Budget for Deployment

| Task | Time |
|------|------|
| Connect repo + first deploy | 5 min |
| Environment variables | 5 min |
| Fix build errors (2 rounds) | 10 min |
| Custom domain | 5 min |
| Performance optimization | 15 min |
| Debugging unexpected errors | 15 min |
| Monitoring setup | 5 min |
| **Total** | **60 min** |

**Pro tip:** Start deployment at hour 4 of a 6-hour hackathon. If deployment takes longer than 60 minutes, you have buffer. If it's fast, you get extra polish time.
