# Annotated Resource Notes — 10 Essential Hackathon Tools

Keep a living document like this before every hackathon. Share it with your team 48 hours before the event so nobody's searching for links during the sprint.

---

## 1. Vercel

**URL:** https://vercel.com

**What it does:** Deploy web apps (Next.js, React, Vue, Svelte, etc.) with zero config. Push to GitHub, get a live URL in 30 seconds.

**Why it matters for hackathons:** You NEED a working demo link for judges. Vercel gives you one in seconds with no DevOps. Every minute you spend on deployment is a minute not spent building.

**Free tier:** Unlimited deploys, custom domains, serverless functions, analytics. Covers everything a hackathon needs. No credit card required.

**Pro tip:** Pre-connect your GitHub account BEFORE the hackathon. Create a Vercel team, add your teammates. Day-of setup eats 15 minutes you don't have.

**Use this when:** You're building a web app and need a live URL for judges. This should be your default unless you have a specific reason not to use it.

---

## 2. Figma

**URL:** https://figma.com

**What it does:** Collaborative design tool — wireframes, UI mockups, and prototypes. Works in the browser.

**Why it matters for hackathons:** A 10-minute wireframe before coding saves 2 hours of "wait, what does this page look like?" arguments. Design-first teams ship faster than code-first teams.

**Free tier:** Unlimited files, 3 Figma projects, real-time collaboration for up to 2 designers. More than enough for hackathons.

**Pro tip:** Create a shared Figma file with your team BEFORE the event. Set up a basic design system (colors, fonts, 3-4 component variants). When you start building, you're pulling from a system, not inventing pixels.

**Use this when:** Your project has a UI. Even a simple wireframe of "what goes where" prevents misalignment between frontend and backend teammates.

---

## 3. Stripe

**URL:** https://stripe.com

**What it does:** Payment processing API — accept credit cards, subscriptions, and invoices.

**Why it matters for hackathons:** If your project involves money (marketplaces, SaaS, subscriptions), Stripe is the fastest way to show "this can actually charge users." Judges love revenue models that don't require explaining the payment flow.

**Free tier:** No monthly fees. 2.9% + $0.30 per transaction. Test mode with fake cards — you never touch real money during a hackathon.

**Pro tip:** Use Stripe's test mode with their documented test card numbers (4242 4242 4242 4242). Set up webhooks for payment success/failure in the first 2 hours — this is the part that breaks most teams.

**Use this when:** Your project involves any kind of payment, subscription, or financial transaction. Also use when you want to show judges a revenue model, even if the actual payments are simulated.

---

## 4. Clerk or NextAuth.js

**URLs:** https://clerk.com / https://next-auth.js.org

**What they do:** User authentication — sign up, log in, session management. Clerk is a hosted service; NextAuth is self-hosted.

**Why it matters for hackathons:** Auth is table stakes. Every judge expects user accounts. Building auth from scratch wastes 3-4 hours and introduces security bugs. Use a library.

**Free tier:**
- Clerk: 10,000 monthly active users, Google/social logins, hosted login pages
- NextAuth: Completely free, self-hosted, supports 50+ providers

**Pro tip:** If your project is Next.js, use NextAuth — it's already in the ecosystem. If you want the fastest possible setup with beautiful UI, use Clerk. Either way, set up auth in the first hour. It touches every other feature.

**Use this when:** Your app has user accounts. Which one depends on your stack — NextAuth for Next.js purists, Clerk for speed.

---

## 5. Prisma

**URL:** https://prisma.io

**What it does:** Database ORM for Node.js/TypeScript — defines your schema in a single file, generates type-safe queries, handles migrations.

**Why it matters for hackathons:** Raw SQL in a hackathon is a nightmare. Prisma gives you type-safe queries with autocomplete. When you're coding at 3 AM, your IDE catching a column name typo saves you 30 minutes of debugging.

**Free tier:** Prisma is open source and free. Works with PostgreSQL, MySQL, SQLite, and MongoDB. Use SQLite for local dev (zero setup) and PostgreSQL for production (Vercel Postgres is free).

**Pro tip:** Run `npx prisma studio` during development — it opens a visual database browser. Faster than writing SELECT queries to check if your seed data worked.

**Use this when:** You're using a SQL or MongoDB database with a JavaScript/TypeScript backend. If you're using Supabase or Firebase, skip Prisma — they have their own query layers.

---

## 6. Tailwind CSS

**URL:** https://tailwindcss.com

**What it does:** Utility-first CSS framework — build UI by composing small classes instead of writing custom CSS.

**Why it matters for hackathons:** You will NOT have time to write CSS from scratch. Tailwind lets you prototype a polished UI in minutes. Most hackathon-winning projects use Tailwind or a Tailwind-based component library.

**Free tier:** Completely free and open source. Pair with shadcn/ui (https://shadcn.dev) for pre-built, accessible components.

**Pro tip:** Install the Tailwind VS Code extension before the event. The autocomplete for class names saves enormous time. Also, bookmark the Tailwind docs — the search is excellent and you'll use it constantly.

**Use this when:** You're building any web UI. There's no reason to use raw CSS in a hackathon. If you already know another CSS framework well (Bootstrap, Bulma), use that instead — familiarity beats novelty in a time crunch.

---

## 7. OpenAI API

**URL:** https://platform.openai.com

**What it does:** Access GPT-4, DALL-E, Whisper, and other AI models via API.

**Why it matters for hackathons:** AI features are the fastest way to make a judge say "wow." Even a simple "summarize this" or "classify this" feature powered by GPT-4 feels magical. Many hackathons have specific AI categories with separate prizes.

**Free tier:** $5 credit for new accounts (as of 2026). Enough for hundreds of API calls during a hackathon. GPT-4o-mini is cheap ($0.15/1M input tokens).

**Pro tip:** Use GPT-4o-mini for prototyping — it's 10x cheaper than GPT-4 and fast enough for most use cases. Upgrade to GPT-4 only if you need complex reasoning. Set a token limit in your code so a bug doesn't cost you $50 in one run.

**Use this when:** Your project has any AI/ML feature — text generation, classification, summarization, image analysis, embeddings. Also use when you want to add "AI-powered" to your pitch (judges love it, but only if it actually works).

---

## 8. GitHub

**URL:** https://github.com

**What it does:** Code hosting, version control, collaboration. Every hackathon team needs this.

**Why it matters for hackathons:** Judges look at your GitHub repo. A clean repo with a good README, recent commits, and organized code signals "this team is professional." A messy repo with no README signals "we threw this together."

**Free tier:** Unlimited public and private repos, GitHub Actions (2,000 minutes/month), GitHub Pages (free static hosting).

**Pro tip:** Create the repo and README BEFORE the hackathon starts. Add the project description, tech stack, and team members. When judges visit your GitHub during the demo, they see a polished page, not an empty repo.

**Use this when:** Always. Non-negotiable. If your team isn't using GitHub (or Git), you have a bigger problem than tooling.

---

## 9. Resend

**URL:** https://resend.com

**What it does:** Transactional email API — send emails from your app with a clean developer experience.

**Why it matters for hackathons:** If your project involves notifications, confirmations, or alerts, email is the simplest way to show it. Resend takes 10 minutes to set up vs. hours for SendGrid or AWS SES configuration.

**Free tier:** 3,000 emails/month, 100 emails/day. Covers every hackathon use case. No credit card required.

**Pro tip:** Use their React Email integration — write email templates as React components. It's faster than hand-coding HTML emails and the templates look professional. Set up a `noreply@yourproject.com` alias for the demo — it looks more legitimate than a Gmail address.

**Use this when:** Your project sends any kind of email — welcome messages, notifications, password resets, weekly digests. Skip email entirely if your project doesn't need it (don't add features just to use a tool).

---

## 10. Linear

**URL:** https://linear.app

**What it does:** Project management tool built for software teams — issues, sprints, roadmaps. Faster and cleaner than Jira or Trello.

**Why it matters for hackathons:** At hour 20, your team forgets what was decided at hour 4. Linear keeps everyone aligned — who's building what, what's done, what's blocking. It's the difference between 4 people building in parallel vs. 4 people building in circles.

**Free tier:** Up to 250 issues, unlimited members. Enough for any hackathon.

**Pro tip:** Set up a Linear project 48 hours before the event. Pre-create issues for your planned features using your Figma wireframes as reference. When the hackathon starts, your team picks up issues instead of spending an hour deciding what to build.

**Use this when:** Your team has 3+ people. For 2-person teams, a shared Notion doc or even a text file works fine. For 3+, you need structure or you'll lose the plot.

---

## The Hackathon Toolkit Cheat Sheet

| Category | Tool | Setup time | Must-have? |
|----------|------|-----------|-----------|
| Hosting | Vercel | 5 min | Yes |
| Design | Figma | 15 min (shared file) | Recommended |
| Payments | Stripe | 30 min | If payments are a feature |
| Auth | Clerk or NextAuth | 30 min | Yes (if user accounts) |
| Database | Prisma | 10 min | Yes (if database needed) |
| Styling | Tailwind CSS | 5 min | Yes |
| AI | OpenAI API | 10 min | If AI is a feature |
| Version control | GitHub | 5 min | Yes, always |
| Email | Resend | 10 min | If emails are a feature |
| Project management | Linear | 15 min | Recommended for 3+ people |

**Total setup time for a typical project:** ~90 minutes. Do it BEFORE the hackathon. Day-of setup is dead time.

---

## How to Use This Document

1. **Before the hackathon:** Create accounts on every tool you'll need. Verify emails, set up teams, connect GitHub.
2. **48 hours before:** Share this doc with your team. Everyone should have access to shared Figma, Linear, and Vercel.
3. **During the hackathon:** Keep this doc open. When someone says "where's the Stripe dashboard?" — the answer is in here.
4. **After the hackathon:** Update this doc with what worked and what didn't. Your future hackathon self will thank you.
