# Example Team Plan: 4-Person Team at a 24-Hour Hackathon

**Team Name:** Debug Dynasty
**Hackathon:** 24-hour university hackathon (Saturday 9 AM – Sunday 9 AM)
**Project:** TrackIntern — internship application tracker
**Stack:** Next.js, Tailwind CSS, Prisma, PostgreSQL, Vercel

---

## Team Roles & Assignments

| Person | Role | Responsibilities | Skills |
|--------|------|-----------------|--------|
| **Alex** | Tech Lead / Backend | Architecture decisions, API routes, database schema, deployment | React, Node.js, PostgreSQL |
| **Jordan** | Frontend Dev | UI components, styling, responsive design, animations | Tailwind CSS, Figma, CSS |
| **Sam** | Full-Stack / Integration | Auth system, connect frontend to backend, testing, bug fixes | Next.js, API integration |
| **Casey** | Designer / Pitch | UI design, landing page, pitch script, demo rehearsal, documentation | Figma, storytelling, presentation |

**Why these assignments:** Alex knows databases best, so schema and API ownership makes sense. Jordan is a visual thinker — give them the UI and let them make it beautiful. Sam is the glue person who connects things and fixes what breaks. Casey is the communicator — they'll make the project look and sound good.

---

## Communication Schedule

**Primary channel:** Discord server with text channels:
- `#general` — casual chat, memes, hype
- `#dev` — technical discussions, PR reviews, "help I broke something"
- `#design` — mockups, color choices, layout decisions
- `#standup` — hourly check-ins (posted, not called)

**Rules:**
1. Post in `#standup` every hour on the hour with: what you did, what you're doing next, any blockers
2. If you're stuck for more than 15 minutes, post in `#dev` — the team solves it together
3. No side conversations about technical decisions — everything in `#dev` so there's a record
4. Camera on during work sessions (Zoom in background) — it keeps everyone accountable

**Why hourly standups:** In a 24-hour hackathon, things go wrong fast. A 15-minute miscommunication at hour 4 becomes a 2-hour rework at hour 10. Hourly check-ins catch problems early.

---

## Work Sessions & Break Rotation

The hackathon runs 24 hours, but humans don't. Here's how we structured sleep and breaks:

### Session 1: Kickoff (9 AM – 1 PM) — 4 hours
- 9:00–9:30: Team huddle. Brainstorm ideas. Vote on project (TrackIntern wins 3-1).
- 9:30–10:00: Setup. Alex creates repo, Prisma schema, database. Casey starts Figma mockups. Jordan and Sam install dependencies.
- 10:00–12:00: Core build. Alex builds API routes. Jordan builds landing page. Sam sets up auth. Casey designs dashboard mockup.
- 12:00–12:30: **Lunch break.** All four step away from screens. Eat actual food (not chips).
- 12:30–1:00: Integration check. Sam connects frontend to API. First end-to-end flow works.

**Break rotation:** Nobody took individual breaks during the 3-hour work blocks. We kept momentum. Lunch was the collective reset.

### Session 2: Deep Build (1 PM – 7 PM) — 6 hours
- 1:00–3:00: Dashboard UI. Jordan builds stats cards and table. Alex adds delete/update endpoints. Sam handles form page.
- 3:00–3:30: **Afternoon break.** Walk outside for 15 minutes. Fresh air resets your brain.
- 3:30–5:00: Polish pass. Color-coded badges, responsive design, toast notifications. Casey reviews every page and flags UX issues.
- 5:00–6:00: **Dinner break.** Away from screens. We talked about non-hackathon things. Needed the mental reset.
- 6:00–7:00: Pre-deploy check. Test all flows. Fix bugs. Alex starts Vercel deployment.

**Energy management:** Afternoon is the danger zone. Post-lunch sleepiness hits hard. The 3:30 walk outside saved us — everyone came back energized.

### Session 3: Deploy & Polish (7 PM – 11 PM) — 4 hours
- 7:00–8:00: Deployment. Vercel setup, env vars, build fixes (bcrypt error — switched to bcryptjs).
- 8:00–9:00: Performance optimization. Lighthouse score goes from 72 to 96.
- 9:00–9:30: **Evening break.** Snacks, coffee, quick stretch.
- 9:30–10:30: Casey writes pitch script. First draft is too technical — rewritten to focus on the problem.
- 10:30–11:00: **Demo rehearsal #1.** Crashes — Google OAuth button doesn't work. Remove it. Rehearsal #2 goes smoothly.

**Break rotation:** Evening breaks are optional but recommended. We took a 30-minute break at 9 PM and it was the best decision of the day.

### Session 4: Overnight (11 PM – 5 AM) — 6 hours
- 11:00 PM: **Sleep rotation begins.**
  - Alex and Casey sleep 11 PM – 3 AM (4 hours)
  - Jordan and Sam stay awake for "night watch" — fix bugs, polish UI, write documentation
  - 3 AM: Swap. Alex and Casey wake up. Jordan and Sam sleep 3 AM – 7 AM (4 hours)
- 3:00–5:00: Night watch pair (Alex + Casey) does final bug fixes and README updates.
- 5:00 AM: **Everyone sleeps.** Alarm set for 7 AM. 2 hours of real sleep.

**Why sleep at all:** We tried an all-nighter at a previous hackathon. By hour 20, we were making mistakes that took longer to fix than the time we "saved" by not sleeping. Four hours of sleep per person is the minimum for functioning code.

**Overnight bugs caught:**
- 11:30 PM: Prisma client connection exhaustion. Jordan added singleton pattern. (Sam would've caught this in the morning — good thing Jordan was awake.)
- 1:00 AM: Supabase database paused due to inactivity. Casey restored it from the dashboard. (This would've been a morning-of crisis without overnight watch.)

### Session 5: Final Push (7 AM – 9 AM) — 2 hours
- 7:00–7:30: Everyone wakes up. Coffee. Quick status check — what's done, what's broken.
- 7:30–8:00: **Demo rehearsal #3.** Timed: 58 seconds. Perfect. Practice Q&A responses.
- 8:00–8:30: Final polish. Clean up console.logs. Update README. Push final commit.
- 8:30–9:00: **Submission.** Upload to hackathon platform. Deep breath. We're done.

---

## The Conflict (And How We Resolved It)

**Hour 3 (12:00 PM):** Jordan and Alex disagreed on the dashboard layout.

Jordan wanted a card-based layout with large status indicators and visual flair. Alex wanted a dense table layout that showed more data. Both felt strongly.

**What happened:**
1. Jordan posted mockups in `#design` — card layout with colorful status circles
2. Alex responded in `#dev` — "tables are more functional, cards waste space"
3. Jordan replied — "cards look better in a demo, judges scan visually"
4. Sam jumped in — "what if we do both? Stats cards on top, table below"

**Resolution:** Sam's compromise. Stats cards at the top for visual impact (Jordan's preference), table below for data density (Alex's preference). Both got what they wanted. The combo actually looked better than either option alone.

**Time lost:** 20 minutes of debate + 15 minutes implementing the compromise = 35 minutes total.

**Lesson learned:** Settle design disagreements fast with a "yes, and" approach. Sam's intervention was key — sometimes the best team member is the one who bridges two strong opinions.

---

## What Worked Well

1. **Hourly standups caught issues early.** At hour 6, Sam mentioned the auth redirect was broken. Alex fixed it in 5 minutes. Without standups, that would've been discovered at hour 10 during integration.

2. **Sleep rotation was essential.** Jordan and Sam's overnight session caught two critical bugs. Alex and Casey's 3 AM session cleaned up the codebase. Everyone got at least 4 hours of real sleep.

3. **Casey's design review at hour 5** caught 8 UX issues that the developers missed (unclear button labels, inconsistent spacing, missing hover states). A dedicated "reviewer" role pays off.

4. **The 35-minute design conflict** actually improved the final product. The stats cards + table combo became one of the judges' favorite features.

---

## What We'd Do Differently

1. **Pre-setup on Friday night.** We wasted 30 minutes on Saturday morning installing dependencies and creating the repo. Do this the night before.

2. **Cloud database from hour 0.** We used local Postgres and had to migrate to Supabase at hour 5. That 20-minute scramble was avoidable.

3. **More sleep.** The 5 AM – 7 AM block (2 hours for everyone) wasn't enough. By the final demo, Sam was functioning on caffeine and adrenaline. Next time: schedule a full 6-hour sleep block per person.

4. **Assign a "scope cop."** We built a reminder feature that we cut from the demo because it wasn't polished. Someone should've flagged earlier: "this won't make the demo, cut it now."

---

## Post-Hackathon Retrospective

We did a 30-minute retrospective the following Monday. Here's what each person said:

**Alex (Tech Lead):** "I should've delegated more. I spent 2 hours on API routes that Sam could've handled. I should've focused on architecture and deployment."

**Jordan (Frontend):** "I got tunnel vision on the UI. I should've checked in with Casey more often — she caught 8 issues in 10 minutes that I'd been staring at for 2 hours."

**Sam (Full-Stack):** "I was the glue but I didn't have clear ownership. Next time, give me a specific feature to own, not just 'connect things.'"

**Casey (Designer/Pitch):** "I felt useless during hours 2-4 when everyone was coding. I should've started the pitch script earlier and done more user research."

**Key takeaway:** Every role needs clear ownership AND clear downtime. Casey's "useless" feeling during the coding phase could've been avoided by scheduling user research or competitor analysis during that time.

---

## Team Plan Template (Copy This)

```
TEAM: [Name]
HACKATHON: [Name] ([Duration])
PROJECT: [One-line description]

ROLES:
- Person 1: [Role] — [Top 3 responsibilities]
- Person 2: [Role] — [Top 3 responsibilities]
- Person 3: [Role] — [Top 3 responsibilities]
- Person 4: [Role] — [Top 3 responsibilities]

COMMUNICATION:
- Primary channel: [Discord/Slack/etc.]
- Standup schedule: [Frequency]
- Escalation rule: [When to ask for help]

SCHEDULE:
- Session 1: [Time] — [Focus area]
- Break: [Time]
- Session 2: [Time] — [Focus area]
- ...
- Sleep rotation: [Who sleeps when]

CONFLICT RESOLUTION:
- Design disputes: [Process]
- Technical disagreements: [Process]
- Scope changes: [Who decides]

CHECKLIST (before hackathon):
□ Repo created
□ Dependencies installed locally
□ Cloud database provisioned
□ Figma file set up
□ Pitch outline drafted
□ Sleep schedule agreed upon
```
