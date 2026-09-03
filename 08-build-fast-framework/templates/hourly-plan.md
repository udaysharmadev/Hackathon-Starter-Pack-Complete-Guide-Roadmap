# Hourly Build Plan — Three Variants for Any Hackathon Duration

Pick the plan that matches your hackathon length. Each hour has a specific deliverable and a checkpoint question to tell you if you're on track.

---

## The 6-Hour Sprint (Single-Track)

For short hackathons or solo builders.

### Hour 0–1: Scope and Scaffold

**Deliverable:** Project repo, dependencies installed, one page rendering.

**What to do:**
- Pick your stack (keep it simple: Next.js + Supabase covers 90% of cases)
- `npx create-next-app@latest` or equivalent
- Set up Supabase / Firebase / your database
- Create a README with your one-liner pitch
- Push to GitHub

**Checkpoint:** Can you run `npm run dev` and see a blank page? If no, stop everything and fix it.

**If behind:** Skip the repo setup. Use a online editor (StackBlitz, CodeSandbox) and deploy later.

### Hour 1–2: Core Feature MVP

**Deliverable:** The one thing your app does, working end-to-end.

**What to do:**
- Build the ONE core action (e.g., "user submits a form and sees a result")
- Wire up your main API call
- Get data flowing front-to-back
- Skip auth, skip polish, skip edge cases

**Checkpoint:** Can a stranger use the core feature with zero instructions? If yes, you're golden.

**If behind:** Cut scope. What's the simplest version that still demonstrates the idea? Build that.

### Hour 2–3: Second Feature + Auth

**Deliverable:** Auth working, second feature rough but functional.

**What to do:**
- Add auth (Clerk/Supabase Auth — 15 minutes)
- Build your second feature
- Connect it to the first (data should flow between them)

**Checkpoint:** Can a logged-in user do two things in your app?

**If behind:** Skip the second feature. Make the first feature amazing instead.

### Hour 3–4: Connect and Complete

**Deliverable:** Full user flow from start to finish.

**What to do:**
- Wire up all features into a single user journey
- Fix obvious bugs
- Add basic error handling (loading states, error messages)

**Checkpoint:** Can you demo the full flow without saying "and then it would..."

**If behind:** Cut features until you can. A working 2-feature app beats a broken 5-feature app.

### Hour 4–5: Polish

**Deliverable:** Looks professional. Feels complete.

**What to do:**
- Clean up spacing, colors, typography
- Add a favicon and page title
- Fix mobile layout
- Write your demo script

**Checkpoint:** Take a screenshot. Does it look like a real product?

**If behind:** Just fix the landing page. First impressions matter most.

### Hour 5–6: Deploy and Rehearse

**Deliverable:** Live URL. Two practice runs.

**What to do:**
- Deploy to Vercel/Render/Firebase Hosting
- Test the live URL on a phone
- Practice your 2-minute demo twice
- Record a backup video in case of Wi-Fi failure

**Checkpoint:** Can someone else use your live app on their phone right now?

**If behind:** Deploy immediately, even if ugly. A working ugly app beats a polished localhost.

---

## The 12-Hour Build (Parallel Tracks)

For overnight or all-day hackathons. Teams of 2–3.

### Track A: Frontend (Person 1)

| Hour | Deliverable |
|---|---|
| 0–1 | Project setup, UI framework, design tokens |
| 1–2 | Landing page + layout components |
| 2–3 | Core feature UI (forms, displays) |
| 3–4 | Second feature UI |
| 4–5 | Auth pages (login, signup, dashboard) |
| 5–6 | Mobile responsive pass |
| 6–7 | Loading/error/empty states |
| 7–8 | Polish: animations, transitions, micro-interactions |
| 8–9 | Screenshot-worthy hero section |
| 9–10 | Final spacing and typography pass |
| 10–11 | Help backend with integration |
| 11–12 | Deploy prep, demo recording |

### Track B: Backend (Person 2)

| Hour | Deliverable |
|---|---|
| 0–1 | Project setup, database schema, API routes |
| 1–2 | Auth endpoint (signup, login, session) |
| 2–3 | Core feature API (CRUD) |
| 3–4 | Second feature API |
| 4–5 | Third feature API (if needed) |
| 5–6 | Error handling, input validation |
| 6–7 | Seed data for demo |
| 7–8 | API docs / integration contract with frontend |
| 8–9 | Performance: caching, query optimization |
| 9–10 | Webhook integrations |
| 10–11 | Integrate with frontend |
| 11–12 | Deploy, env vars, DNS |

### Track C: AI/Integration (Person 3, if available)

| Hour | Deliverable |
|---|---|
| 0–1 | API key setup, API testing |
| 1–2 | First AI/external API integration |
| 2–3 | Second API integration |
| 3–4 | Data pipeline / processing logic |
| 4–5 | Edge cases and retry logic |
| 5–6 | Prompt engineering / fine-tuning |
| 6–7 | Test with realistic data |
| 7–8 | Error boundaries for API failures |
| 8–9 | Cost/rate-limit monitoring |
| 9–10 | Documentation |
| 10–11 | Help integrate with main app |
| 11–12 | Backup plan if API fails during demo |

### Parallel Sync Points

- **Hour 4:** All tracks check in. What's working? What's not? Re-scope if needed.
- **Hour 8:** Integration checkpoint. Can the pieces talk to each other?
- **Hour 10:** Full integration test. Run the entire demo flow.
- **Hour 11:** Deploy and test live.
- **Hour 12:** Demo practice.

---

## The 24-Hour Marathon (Full Build)

For 24-hour hackathons. Teams of 3–5. This is a production-grade build.

### Phase 1: Foundation (Hours 0–4)

| Hour | Frontend | Backend | Design/Research |
|---|---|---|---|
| 0–1 | Repo, framework, component library | DB schema, API framework | Pitch deck, user flow diagram |
| 1–2 | Layout, nav, routing | Auth endpoints | Wireframes for main screens |
| 2–3 | Landing page | Core CRUD APIs | Color palette, typography |
| 3–4 | Core feature UI | Database seeding | Copy and content |

### Phase 2: Build (Hours 4–12)

| Hour | Frontend | Backend | AI/Integration |
|---|---|---|---|
| 4–5 | Auth UI (login, signup) | File upload endpoint | First API integration |
| 5–6 | Dashboard | Search/filter API | Second API integration |
| 6–7 | Feature 2 UI | Real-time endpoint | Data processing |
| 7–8 | Feature 3 UI | Webhook handlers | Prompt engineering |
| 8–9 | Settings/profile page | Rate limiting | Error handling |
| 9–10 | Mobile responsive | Logging/monitoring | Test with real data |
| 10–11 | Error states | API documentation | Fallback strategies |
| 11–12 | Integration test | Integration test | Integration test |

### Phase 3: Polish (Hours 12–20)

| Hour | Focus |
|---|---|
| 12–13 | Fix all blocking bugs |
| 13–14 | Loading states, animations |
| 14–15 | Accessibility pass (keyboard nav, screen reader) |
| 15–16 | Performance optimization |
| 16–17 | Security review (auth checks, input validation) |
| 17–18 | Mobile/tablet responsive fine-tuning |
| 18–19 | Empty states, onboarding flow |
| 19–20 | Final UI polish (shadows, border-radius, spacing) |

### Phase 4: Ship (Hours 20–24)

| Hour | Deliverable |
|---|---|
| 20–21 | Deploy to production |
| 21–22 | Full end-to-end test on live |
| 22–23 | Demo script, practice runs |
| 23–24 | Buffer for disasters. Backup video. Submit. |

### Team Sync Schedule (24h)

- **Every 4 hours:** 10-minute standup. What's done? What's blocked?
- **Hour 12:** Midpoint review. Cut scope if behind.
- **Hour 20:** Code freeze. No new features.
- **Hour 22:** Final integration test on live URL.
- **Hour 23:** Submit. Breathe.

---

## Energy Management Tips

- **Hours 0–2:** Peak focus. Do your hardest logic here.
- **Hours 2–6:** Momentum phase. Build fast, don't overthink.
- **Hours 6–10:** Danger zone. Fatigue hits. Drink water, eat protein, take a 10-min walk.
- **Hours 10–14:** Second wind. Fresh perspective on bugs you couldn't solve earlier.
- **Hours 14–20:** Grind phase. Do boring but necessary work (polish, responsive, states).
- **Hours 20–24:** Adrenaline. You'll run on stress. Don't add new features. Just ship.

## Emergency Scope Cuts (Ranked by Pain)

If you're behind, cut in this order:

1. **Cut first:** Analytics, admin panel, user settings page
2. **Cut second:** Third-party integrations beyond one
3. **Cut third:** Complex animations, dark mode
4. **Cut fourth:** Mobile responsive (desktop-first is fine for demo)
5. **Cut last:** Auth, core feature, basic error handling

**Never cut:** A working demo, even if it's simple. Judges remember what works, not what was planned.
