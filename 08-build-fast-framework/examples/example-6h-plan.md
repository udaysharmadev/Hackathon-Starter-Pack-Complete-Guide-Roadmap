# Example 6-Hour Build Plan: Internship Tracker

**Project:** TrackIntern — a dashboard for college students to manage internship applications
**Team:** 3 people (2 developers, 1 designer/pitch lead)
**Hackathon time block:** 6 hours (10:00 AM – 4:00 PM)
**Stack:** Next.js 14, Tailwind CSS, Prisma, PostgreSQL, Vercel

---

## Hour 1: Scaffold & Setup (10:00 – 11:00)

**Planned:** Initialize repo, install dependencies, set up database, build landing page.

**What actually happened:**
- 10:00–10:10: Created GitHub repo, ran `npx create-next-app@latest`. Smooth.
- 10:10–10:25: Installed Tailwind, Prisma, NextAuth. Tailwind config worked first try. Prisma init worked but we hit a snag — PostgreSQL wasn't running locally. Spent 12 minutes realizing we hadn't started Postgres via Homebrew.
- 10:37–10:50: Got the database running. Created the Prisma schema (User + Internship models). Ran `npx prisma db push` — it worked. Felt good.
- 10:50–11:00: Built the landing page hero section. Just a headline, subheadline, and a CTA button. Kept it simple.

**Time spent vs planned:** 60 min vs 60 min (on track, but the Postgres hiccup ate buffer time)

**Energy level:** 9/10. Coffee kicked in. Everyone's excited.

**Save point:** ✅ Commit: "scaffold: Next.js + Prisma + landing page"

**Lesson learned:** Start database setup FIRST. If Postgres wasn't installed, that 12-minute fix could've been 30 minutes.

---

## Hour 2: Auth & Data Layer (11:00 – 12:00)

**Planned:** Implement NextAuth login, create API routes for internships.

**What actually happened:**
- 11:00–11:20: Set up NextAuth with email/password provider. The config file took three tries — first attempt used the wrong adapter, second missed the session callback, third worked. Classic NextAuth friction.
- 11:20–11:40: Built API routes: GET /api/internships (list), POST /api/internships (create), DELETE /api/internships/:id. Used Prisma client directly. Had a bug where the POST route wasn't parsing the body correctly — turned out we forgot to add `body-parser` config. Fixed in 5 minutes.
- 11:40–12:00: Connected auth to the API routes (middleware to check session). First time seeing data flow from form → API → database → page. Satisfying moment.

**Time spent vs planned:** 60 min vs 60 min (on track)

**Energy level:** 8/10. Solid focus. One person grabbed snacks during the API debugging.

**Save point:** ✅ Commit: "feat: auth + API routes for internships"

**Lesson learned:** NextAuth always takes longer than you think. Budget 20 minutes minimum for config issues.

---

## Hour 3: Dashboard UI (12:00 – 1:00 PM)

**Planned:** Build the main dashboard with table view and stats cards.

**What actually happened:**
- 12:00–12:20: Built the stats row — 4 cards showing counts per status. Used `useEffect` to fetch data. Cards looked clean with Tailwind.
- 12:20–12:45: Built the internships table. This took longer than expected because we wanted sortable columns. Spent 15 minutes on sort logic before deciding to cut it — just sort by deadline on the server side. **Decision: cut scope, ship simple.**
- 12:45–1:00: Added color-coded status badges (green, yellow, blue, red). The designer picked colors that didn't contrast well on white backgrounds. Quick fix: bumped saturation. Looked great after.

**Time spent vs planned:** 60 min vs 60 min (on track, but only because we cut sorting)

**Energy level:** 7/10. Post-lunch dip starting. One person stepped out for a walk.

**Save point:** ✅ Commit: "feat: dashboard with stats cards and table"

**Lesson learned:** "Sortable columns" sounds simple but eats time. Server-side sort by one field is enough for a hackathon demo.

---

## Hour 4: Form & Polish (1:00 – 2:00 PM)

**Planned:** Build the add-internship form, add delete functionality, polish UI.

**What actually happened:**
- 1:00–1:20: Built the form page. Company, role, status dropdown, deadline date picker, notes textarea. Used native HTML date input — no fancy library. Saved to database on submit. Redirected to dashboard. Clean.
- 1:20–1:35: Added delete button on each row with a confirmation dialog. Also added a "toast" notification on successful save (just a green div that fades out). Small touches that make the demo feel polished.
- 1:35–1:50: **Unexpected issue:** The Prisma client was creating a new connection on every API call. In production this would exhaust connections. Spent 15 minutes adding a global Prisma client singleton. Not demo-critical, but judges might ask about it.
- 1:50–2:00: Quick UI pass — adjusted padding, fixed a mobile responsiveness issue where the table overflowed on small screens (added `overflow-x-auto`).

**Time spent vs planned:** 60 min vs 60 min (on track)

**Energy level:** 6/10. That 2 PM wall is real. Someone made espresso.

**Save point:** ✅ Commit: "feat: form + delete + UI polish"

**Lesson learned:** The Prisma singleton thing is a real gotcha. Add it at the start, not hour 4.

---

## Hour 5: Deploy & Test (2:00 – 3:00 PM)

**Planned:** Deploy to Vercel, set up env vars, test everything live.

**What actually happened:**
- 2:00–2:10: Pushed to GitHub. Connected repo to Vercel. Build started automatically.
- 2:10–2:25: **Build failed.** Error: `Module not found: Can't resolve 'bcrypt'`. We were using bcrypt for password hashing but it's a native module that doesn't work on Vercel's edge runtime. Panic moment. Quick fix: switched to `bcryptjs` (pure JS implementation). Took 10 minutes including install and testing.
- 2:25–2:40: Set up environment variables in Vercel dashboard. DATABASE_URL, NEXTAUTH_SECRET, NEXTAUTH_URL (set to the Vercel domain). Redeployed. Build passed.
- 2:40–2:55: Tested the live URL. Login worked. Form worked. Dashboard loaded. BUT — the database was still our local Postgres. **Big problem.** We needed a cloud database. Signed up for Supabase (free tier), created a new project, got the connection string, updated Vercel env vars, redeployed. 15 minutes of scramble but it worked.
- 2:55–3:00: Final test on the live URL. Everything working end-to-end.

**Time spent vs planned:** 60 min vs 60 min (on track, but the database migration was stressful)

**Energy level:** 5/10. Deployment debugging is exhausting. Adrenaline from the bcrypt scare helped.

**Save point:** ✅ Commit: "deploy: fix bcrypt, switch to Supabase"

**Lesson learned:** ALWAYS use a cloud database from the start if you plan to deploy. Local Postgres → Supabase migration at hour 5 is terrifying. Also: test `bcryptjs` locally before deploy day.

---

## Hour 6: Rehearse & Ship (3:00 – 4:00 PM)

**Planned:** Write pitch, rehearse demo, finalize everything.

**What actually happened:**
- 3:00–3:15: Designer wrote the pitch script. Two attempts — first version was too technical ("We used Prisma ORM with a PostgreSQL backend..."). Judges don't care. Rewrote to focus on the problem: "67% of college students miss internship deadlines because they track them in scattered spreadsheets."
- 3:15–3:35: **Demo rehearsal #1.** Crashed and burned. The login page loaded but the Google OAuth button didn't work (we never set up Google credentials — only email/password). Cut the Google button from the UI in 3 minutes. Rehearsal #2 went smoothly.
- 3:35–3:50: **Demo rehearsal #3.** Timed it: 2 minutes 10 seconds. Too long. Cut the "how it works" explanation. Focused on: problem → live demo → impact numbers → call to action. Final time: 58 seconds.
- 3:50–4:00: Final commits. Cleaned up console.logs. Updated README with screenshots. Pushed final version. Deep breath.

**Time spent vs planned:** 60 min vs 60 min (on track)

**Energy level:** 4/10 but wired on caffeine and adrenaline. The finish line is close.

**Save point:** ✅ Commit: "chore: final polish + README"

**Final result:** Submitted project. Won "Best UI/UX" award. The clean design and smooth demo carried us — the code underneath had rough edges, but the judges never saw those.

---

## Post-Mortem: What We'd Do Differently

| Issue | Time Lost | Prevention |
|-------|-----------|------------|
| Postgres not running | 12 min | Pre-install everything the night before |
| NextAuth config bugs | 10 min | Use a NextAuth boilerplate template |
| Sortable columns scope creep | 15 min | Decide "cut list" before building |
| Prisma connection exhaustion | 15 min | Add singleton pattern in hour 1 |
| bcrypt on Vercel | 15 min | Use bcryptjs from the start |
| Local → cloud DB migration | 20 min | Use Supabase from hour 0 |
| Google OAuth not configured | 10 min | Only show features that actually work |

**Total time lost to preventable issues:** ~97 minutes

If we'd prepped the night before (install deps, use cloud DB, use boilerplate auth), we could've built 1.5x more features in the same 6 hours.

---

## The Golden Rules We Learned

1. **Deploy by hour 4, not hour 5.** Give yourself buffer for deployment surprises.
2. **Use cloud databases from the start.** Local → cloud migration under time pressure is a nightmare.
3. **Cut scope aggressively at hour 3.** If a feature isn't built by hour 3, it's not making the demo.
4. **Rehearse the demo at least 3 times.** The pitch matters more than the code.
5. **Commit every hour.** Those save points saved us twice when we broke things.
