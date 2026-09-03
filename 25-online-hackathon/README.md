# Section 25: Online Hackathon

Online hackathons have exploded in popularity. You can participate from your couch,
your dorm room, or a coffee shop in another country. But remote hackathons come with
their own set of challenges that most people don't anticipate. This section covers
everything you need to thrive in a virtual hackathon environment.

---

## 1. Online vs In-Person Hackathons

The format changes everything. What works in person doesn't always translate online.

**Communication:**
In person, you tap a teammate on the shoulder. Online, you message and wait. You
can't read body language, overhear conversations, or "vibe check" the team's energy.

**Environment:**
In person, the venue provides structure — tables, power, food, focus. At home, your
bed is ten feet away, your phone is buzzing, and nobody's watching if you disappear.

**Energy:**
In-person hackathons have contagious energy. Other teams are working around you, the
clock is ticking. Online, you have to create that energy yourself.

**Advantages of Online:**
- No travel costs or time. Participate from anywhere.
- Your own setup — monitors, chair, food
- More flexible schedule (sleep in your own bed)
- Lower barrier to entry for first-timers

**Challenges of Online:**
- Distractions are everywhere
- Harder to build team chemistry
- Time zone coordination for international teams
- Less accountability — easy to ghost your team
- Demo logistics are more complex

---

## 2. Remote Survival Kit

Your workspace makes or breaks your online hackathon experience. Set it up
before the event — not during.

**Workspace Setup:**
- **Dedicated space.** A desk in a quiet room. Not your bed. Not the couch.
- **External monitor.** Splitting code and docs across two screens saves constant
  tab switching. Worth it for any remote work.
- **External keyboard and mouse.** Your laptop keyboard is fine for an hour.
  For 48 hours, your wrists need something better.
- **Lighting.** Make sure your face is visible on camera. A desk lamp or ring light helps.
- **Headphones.** Noise-canceling if you have them. Your family will make noise.

**Tools You Need:**
- **Communication:** Discord or Slack — installed and tested before day one
- **Screen sharing:** Zoom or Google Meet — test quality and audio in advance
- **Code editor:** VS Code with Live Share, or Replit/CodeSandbox
- **Version control:** Git with GitHub — set up SSH keys in advance
- **Design:** Figma (free tier works for hackathons)
- **Notes:** Shared doc in Google Docs or Notion for all decisions

**Notification Management — This Is Critical:**
- Phone in another room or Do Not Disturb mode
- Close personal Slack/Teams/Discord
- Turn off email notifications
- Use focus mode (Focus on Mac, Focus Assist on Windows)
- Tell friends and family you're unavailable for the weekend
- Close all unrelated browser tabs
- Use a website blocker if you need to (Cold Turkey, Freedom)

---

## 3. Async Team Coordination

Online teams can't just turn around and ask a question. You need systems
that work across time and space.

**Communication Protocols (Set Before You Start):**
- Response time expectations: "Respond within 30 minutes during working hours"
- Meeting cadence: 15-minute standup morning and evening. That's it.
- Decision-making: Quick decisions — whoever's available calls it. Architectural — team votes.
- Escalation: "Blocked for 30+ minutes? Post in the main channel."
- Status updates: "Update the shared doc every 2 hours."

**Shared Docs:**
Create one document before the hackathon: project brief, feature list, decision
log, blockers list, demo plan, and all links. Keep it open the entire time.

**Daily Standups (10 minutes max):**
Each person shares: what they completed, what they're working on next, and what's
blocking them. Write updates in the shared doc so anyone who misses it can catch up.

**Branching Strategy:**
Git conflicts kill online hackathons. Prevent them:
- Everyone works on their own feature branch
- Pull from main at least twice daily
- Merge only after someone reviews
- Communicate when touching shared files
- Use descriptive branch names: `feat/user-login`, `fix/header-alignment`

---

## 4. Time Zone Management

If your team spans multiple time zones, this is your biggest challenge.

**Finding Overlapping Hours:**
- Same country: easy. Different countries: find the 4-6 hour overlap and make it sacred.
- During overlap: collaborative work — meetings, code reviews, pair programming.
- During non-overlap: independent work — individual features, documentation, designs.

**Handoff Protocols:**
When one "shift" ends and another begins:
- Write a clear status update in the shared doc
- Push all code to a branch (not main)
- Document incomplete work — where you stopped, what's next
- Leave comments in the code where you left off
- Don't push broken code and disappear

**Scheduling Tools:**
World Time Buddy (compare time zones), Calendly (book slots during your hours),
Google Calendar (shared team calendar with working hours), When2meet (find common
availability quickly).

**Team Agreement:**
Write down: core hours in a specific time zone, response time expectations during
and outside core hours, daily standup time, and demo rehearsal time.

---

## 5. Virtual Demo Tricks

A virtual demo is harder than in-person. You can't rely on the venue's setup,
and technical issues are more likely. Preparation is everything.

**Screen Sharing Tips:**
- Close everything unrelated. Use a clean desktop or dedicated user profile.
- Increase font size. What looks fine on your screen is tiny when shared.
- Use a plain or blurred background.
- Test your resolution — share your screen and check readability.
- Practice transitions between code, browser, and terminal.

**Backup Recordings:**
Record a backup demo video before the live presentation:
- Use QuickTime (Mac) or OBS Studio (any platform)
- Narrate clearly, speak slowly, keep it 3-4 minutes
- Upload to YouTube (unlisted) as backup
- If live demo crashes, play the video instead

**Bandwidth Management:**
- Close unnecessary apps and tabs during the demo
- Use wired ethernet instead of WiFi if possible
- Turn off audience video if the platform allows it
- Have a phone hotspot ready as backup internet
- Test upload speed — need at least 5 Mbps for smooth screen share

**Dealing with Issues During the Demo:**
Stay calm. Have a backup ready (pre-recorded video, screenshots, different browser).
Acknowledge briefly: "Looks like a connectivity issue — let me show you a recording."
Don't spend more than 30 seconds trying to fix something live.

---

## 6. Staying Motivated Alone

At in-person hackathons, the energy of other teams keeps you going. At home,
you have to manufacture your own motivation.

**Accountability Systems:**
- Daily check-ins: 10-minute standup every morning keeps everyone honest
- Pair programming: work on a call with a teammate, screen share and code together
- Public commitment: tell your team what you'll complete by the next check-in
- Progress tracking: check things off a task list. Seeing progress motivates.

**Progress Tracking:**
Each morning write: today's goal (one thing), 3-5 small tasks, and at end of day,
a "done list." This creates momentum and gives you something to share at standups.

**Reward Systems:**
- "Finish this feature → 20-minute walk outside"
- "After standup → favorite snack"
- "Demo ready → watch an episode"
- "Win → team takeout celebration"

**Pomodoro Technique:**
Work in focused sprints: pick one task, set timer for 25 minutes, work with zero
distractions. When timer rings, 5-minute break. After 4 cycles, 15-30 minute break.
Prevents burnout and keeps focus sharp all day.

---

## 7. Online Collaboration Tools

These tools make remote collaboration feel almost as smooth as being in the same room.

**Figma (Design Collaboration):**
Multiple people design simultaneously. Create a shared team library for consistent
components. Use FigJam for brainstorming. Export assets directly for your app.

**CodeSandbox / Replit (Cloud IDEs):**
Code in the browser — no local setup. Share your environment with a link. Built-in
terminal, package manager, and debugging. Replit supports real-time collaboration.

**Gitpod / GitHub Codespaces (Cloud Dev Environments):**
Full VS Code in the browser. Pre-configured environments that match your project.
Spin up in seconds. Great for teams where everyone needs the same setup.

**VS Code Live Share (Pair Programming):**
Share your editor with teammates in real time. They can edit code, run commands,
and debug alongside you. No project setup needed on their machine.

**Discord / Slack (Communication):**
Create channels: #general, #code, #design, #blocked. Use threads for organization.
Pin important decisions. Voice channels for quick discussions instead of typing.

**Notion / Google Docs (Shared Documentation):**
All project docs in one place. Track decisions, action items, blockers. Everyone
edits simultaneously. Create a "quick links" page with all repos and resources.

---

## 8. "The Loneliness Factor"

This is the thing nobody talks about. Online hackathons can be genuinely lonely.
You're sitting alone in your room, working on code, while teammates are silently
typing in their own rooms. The social connection that makes hackathons fun is
harder to build remotely.

**Combating Isolation:**
- Keep your camera on during calls. Seeing faces helps.
- Use voice channels. Even silently being in a Discord voice call creates presence.
- Start each day with casual chat — 2-3 minutes before standup about how everyone is.
- Share small wins: "Hey, I just got auth working!" keeps energy up.

**Joining Side Channels:**
Most online hackathons have community channels beyond the competition: general chat,
theme-specific discussions, help channels, social channels for memes and off-topic
conversations. Jump in. Talk to people outside your team.

**Virtual Co-Working:**
Set up recurring calls with your team where everyone works simultaneously. It's not
about talking — it's about being "together" while working. Cameras on, work silently,
take breaks together.

**Personal Connection:**
Learn teammates' names, time zones, and something about them. Share photos of your
workspace. Celebrate wins together. If someone is quiet, check in on them. After the
hackathon, stay in touch — these connections lead to future collaborations.

---

## 9. Submission Logistics

You built something amazing. Now submit it properly. This is where many online
hackathon teams fail — not because their project wasn't good, but because they
messed up the submission.

**File Formats:**
- **Code:** GitHub repo link — make sure it's public or has correct permissions
- **Video:** MP4 is safest. Check time limit (usually 3-5 minutes). 1080p ideal.
- **Slides:** PDF is universal. Don't submit PowerPoint files.
- **Documentation:** PDF or markdown in the repo. Follow the template if provided.

**Upload Requirements:**
- Test uploads before submission day — some platforms have file size limits
- Have backup copies of everything
- Upload at least 2 hours before deadline — platforms get slow near deadlines
- Verify your submission: open all links in incognito window

**Deadline Management:**
Online hackathons are ruthlessly strict. No "just 5 more minutes."
- Confirm: is the deadline in your time zone, UTC, or organizer's?
- Set multiple alarms — phone, calendar, team chat
- Submit 1-2 hours before the actual deadline
- Assign one person as the submission buddy — everyone sends final files to them

**Common Submission Mistakes:**
- Pushing code after deadline (judges can't see it)
- Video link is private or requires login
- Forgot to list a team member in the form
- Code repo is private and judges don't have access
- Submitted wrong video version
- Didn't include setup instructions

---

## 10. "Winning Online"

Online hackathon judges face different challenges than in-person judges. They
can't walk around, ask spontaneous questions, or feel your project's energy.
You need to compensate for that.

**What Judges Look For:**
- **Clarity over complexity.** Since they can't ask questions, your demo needs
  to be self-explanatory. If they're confused, they move on.
- **Video quality.** A shaky recording with bad audio screams "we didn't prepare."
  Invest time in making it look and sound professional.
- **Documentation.** In person, you explain verbally. Online, your README, docs,
  and video need to tell the whole story. Write like judges have zero context.

**Demo Video Best Practices:**
- Start with the problem (10-15 seconds). "Have you ever..."
- Show the solution (60-90 seconds). Walk through the app. Narrate clearly.
- Highlight impact (15-20 seconds). Numbers, scale, potential.
- Credit the team (10 seconds). Names and roles.
- Total: 2-3 minutes. Judges watch dozens. Don't waste their time.
- Audio: Use a good mic. Built-in laptop mics sound terrible.
- Pacing: Speak slowly. Pause between sections. Don't rush.

**Standing Out:**
- A great name — catchy and descriptive. Not "HackProject_v2."
- A clear tagline — one sentence explaining what it does.
- Visual polish — well-designed UI and slides show professionalism.
- A story — show the problem, journey, and solution. Not just features.
- Confidence in the README — write like you're explaining to a friend.
- Social proof — include user feedback gathered during the hackathon.

**Post-Submission:**
Share your project on social media with the hackathon hashtag. Write a blog post.
Connect with participants and judges on LinkedIn. Update your portfolio. If you
didn't win, stay engaged with the community — don't disappear.

---

## Quick Reference: Online Hackathon Checklist

**Before:**
- [ ] Set up workspace (desk, monitor, keyboard, headphones)
- [ ] Install and test all required tools
- [ ] Set up notification management
- [ ] Create shared docs and communication channels
- [ ] Test screen sharing and video calls
- [ ] Coordinate time zones with your team
- [ ] Set up development environment
- [ ] Prepare backup internet (phone hotspot)

**During:**
- [ ] Join daily standups
- [ ] Update shared doc regularly
- [ ] Commit code frequently
- [ ] Test as you build
- [ ] Take breaks and stay hydrated
- [ ] Communicate blockers early
- [ ] Start demo video early

**Before Submission:**
- [ ] Verify all links work in incognito mode
- [ ] Check file formats and size limits
- [ ] Test demo end-to-end
- [ ] Submit at least 2 hours before deadline
- [ ] Save copies of everything submitted

---

## Final Thought

Online hackathons remove barriers of geography, cost, and logistics. They let
anyone, anywhere, participate. But they require more discipline, more intentional
communication, and more self-motivation than in-person events. Set up your
environment, build systems with your team, and don't forget to connect with
people — not just code. The best online hackathon experiences are the ones where
you build something great and build relationships that last beyond the weekend.
