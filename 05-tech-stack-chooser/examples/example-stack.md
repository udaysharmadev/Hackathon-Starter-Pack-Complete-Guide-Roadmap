# Example Stack: Before/After — The Same Project, Two Different Outcomes

Both teams built a "Student Deadline Tracker" at the same 36-hour hackathon. Same idea. Same team size (3 people). One team chose poorly. The other chose well. Here's what happened.

---

## The Project

An app where students can:
1. Add assignment deadlines (course, title, due date, priority)
2. See a dashboard with upcoming deadlines
3. Get email reminders 24 hours before due
4. Mark assignments complete

Simple enough. The difference was entirely in the stack.

---

## Team A: The Wrong Stack

**What they chose:**
- **Backend:** Django (Python)
- **Database:** MongoDB
- **Auth:** Custom-built with bcrypt + JWT tokens
- **Frontend:** Plain HTML/CSS/JS with jQuery
- **Deployment:** Heroku (free tier)

### The Time Breakdown

| Task | Time Spent | Why It Took So Long |
|---|---|---|
| Set up Django project + virtualenv + dependencies | 1.5 hours | Virtualenv issues. Pip dependency conflicts between Django 4.2 and a package requiring Django 3.9. Had to downgrade. |
| Set up MongoDB connection | 2 hours | Django doesn't natively support MongoDB. Had to install `djongo` which is unmaintained. Switched to `mongoengine` which required restructuring all models. |
| Build custom auth (registration, login, JWT) | 4 hours | Had to manually handle: password hashing, token generation, token refresh, session management, CORS headers. Each step had a bug. |
| Build the assignment CRUD | 3 hours | MongoDB document structure was harder than expected. Decided on embedding vs. referencing. Had to rebuild the data model twice. |
| Build the dashboard UI | 3 hours | jQuery DOM manipulation for dynamic rendering. No component system. Code became spaghetti fast. Had to rewrite the dashboard rendering twice. |
| Add email reminders | 2.5 hours | Celery setup for background tasks took 1.5 hours alone (Redis broker, worker configuration). Debugging email sending with Gmail SMTP took another hour. |
| Fix deployment issues | 4 hours | Heroku didn't support MongoDB well. Switched to MongoDB Atlas. Configured env vars. Debugged CORS. Fixed static file serving. |
| Final debugging + polish | 2 hours | jQuery selector bugs. MongoDB connection pool exhaustion. JWT token not refreshing correctly. |
| **TOTAL** | **22 hours** | **Left with 14 hours of buffer, but used 12 of those fixing bugs. Presented a half-working demo.** |

### What Went Wrong

1. **MongoDB + Django = pain.** Django is built for SQL databases. Every ORM feature they tried to use didn't work with MongoDB. They spent 2 hours just getting the database connection stable.

2. **Custom auth stole 4 hours.** That's 11% of the entire hackathon spent on something Supabase or Clerk gives you in 10 minutes. Auth is a solved problem — don't rebuild it.

3. **jQuery for dynamic UI was painful.** No component system meant every UI update required manual DOM manipulation. The dashboard code was 400 lines of spaghetti jQuery. A component-based framework (React, Vue, Svelte) would've been 80 lines.

4. **Celery for background jobs was overkill.** They needed to send one email 24 hours before a deadline. Celery requires Redis, a worker process, and task configuration. They spent 1.5 hours just setting up the infrastructure for one simple job.

5. **Heroku + MongoDB deployment was a nightmare.** Heroku's free tier doesn't play well with MongoDB. They had to switch to Atlas mid-hackathon, which meant changing connection strings, debugging firewall rules, and reconfiguring everything.

### What They Presented

A working login page, a form to add assignments (that sometimes saved to the database), and a dashboard that showed assignments but didn't update without a page refresh. Email reminders didn't work. The judges saw a login screen and a form. Not impressive.

---

## Team B: The Right Stack

**What they chose:**
- **Full-stack framework:** Next.js 14 (React)
- **Database:** Supabase (PostgreSQL)
- **Auth:** Clerk
- **Styling:** Tailwind CSS
- **Hosting:** Vercel
- **Email:** Resend

### The Time Breakdown

| Task | Time Spent | Why It Was Fast |
|---|---|---|
| Set up Next.js project + Tailwind | 15 minutes | `npx create-next-app` + one config file. Tailwind included by default. |
| Set up Supabase + create tables | 20 minutes | Supabase dashboard → SQL editor → 3 CREATE TABLE statements → done. Auth, realtime, and API endpoints auto-generated. |
| Set up Clerk auth | 10 minutes | `<ClerkProvider>` in layout, two components (`<SignedIn>`, `<SignedOut>`), Google SSO enabled by default. |
| Build the assignment CRUD | 1 hour | Supabase auto-generates REST API. `fetch('/api/assignments')` for GET, POST with JSON body. No backend code needed. |
| Build the dashboard UI | 1.5 hours | Tailwind for styling (no CSS file needed). React components for each section. Dynamic rendering with `useState` and `useEffect`. |
| Add email reminders | 1 hour | Resend API: 3 lines of code to send an email. For the 24-hour reminder: simple `setTimeout` on the server + a `cron` job for reliability. No Celery, no Redis. |
| Deploy to Vercel | 10 minutes | `git push` → Vercel auto-deploys. Done. No configuration needed. |
| Final debugging + polish | 1 hour | Minor Tailwind alignment issues. One Supabase RLS policy fix. |
| **TOTAL** | **5.5 hours** | **Left with 30.5 hours of buffer. Used 20 of those adding features: search, sorting, priority filters, a chart showing completion rate, and a landing page.** |

### What Went Right

1. **Supabase replaced 4 tools.** Database, API, auth (backup), and real-time — all in one. No Celery, no Redis, no separate API layer. One dashboard, one connection string.

2. **Clerk gave them auth in 10 minutes.** Registration, login, Google SSO, JWT handling, session management — all handled. They didn't write a single line of auth code.

3. **Next.js API routes eliminated the backend.** No separate Django server. API routes live inside the Next.js project. One codebase, one deployment.

4. **Tailwind meant no CSS debugging.** No "why is this div 2px off?" moments. Utility classes in the JSX. The dashboard looked polished in 30 minutes.

5. **Vercel deploy was instant.** No Heroku, no MongoDB Atlas, no CORS config, no env var debugging. `git push` → live URL.

### What They Presented

A fully working app with: Google SSO login, a dashboard with 12 pre-seeded assignments, working add/edit/delete, a priority filter, a search bar, a completion chart (Chart.js), and a polished landing page. They also had time to add a "study streak" gamification feature. The judges saw a product, not a prototype.

---

## The Side-by-Side Comparison

| Metric | Team A (Wrong Stack) | Team B (Right Stack) |
|---|---|---|
| **Setup time** | 3.5 hours | 45 minutes |
| **Auth implementation** | 4 hours | 10 minutes |
| **Database setup** | 2 hours | 20 minutes |
| **Background jobs** | 2.5 hours | 1 hour |
| **Deployment** | 4 hours | 10 minutes |
| **Total build time** | 22 hours | 5.5 hours |
| **Features delivered** | Login, add form, broken dashboard | Login, full CRUD, dashboard, search, charts, gamification |
| **Demo quality** | Half-working | Fully polished |
| **Bugs during demo** | 3 (database timeout, JWT error, UI freeze) | 0 |

---

## The Lesson

The stack isn't about what's "best" or "most popular." It's about **what gets you to a working demo fastest.**

**Team A's mistake:** They chose based on what they knew from their day job (Django, MongoDB) instead of what was fastest for a hackathon. They also chose to build solved problems (auth, background jobs) instead of using services.

**Team B's choice:** They chose based on one criterion: "What lets us ship a working product in the least time?" Every tool was selected for speed, not purity.

**The rule of thumb:** If a service has a free tier and solves your problem, use it. Don't build auth — use Clerk. Don't build a database API — use Supabase. Don't configure deployment — use Vercel. Save your 36 hours for the thing that makes your project unique.
