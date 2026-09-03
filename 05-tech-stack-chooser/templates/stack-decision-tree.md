# Stack Decision Tree

Start at the top. Answer honestly. The tree will tell you what to build with.

---

## Step 1: What Are You Building?

### Web App (browser-based)
→ Go to **Step 2A**

### Mobile App (iOS/Android)
→ Go to **Step 2B**

### CLI Tool / Backend Service (no UI)
→ Go to **Step 2C**

### Hardware / IoT / AR
→ Go to **Step 2D**

---

## Step 2A: Web App

### Q: Do you need server-side rendering (SEO, fast first paint)?
**Yes →** Use **Next.js** (React) or **Nuxt** (Vue)
**No →** Go to next question

### Q: Do you need a backend (database, auth, API)?
**Yes, complex →** Go to **Step 3A** (Backend selection)
**Yes, simple →** Use **Supabase** or **Firebase** — they give you auth + DB + realtime out of the box
**No, static →** Use **Next.js** on Vercel, or **Astro** for maximum speed

### Q: How comfortable is your team with React?
**Very →** Next.js + Tailwind + shadcn/ui
**Somewhat →** Next.js (use templates, don't build from scratch)
**Not at all →** Use **SvelteKit** or **Vue + Nuxt** (lower learning curve)

---

## Step 2B: Mobile App

### Q: Do you need both iOS and Android?
**Yes, one codebase →** Go to next question
**Just one platform →** Use **SwiftUI** (iOS) or **Kotlin** (Android) — native is faster to build

### Q: Cross-platform framework preference?
**React →** **React Native** (Expo for zero-config setup)
**Flutter →** **Flutter** (better for complex UI, but Dart is a new language)
**Don't care →** **React Native + Expo** (bigger ecosystem, easier to find help)

### Q: Do you need backend/data?
**Yes →** **Supabase** (works great with React Native) or **Firebase**
**No →** Local storage only — skip backend entirely

---

## Step 2C: CLI / Backend Service

### Q: What language?
**Python →** **FastAPI** (modern, fast, great docs) or **Flask** (simpler)
**TypeScript →** **Express** (mature) or **Hono** (newer, edge-ready)
**Rust →** **Axum** or **Actix** (fastest possible)
**Go →** **Gin** or **Chi**

### Q: Do you need a database?
**Yes →** Go to **Step 3A**
**No →** File-based storage (JSON/SQLite) is fine for a hackathon

---

## Step 2D: Hardware / IoT / AR

**IoT with sensors →** **Arduino** + **PlatformIO** + **MQTT** broker
**AR on mobile →** **ARKit** (iOS) or **ARCore** (Android) or **8th Wall** (web AR)
**VR →** **Unity** + **Meta Quest SDK**
**Raspberry Pi project →** Python + **FastAPI** for control interface

---

## Step 3A: Backend & Database Selection

### Q: What's your database needs?
**Simple CRUD (users, posts, data) →** Go to next question
**Complex queries, joins, analytics →** **PostgreSQL** (via Supabase or direct)
**Key-value, caching →** **Redis** or **Upstash**
**Documents, flexible schema →** **MongoDB** (via Atlas free tier)
**File storage (images, files) →** **Supabase Storage** or **Cloudflare R2**

### Q: Do you need authentication?
**Yes, standard (email/password + OAuth) →** **Supabase Auth** or **Clerk**
**Yes, complex (roles, orgs, permissions) →** **Clerk** or **Auth.js**
**No →** Skip auth, use API keys or hardcoded tokens

### Q: Do you need real-time features (live updates, chat, notifications)?
**Yes →** **Supabase Realtime** or **Firebase** or **Socket.io**
**No →** Standard REST API is fine

---

## Step 3B: Deployment Decision Tree

### Q: What's your budget?
**$0 →** Go to next question
**$10–50 →** **Railway** ($5 credit) or **Render** (free tier + paid)
**$50+ →** **AWS/GCP/Azure** (overkill for a hackathon, but doable)

### $0 Deployment Options:

| Platform | What it handles | Limitations |
|----------|----------------|-------------|
| **Vercel** | Frontend / Next.js | No long-running backend (use serverless) |
| **Netlify** | Frontend / static | Same as Vercel |
| **Railway** | Full backend + DB | $5 free credit, then paidd |
| **Fly.io** | Full backend + DB | 3 shared VMs free |
| **Cloudflare Pages** | Frontend / Workers | Edge computing, no Node.js runtime |
| **Render** | Full stack | Free tier has cold starts (30s+) |
| **GitHub Pages** | Static only | No backend, no serverless |

### Q: Does your app need a backend running 24/7?
**Yes →** **Railway** or **Fly.io** (free tier)
**No (serverless is fine) →** **Vercel** (API routes) or **Netlify Functions**
**Not sure →** Start with Vercel, migrate if needed

---

## Decision Summary Tables

### Frontend Stack Quick Pick

| Need | Stack | Why |
|------|-------|-----|
| Fastest possible | Next.js + Tailwind + shadcn/ui | Battle-tested, huge ecosystem |
| Lowest learning curve | SvelteKit or Vue + Nuxt | Simpler syntax, less boilerplate |
| Best for complex UI | React + Tailwind | Most flexible, most examples |
| Best for mobile-first | React Native + Expo | One codebase, both platforms |
| Best for real-time | Next.js + Supabase Realtime | Built-in realtime layer |
| Best for static/blog | Astro | Fastest static generation |

### Backend Stack Quick Pick

| Need | Stack | Why |
|------|-------|-----|
| Fastest setup | Supabase | Auth + DB + API + Realtime in 5 min |
| Python + speed | FastAPI | Async, auto-docs, type hints |
| Python + simplicity | Flask | Minimal, well-known |
| TypeScript backend | Express or Hono | Mature ecosystem |
| No backend needed | Firebase | Google's managed backend |

### Database Quick Pick

| Data Type | Database | Free Tier |
|-----------|----------|-----------|
| Structured data, relationships | PostgreSQL (Supabase) | 500MB |
| Flexible documents | MongoDB Atlas | 512MB |
| Key-value, sessions | Redis (Upstash) | 10K commands/day |
| Files, images | Supabase Storage / R2 | 1GB / 10GB |
| Simple local storage | SQLite | Unlimited |

---

## "If You Already Know X" Shortcuts

### "I know React"
→ **Next.js + Tailwind + Supabase + Vercel**
This is the fastest path for most hackathon projects. You'll be productive in 15 minutes.

### "I know Python"
→ **FastAPI + Supabase + PostgreSQL + Railway**
Build your API in Python, let Supabase handle auth and realtime.

### "I know Django"
→ **Django + SQLite + Vercel (or Railway)**
Django is heavy for a hackathon but if you know it well, ship with it.

### "I know Flutter"
→ **Flutter + Firebase**
Classic combo. Firebase handles everything backend.

### "I know nothing, just starting"
→ **Next.js + Supabase + Vercel**
The tutorial ecosystem is massive. You can find a walkthrough for anything.

---

## Budget-Aware Paths

### Path A: $0 Budget (Everything Free)
- Frontend: Next.js on Vercel
- Backend: Supabase (free tier)
- Database: PostgreSQL via Supabase
- Auth: Supabase Auth
- Hosting: Vercel (frontend) + Supabase (backend)
- **Total: $0/month**

### Path B: $10 Budget
- Everything from Path A, plus:
- OpenAI API: $5 credit
- Custom domain: $1 (Namecheap)
- **Total: ~$6 one-time**

### Path C: $50 Budget
- Everything from Path A, plus:
- Railway backend: $5/month
- OpenAI API: $20
- Stripe (for payments): free until you make money
- Professional domain: $12/year
- **Total: ~$37 first month**

---

## Team-Size-Aware Paths

### Solo Hacker (1 person)
- **Strategy:** Maximize leverage. Use managed services for everything.
- **Stack:** Next.js + Supabase + Vercel
- **Why:** Zero DevOps. Focus on the product, not infrastructure.
- **Rule:** If it takes more than 10 minutes to set up, find an alternative.

### Small Team (2–3 people)
- **Strategy:** Split frontend/backend. Use shared types.
- **Stack:** Next.js (frontend) + FastAPI or Supabase (backend)
- **Why:** Clean separation. Two people can work in parallel.
- **Rule:** Set up shared TypeScript types on day 1.

### Larger Team (4+ people)
- **Strategy:** Microservices + clear ownership.
- **Stack:** Next.js (frontend) + FastAPI (API) + Supabase (DB) + separate services
- **Why:** Multiple people can work on different services simultaneously.
- **Rule:** Define API contracts in the first hour. No guessing.

---

## Emergency Fallback Stacks

**"We're behind schedule and need to ship SOMETHING":**
→ **Next.js + Supabase + Vercel** — deploy a basic CRUD app in 30 minutes
→ Use a template: [shipfa.st](https://shipfa.st) or [nextjs-starter](https://github.com/vercel/next.js/tree/canary/examples)

**"Our backend is broken and we can't fix it":**
→ Switch to **Supabase** for everything. It's a backend-as-a-service.

**"We can't deploy":**
→ Use **Replit** or **CodeSandbox** — instant deployment, zero config

**"We don't have time to build a UI":**
→ Use **v0.dev** to generate React components from descriptions
→ Use **shadcn/ui** components — copy-paste ready

---

## The Only Rule That Matters

> **The best stack is the one your team already knows.** A hackathon is not the time to learn a new framework. Use what you're productive with. Speed > perfection.

If you're still unsure, pick **Next.js + Supabase + Vercel**. It works for 90% of hackathon projects and you'll find help everywhere.

---

*Decision tree v1.0 — Adapt based on your team's strengths and the hackathon's requirements.*
