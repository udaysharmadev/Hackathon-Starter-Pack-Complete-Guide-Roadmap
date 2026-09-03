# Section 24: Non-Coder Guide

Let's get one thing straight: you don't need to write code to be essential at a
hackathon. In fact, some of the winning teams have members who never touch the
codebase. If you can think clearly, communicate well, and bring structure to chaos,
you're exactly the kind of person teams need.

---

## 1. Why Non-Coders Are Valuable at Hackathons

There's a myth that hackathons are only for programmers. It's wrong. The teams
that consistently win aren't just the ones with the best coders — they're the ones
with the best product thinking, design, and storytelling.

**The Numbers Don't Lie:**
Studies of hackathon winners consistently show that winning teams have diverse
skill sets. A team of four backend developers will build something technically
impressive but often fails because nobody thought about the user experience,
the problem validation, or the pitch.

**What Non-Coders Bring:**
- **Perspective.** Coders get tunnel vision on implementation. Non-coders keep
  the team focused on the problem and the user.
- **Structure.** Someone needs to decide what gets built, in what order, and when
  to stop. That's product management.
- **Communication.** The best project loses if you can't explain why it matters.
  That's what pitch leads and content creators do.
- **Validation.** Before you build anything, someone should verify the problem
  actually exists. That's research.

The real competitive advantage: when every team has developers, the teams that
stand out are the ones that also have someone dedicated to making the product
make sense, look good, and tell a compelling story.

---

## 2. Researcher Role

If you love digging into problems and asking questions, this is your role.
Researchers make sure the team is solving a real problem — not just building
something cool for the sake of it.

**Problem Validation — Ask Before You Build:**
- Does this problem actually exist? How do we know?
- Who experiences this? How many people?
- How do they solve it right now? What's wrong with current solutions?
- Would people actually pay for or use our solution?

**Market Research (First Hour of the Hackathon):**
- Search for existing solutions. If five products already do this, you need a
  clear differentiator.
- Look at app store reviews of competitors. People tell you what's broken.
- Check Reddit, Twitter, and forums for complaints about the problem space
- Find statistics that back up the problem's significance

**Competitor Analysis:**
Create a quick comparison table of 3-4 competitors. For each, note their core
feature, pricing, platforms, and key gap. This takes 30 minutes and gives your
team crucial context about where to position your solution.

**User Interviews:**
If the hackathon is in person, walk around and ask people:
- "Do you ever experience [problem]? How do you deal with it?"
- "Would you pay for a solution that did X?"
- "What's the most frustrating part of Y?"
Even 5-10 conversations give you real data.

---

## 3. Product Manager Role

The PM role at a hackathon is about keeping the team focused and shipping.
Without someone playing this role, teams build everything and nothing at the same time.

**Feature Prioritization:**
Ask three questions about each feature:
1. Does this help us win the demo? If no, cut it.
2. Can we build this in the time we have? If no, simplify it.
3. Does this solve the core problem? If no, why are we building it?

Put features in a 2x2 matrix: impact (high/low) vs. effort (high/low).
Build high-impact, low-effort first. Skip low-impact, high-effort entirely.

**Scope Management:**
Your job is to say "no." Every time someone says "what if we also..." your
response should be: "Will this make the demo better or just different?" and
"Can we do this in the next 2 hours?" Write the scope on a whiteboard and
make the team commit to it.

**User Stories:**
Write simple stories to keep everyone aligned:
- "As a busy parent, I want to schedule meals in 2 minutes so that I don't
  spend time planning every week"
- "As a student, I want to track my study sessions so I can see where my time goes"

**Acceptance Criteria:**
For each feature, define what "done" looks like:
- User can log in with Google OAuth → Success
- User can create a project → Must save to database and appear in list
This prevents arguments about whether something is "finished."

---

## 4. Designer Role

Design at a hackathon isn't about creating a polished product — it's about
making sure the judges can understand and appreciate what your team built.
A few well-designed screens make a massive difference.

**Wireframes:**
Before anyone starts coding, sketch the key screens: landing page, core flow
(3-4 screens showing the main feature), dashboard, and error states. Paper
wireframes are fine. Just get the layout clear so developers know what to build.

**UI Design:**
- Pick a color palette (2-3 colors max). Use Coolors or Color Hunt.
- Choose typography (2 fonts max — one for headings, one for body)
- Design the 4-5 most important screens in Figma
- Use free icon libraries: Lucide, Heroicons, or Phosphor

**User Flow:**
Map the user's journey: landing → core action → result → share. If any step
is confusing, redesign it. Judges follow this flow during your demo, and
confusion kills presentations.

**Branding:**
Create a simple identity: a memorable name, a tagline (one sentence explaining
what it does), consistent colors across all screens. Don't spend more than 30
minutes on a logo.

**Presentation Design:**
This is arguably more important than the app design. Create 8-10 slides:
problem slide with a relatable scenario, solution slide showing the app,
demo slide with live or recorded demo, and team slide. Keep text minimal —
one key point per slide.

---

## 5. Pitch Lead Role

The pitch can make or break your hackathon. You could have the best project
in the room, but if you can't explain why it matters, judges won't care.

**Storytelling Structure:**
1. **Hook (15s):** Start with a relatable problem. "Raise your hand if you've
   ever spent 20 minutes trying to find parking."
2. **Problem (30s):** Make the audience feel the pain. Use specific numbers.
3. **Solution (30s):** Show how your product solves the problem. Keep it simple.
4. **Demo (2-3 min):** Show the product working. Narrate what's happening.
5. **Impact (30s):** How many people does this help? What's the potential?
6. **Closing (15s):** Restate the name, tagline, and team.

Total time: 4-5 minutes. Practice it until it fits.

**Demo Scripting:**
Write a flow script (not word-for-word):
- "First, I'll show you [feature]. Watch what happens when I..."
- "Notice how [benefit]. This is different from [competitor] because..."
Practice the demo 5 times. Have a backup video in case the live demo fails.

**Public Speaking Tips:**
- Speak slowly — you talk faster when nervous
- Make eye contact with judges, not the screen
- Stand up straight. Don't lean on the table.
- If you mess up, keep going. Nobody notices unless you point it out.
- If a judge asks something you can't answer, say "Great question — that's
  something we'd explore next" instead of guessing.

---

## 6. QA/Tester Role

Every team needs someone whose job is to break things. If nobody tests before
the demo, something will fail in front of the judges. That's where you come in.

**Testing Approach:**
- **Happy path:** Does the basic flow work? Can a user complete the main action?
- **Edge cases:** Empty inputs? Very long text? Special characters?
- **Error handling:** Slow server? Missing required fields? Wrong button order?
- **Browser testing:** Chrome, Firefox, Safari, mobile?
- **Accessibility basics:** Tab navigation? Alt texts? Contrast readable?

**Bug Reporting Template:**
- **Title:** What went wrong in one line
- **Steps to reproduce:** Numbered list of exactly what you did
- **Expected vs. Actual:** What should have happened vs. what did
- **Severity:** Critical (demo will fail), Major (noticeable but workaround), or Minor

**Edge Cases to Test:**
Submit a form with every field empty. Try extremely long text (500+ characters).
Upload unsupported files. Click buttons rapidly. Resize the browser. Use the
browser back button during a flow. Open in two tabs simultaneously.

**Demo Data Creation:**
Create realistic data that makes the demo look good — realistic names (not "test"),
a mix of record sizes, a few impressive-looking entries, and data that tells a
story during the presentation. Pre-load everything so judges see a populated app.

---

## 7. Content Creator Role

Content creators document the journey and make sure your project gets visibility
beyond the judging room. This role is especially valuable for "Best Social Media"
or "Community Choice" prize categories.

**Documentation:**
Throughout the hackathon, keep a log of decisions, screenshots of progress,
key challenges, and memorable moments. This becomes your blog post, presentation
backup, and portfolio content.

**Social Media:**
Post updates every few hours: a team photo at the start, progress sneak peeks,
behind-the-scenes moments, and a final post about what you built. Tag the
hackathon organizers, sponsors, and use the event hashtag. Judges notice this.

**Blog Post:**
After the hackathon, write about the problem, your approach, challenges,
lessons learned, and what you'd do differently. Include screenshots. Publish
on Medium, Dev.to, or your personal blog.

**Demo Video:**
Record a 2-3 minute walkthrough: problem and solution in 30 seconds, main
features with narration, impact and team credits. No background music, no
flashy effects. Upload to YouTube and link in your submission.

---

## 8. "How to Contribute Without Writing Code"

20 specific tasks you can do right now at a hackathon:

1. Validate the problem idea — talk to 5 people and confirm it's real
2. Research competitors — find 3 existing solutions and document weaknesses
3. Create user personas — who is this for? What do they need?
4. Write user stories — "As a X, I want to Y so that Z"
5. Prioritize features — build a roadmap of what to build first
6. Design wireframes — sketch every screen on paper or in Figma
7. Create the visual design — colors, fonts, components in Figma
8. Design the logo and branding — name, tagline, visual identity
9. Build the slide deck — structure the story and design the presentation
10. Write the demo script — plan exactly what you'll show and say
11. Create test data — realistic entries that make the app look populated
12. Test the app — find bugs before the judges do
13. Write documentation — setup instructions, API docs, README
14. Record a demo video — backup in case live demo fails
15. Manage the project board — track what's done, what's in progress
16. Handle food logistics — order food, keep the team fed and hydrated
17. Coordinate with other teams — learn what others are building
18. Write social media posts — document the journey
19. Prepare for Q&A — anticipate judge questions and prep answers
20. Be the timekeeper — make sure the team doesn't miss deadlines

---

## 9. Communication Tips

Working with developers requires a different kind of communication.

**Do:**
- "Can you explain what's blocking you? Maybe I can help think through it."
- "What's the simplest version of this feature we could ship?"
- "The user flow feels confusing at step 3 — can we talk about it?"

**Don't:**
- "Just make it work" — be specific about what "work" means
- "Can you just add a simple button?" — if it were simple, they'd have done it
- "The other team has this, why don't we?" — comparisons kill morale

**Understanding Technical Constraints:**
You don't need to code, but knowing these helps: API rate limits, data storage
complexity, authentication time, third-party setup requirements, and browser
compatibility. When a developer says "that'll take too long," ask what the
simpler alternative is.

**When to Push Back:**
Developers sometimes over-engineer. Gently redirect: "Do we need a perfect
database schema, or can we use a simpler approach for the demo?" and "The demo
is in 4 hours — can we cut scope and focus on the core?"

**When to Back Off:**
If a developer is deep in concentration, don't interrupt. Leave a note or send
a message. If they say "give me 30 minutes," set a timer and come back. Respecting
focus time is one of the most valuable things a non-coder can do.

---

## 10. Portfolio Building

Your hackathon experience is portfolio gold. Here's how to showcase it.

**For Your Resume:**
Add hackathon projects with project name, your role, one-line description, your
specific contributions (not the team's), and technologies used.

Example:
> **MealMatch** — Product Manager & Designer
> AI-powered meal planning app. Led product strategy, designed UI in Figma,
> created pitch deck. Won 2nd place at [Hackathon Name] 2026.

**For LinkedIn:**
Post about the experience with photos, write a short post about what you learned,
tag teammates and organizers, and add the project to your "Featured" section.

**For Your Portfolio Website:**
Create a case study: problem, process (your role), outcome (what you built), and
lessons learned. Include screenshots, wireframes, and slide decks.

**Showcasing Non-Technical Skills:**
Don't try to look technical. Highlight universally valuable skills:
- **Product thinking:** "Identified a real user problem and designed a solution"
- **Leadership:** "Coordinated a team, managed scope, delivered in 36 hours"
- **Communication:** "Created and delivered a pitch that won judges' attention"
- **Design:** "Designed complete UI/UX including user flow and final mockups"
- **Quality assurance:** "Found and documented 15+ bugs before the demo"

**Building Over Time:**
After 3-4 hackathons, you'll have multiple case studies, evidence of working
with different teams, a track record of shipping under pressure, interview
stories, and a network of collaborators.

---

## Quick Reference: Non-Coder Checklist

**Before:**
- [ ] Research the theme and potential problem areas
- [ ] Set up Figma (free account works)
- [ ] Prepare a simple slide template
- [ ] Pack a notebook and pen for sketching

**During:**
- [ ] Validate the problem before building
- [ ] Create wireframes before coding starts
- [ ] Design key screens in Figma
- [ ] Build the slide deck alongside development
- [ ] Test the app throughout, not just at the end
- [ ] Document the journey on social media

**After:**
- [ ] Update your resume and LinkedIn
- [ ] Write a case study for your portfolio
- [ ] Connect with your teammates
- [ ] Reflect on what you learned

---

## Final Thought

The best hackathon teams aren't all coders. They're balanced teams where each
person brings something different. Your ability to think about users, organize
the work, design the experience, and tell the story is just as important as
the code that powers it. Don't let anyone tell you otherwise.
