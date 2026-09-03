# Example Prompts: BAD to GOOD

The difference between a mediocre AI output and a great one is usually 30 seconds of extra thought in your prompt. Below are five prompts for the same hackathon project — an internship tracker app — ranked from worst to best.

---

## Rank 5 (Worst): The One-Liner

```
Make me a web app.
```

**What you get:** A generic hello-world React app with no structure, no styling, no database. The AI has zero context about what you're building. You'll spend 2 hours rewriting everything.

**Why it fails:** You're asking the AI to guess your entire project scope. It's like telling a contractor "build me a house" without mentioning bedrooms, budget, or location.

---

## Rank 4: Vague but Somewhat Specific

```
Create a responsive dashboard for internship tracking.
Use a clean layout, add login, and keep the database schema simple.
```

**What you get:** A functional but generic dashboard. It'll have a table, maybe some filters. Login will be basic. The "clean layout" instruction is subjective — the AI picks its own interpretation.

**Why it's mediocre:** You mentioned features but not tech stack, not data model, not user flow. The AI fills in blanks with defaults that may not match your vision. You'll still do significant rework.

---

## Rank 3: Decent with Tech Stack

```
Build a Next.js 14 internship tracker with TypeScript and Tailwind CSS.
Include: user login with NextAuth, a form to add internships (company,
role, deadline, status), and a dashboard showing all applications in a
table. Use PostgreSQL for the database. Keep it simple — no advanced
features yet.
```

**What you get:** A working app with proper structure. Login works, form works, table displays data. The AI picks sensible defaults for components and styling.

**Why it's better:** You specified the stack, core features, and constraints. But you're still missing data model details and UI specifics, so expect some back-and-forth.

---

## Rank 2: Detailed and Actionable

```
Build a Next.js 14 internship tracker with TypeScript, Tailwind CSS,
and PostgreSQL (using Prisma ORM).

Data model:
- User: id, email, name, createdAt
- Internship: id, company (string), role (string), status (enum:
  "applied", "interview", "offer", "rejected"), deadline (date),
  notes (text), userId (foreign key)

Pages:
1. Landing page — hero section with tagline "Never miss an internship
   deadline" and a "Get Started" button
2. Login/Register — email + password with NextAuth, Google OAuth as
   secondary option
3. Dashboard — table view of all internships, sortable by deadline
   and status, with color-coded status badges (green=offer,
   yellow=interview, blue=applied, red=rejected)
4. Add Internship — form with all fields, redirects to dashboard
   after submit

Styling: Use a minimal design. White background, subtle gray borders,
one accent color (indigo-500). Font: Inter. Cards with slight
rounded corners and shadow.

Deploy to Vercel with environment variables for DATABASE_URL and
NEXTAUTH_SECRET.
```

**What you get:** Almost exactly what you want on the first try. The AI generates proper Prisma schema, functional pages, correct routing, and styling that matches your spec.

**Why it works:** You've eliminated ambiguity. The AI isn't guessing — it's implementing. The data model prevents schema mismatches. The styling spec means no ugly surprises.

---

## Rank 1 (Best): The Full Brief

```
You are building a hackathon project: an internship tracker for
college students. The goal is to help students organize their
internship applications in one place.

Tech stack: Next.js 14 (App Router), TypeScript, Tailwind CSS,
Prisma, PostgreSQL, NextAuth.js.

Project name: "TrackIntern"

Data model (Prisma schema):
  User { id String @id, email String @unique, name String,
         createdAt DateTime, internships Internship[] }
  Internship { id String @id, company String, role String,
               status Enum(APPLIED, INTERVIEW, OFFER, REJECTED),
               deadline DateTime, notes String?, userId String,
               user User @relation(fields: [userId], references: [id]) }

Pages (5 total):
  1. "/" — Marketing landing page. Hero: "Never lose track of your
     internship hunt." Subheadline explaining the problem. CTA button
     to sign up. Below: 3 feature cards (Track Deadlines, Status
     Dashboard, Smart Reminders) with simple SVG icons.
  2. "/auth/login" — Login page. Email + password form. "Sign in with
     Google" button below. Link to register page.
  3. "/auth/register" — Register page. Name, email, password fields.
     Auto-redirect to dashboard after registration.
  4. "/dashboard" — Main dashboard. Top bar with user name and logout
     button. Stats row: 4 cards showing counts for each status
     (Applied: 12, Interview: 3, Offer: 1, Rejected: 2). Below: a
     table of all internships sorted by deadline (nearest first).
     Each row: company, role, status badge (color-coded), deadline,
     edit/delete icons. "Add Internship" button in top right.
  5. "/internships/new" — Form page. Fields: company (text), role
     (text), status (dropdown), deadline (date picker), notes
     (textarea, optional). Submit saves to DB and redirects to
     dashboard with a success toast.

Design system:
  - Colors: white bg, gray-50 cards, indigo-500 primary, indigo-600
    hover, gray-900 text, gray-500 secondary text
  - Font: Inter (import from Google Fonts)
  - Border radius: rounded-lg for cards, rounded-md for buttons
  - Shadows: shadow-sm on cards, shadow-md on hover
  - Spacing: consistent 6-unit gaps (gap-6, p-6)

Deploy target: Vercel. Use environment variables (not hardcoded):
  DATABASE_URL, NEXTAUTH_URL, NEXTAUTH_SECRET, GOOGLE_CLIENT_ID,
  GOOGLE_CLIENT_SECRET.

Important: Generate the Prisma schema file first, then the layout
with nav, then each page. Work top-down.
```

**What you get:** Production-quality code on the first generation. Proper file structure, working auth, correct data relationships, styled exactly as specified, and deployment-ready config.

**Why it's the best:** You've given the AI a complete spec. It knows the project name, every data field, every page, exact copy, color values, and build order. There is almost zero ambiguity. The "work top-down" instruction prevents the AI from going off-track.

---

## Quick Reference: Prompt Checklist

Before hitting enter, make sure your prompt includes:

1. **Tech stack** — frameworks, languages, databases
2. **Data model** — what entities exist and their fields
3. **Page list** — every route with its purpose
4. **Specific copy** — exact headlines and button text
5. **Design tokens** — colors, fonts, spacing
6. **Constraints** — what NOT to build (prevents feature creep)
7. **Build order** — what to generate first

The extra 2 minutes you spend on a prompt saves 2 hours of rework.
