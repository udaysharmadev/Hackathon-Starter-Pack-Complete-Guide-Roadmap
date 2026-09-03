# 12. Team Building

Hackathons are won by teams that figure out their dynamics before the clock starts ticking. You can have the best idea in the room, but if your team can't coordinate, someone else with a worse idea and better teamwork will beat you. This section covers everything from picking the right team size to handling the conflicts that inevitably pop up when four people are sleep-deprived and disagreeing about a CSS framework at 3 AM.

---

## Team Size: The Real Tradeoffs

Not all teams are created equal, and the number of people you bring changes your entire strategy.

### 2-Person Teams

**Pros:** Zero coordination overhead. You don't need a meeting to decide anything — just turn around and ask. Decisions happen in seconds. If you trust your partner, this is the most efficient unit in a hackathon.

**Cons:** You have zero redundancy. If one person gets sick, burns out, or has a family emergency, your project is in serious trouble. You also can't split into parallel tracks easily — one person building while the other designs means nobody's handling deployment, backend, or testing.

**Best for:** Pairs who've worked together before, projects with a narrow scope, or teams where both people are full-stack and can cover each other's gaps.

**Strategy:** Pick one person who's stronger on the backend and one who's stronger on the frontend. Don't try to do everything together — divide the work cleanly and merge every few hours. Your demo prep should start by hour 12, not hour 20.

### 3-Person Teams

**Pros:** This is the sweet spot for most hackathons. You get three distinct roles — builder, designer, and pitch lead — without communication overhead spiraling out of control. Three people can cover frontend, backend, and design without anyone stretching too thin.

**Cons:** Decision-making can stall if two people disagree and the third stays neutral. You also need to be intentional about role clarity, because three people is just enough for someone to feel left out if responsibilities aren't explicit.

**Best for:** Most hackathons, especially 24–48 hour events. This is the default recommendation.

**Strategy:** Assign clear owners: one person owns the backend and data layer, one owns the frontend and UI, one owns the pitch and presentation. The integrator role (merging everyone's work) should rotate or fall to whoever finishes their piece first.

### 4-Person Teams

**Pros:** You get a dedicated integrator/deployment person, which is a luxury most teams don't have. You can also split into two parallel tracks — one team on the core feature, one team on the supporting infrastructure.

**Cons:** Communication overhead doubles compared to a 3-person team. Every decision now requires more coordination. If even one person is passive or disengaged, you'll notice the drag. Four people also means more opinions on the demo, the UI, and the pitch.

**Best for:** Complex projects that genuinely need multiple workstreams — like a full-stack app with a data pipeline, or a project that requires both hardware and software.

**Strategy:** Pair up intentionally. Two people on the core feature, two people on infrastructure and polish. Use a shared task board and have 10-minute standups every 2 hours. The integrator should merge constantly, not at the end.

### 5-Person Teams

**Pros:** Maximum coverage. You can have dedicated frontend, backend, design, pitch, and deployment people. For 48+ hour hackathons, this lets you maintain quality even as people get tired.

**Cons:** This is where teams start to fall apart. Five people is a lot of opinions. The coordination cost is real — you'll spend meaningful time just keeping everyone aligned. One person will inevitably feel like they don't have enough to do, and another will feel like they're doing everything.

**Best for:** Large-scope projects, multi-track hackathons, or teams with very experienced members who know how to self-organize.

**Strategy:** Treat it like a startup sprint. Have one person act as project manager (yes, this is a real role at hackathons). Use strict timeboxes for decisions — if a debate isn't resolved in 5 minutes, the PM decides and moves on. Pair programming helps when people feel disconnected from the work.

---

## Communication Tools: What Actually Works

You'll be communicating constantly during a hackathon. Here's how the major tools compare:

| Feature | Discord | Slack | WhatsApp | Notion |
|---|---|---|---|---|
| **Voice chat** | Excellent — always-on channels, screen sharing, low latency | Good — huddles work but less persistent | Poor — calls are clunky for long sessions | None |
| **Text chat** | Good — threads exist but aren't the focus | Excellent — threads, channels, and search are top-tier | Decent — but no threading, hard to search | Good — but not real-time focused |
| **File sharing** | Good — drag and drop, 25MB limit on free | Good — file uploads with search | Okay — files get buried in chat | Excellent — lives in docs |
| **Task tracking** | Bot integrations (Trello, GitHub) | Bot integrations (Asana, Jira) | None native | Excellent — built-in boards |
| **Screen sharing** | Built-in, very easy | Built-in via huddles | Limited | None |
| **Cost** | Free | Free tier is solid | Free | Free for small teams |
| **Best for** | Remote teams who need voice + text | Teams already in Slack ecosystems | Quick in-person coordination | Documentation and planning |

**The honest take:** Most hackathon teams should default to **Discord** if they're remote (voice channels are unbeatable) or **WhatsApp** if they're in person (everyone already has it). Don't spend the first hour of your hackathon setting up Slack integrations you won't use.

---

## Conflict Resolution: When Things Go Sideways

Conflicts at hackathons aren't a matter of *if* — they're a matter of *when*. Here are three realistic scenarios and how to handle them.

### Scenario 1: "I Want to Use React, Not Vue"

Two frontend developers disagree on the framework. One insists on React because they know it. The other wants to try Vue because they think it's better for this project.

**What usually happens:** They argue for 30 minutes, one person gives up resentfully, and the code quality suffers because they're not working with their preferred tool.

**What to do instead:** The rule is simple — use whatever the person who's writing the frontend code is most comfortable with. Speed matters more than framework purity at a hackathon. If both people are writing frontend code, the tiebreaker is whichever one gets a working prototype up first. This isn't the time for learning curves.

**The line to use:** "We're not shipping a framework. We're shipping a product. Use what you know fastest."

### Scenario 2: Someone Disappears for Three Hours

A team member said they'd handle the database setup but hasn't responded in three hours. Nobody knows if they're stuck, asleep, or just browsing Twitter.

**What usually happens:** Everyone assumes the best, then starts to panic, then someone else scrambles to do the work, and the original person comes back confused about why their task was reassigned.

**What to do instead:** Set a standing rule at the start: if you're going to be away from your computer for more than 30 minutes, post a quick message in your team channel. No explanation needed — just "brb, 30 min" is fine. If someone disappears without warning, assign a buddy to text them directly. Always assume technical difficulty before malice.

**The line to use:** "Hey, just checking in — are you stuck on anything? We can help."

### Scenario 3: The "Visionary" Who Keeps Changing the Idea

One team member keeps pivoting the project direction. First it was a chatbot, now it's a dashboard, and they just suggested adding machine learning. The rest of the team is frustrated because nothing gets finished.

**What usually happens:** The team chases every new idea, builds three half-finished features, and presents a confused demo that doesn't solve any one problem well.

**What to do instead:** This person isn't a villain — they're probably genuinely excited and don't realize the damage. The project manager (or whoever's acting as the de facto leader) needs to say: "We're locking the scope right now. We'll write down the MVP on this whiteboard. Anything that isn't on this list gets cut. If we finish everything, we'll add features." Then physically write the scope down where everyone can see it.

**The line to use:** "I love the ambition. Let's get the core thing working first, then we'll have time for extras."

---

## Solo Hackathon Guide

Not every hackathon requires a team. Some people hack alone — and some of the best projects come from solo makers. Here's how to do it effectively.

### Why Hack Alone?

- No coordination overhead — you make every decision instantly
- You set your own pace and break when you want
- You learn more because you touch every part of the project
- Some hackathons specifically reward individual submissions

### The Solo Strategy

**Pick a narrow scope.** You have half the manpower of a 2-person team, so cut your scope in half too. If a team builds a full-stack app, you build the frontend with a mock API. If a team builds an AI pipeline, you build a polished single-feature tool.

**Work in focused blocks.** The Pomodoro technique works exceptionally well for solo hackers. Work for 50 minutes, break for 10. After three cycles, take a longer break. This prevents the burnout that hits solo hackers hardest because there's nobody to chat with or bounce ideas off.

**Use templates and boilerplates aggressively.** You don't have time to set up authentication from scratch, configure CI/CD, or build a design system. Use a starter template for your framework, grab a UI library, and focus your energy on the thing that makes your project unique.

**Record everything.** Take screenshots and short screen recordings every few hours. When you're solo, you won't have a teammate who captured the behind-the-scenes moments. These are gold for your LinkedIn post later.

**Talk to other hackers.** Even though you're working alone, don't isolate yourself. Walk around, ask people what they're building, share your progress. The feedback you get in the middle of a hackathon can save you hours of building the wrong thing.

### The Solo Demo Prep

Since you don't have a pitch lead, you need to practice your demo more than teams do. Run through it at least five times before you present. Time yourself. Record yourself and watch it back. The biggest risk for solo presenters is rushing — there's nobody else on stage to slow you down.

---

## Team Formation Playbook

### In-Person Hackathons

**Before the event:**
- Check the hackathon's Discord or Slack for team-formation channels
- Post your skills and what you're looking for — be specific ("I build backends in Python and Node, looking for a frontend person")
- Don't commit to the first team that asks — talk to 3–4 groups before deciding
- If you know people attending, reach out 2–3 days before to coordinate

**At the event:**
- Attend the opening mixer — this is where teams actually form
- Look for people who seem organized and have already started discussing ideas
- Avoid groups that are overly large or still debating what to build after the first hour
- If you're solo and looking for a team, walk up to a group that looks like they need your specific skill — "Hey, I heard you're building a React app. I'm a frontend dev — need an extra pair of hands?"

**The golden rule:** Join a team that already has an idea and momentum, not a team that's still brainstorming. You'll get more done in less time.

### Online Hackathons

**Before the event:**
- Introduce yourself in the hackathon's community channels with your timezone, skills, and what you're interested in
- Join a team early — don't wait until the hackathon starts
- Have a quick video call with potential teammates to check for vibe and communication style
- Agree on tools and communication norms before coding begins

**During the event:**
- Over-communicate. In remote settings, silence creates anxiety. Post regular updates even if they're just "still working on the auth flow"
- Use screen sharing liberally — it's the closest thing to looking over someone's shoulder
- Schedule check-ins every 2–3 hours, even if they're just 5-minute standups
- Keep a shared document with task assignments and progress so nobody's status is a mystery

---

## Role Switching for Small Teams

In a 2-person or 3-person team, you can't afford rigid roles. Here's how to handle role switching effectively:

**The generalist rule:** Everyone should be able to handle at least two roles. If your designer can't write a single API endpoint, or your backend dev can't adjust a button color, you're going to bottleneck.

**When to switch roles:**
- When someone is blocked and waiting on someone else's output
- When a person's energy for their current task is dropping (creative work suffers when you're tired)
- When a specific task is clearly a bottleneck that only one person can unblock

**How to switch smoothly:**
- Do a 5-minute handoff: the person switching explains exactly where they left off, what's working, what's broken, and what the next step is
- Leave code comments at the switch point — future-you will thank present-you
- Don't switch too often. Every 2–3 hours is reasonable. Every 20 minutes is chaos.

**The rule of two:** If two people are both struggling with the same task, swap both of them out. Fresh eyes solve problems faster than tired persistence.

---

## Remote Team Coordination

Remote hackathons add a layer of complexity. Here's how to handle it:

**Timezone alignment:** If your team spans time zones, agree on a "core hours" window where everyone is available. Protect those hours for collaborative work — code reviews, pair programming, integration. Use off-hours for individual tasks.

**The shared workspace:** Set up a shared project board (Trello, Notion, or even a shared Google Doc with checkboxes). Every task should be visible to everyone at all times. If you can't see what your teammates are doing, you're already behind.

**Asynchronous communication norms:** Agree on what needs a real-time conversation vs. what can be a message. Quick questions → text. Architecture decisions → voice call. Design reviews → screen share.

**The camera rule:** Turn your camera on during check-ins. It builds trust and makes communication faster. You don't need it on all the time, but for standups and design reviews, seeing faces matters.

**Late-night coordination:** If someone is working late while others sleep, they should leave a detailed status update before logging off. The morning crew should read it before starting work. This handoff protocol prevents the "what did they do last night?" confusion.

---

## Team Health Check

Somewhere around hour 8–12 of a hackathon, do a quick team health check. Ask these questions honestly:

**Energy check:** Is everyone still engaged, or is someone going through the motions? If someone's energy has cratered, give them a break or reassign them to a less demanding task.

**Scope check:** Are we still building the thing we agreed on? Scope creep happens silently — one person adds a feature nobody discussed, and suddenly the project has three half-finished directions.

**Integration check:** Does everyone's code actually work together? Don't wait until hour 20 to find out that the frontend and backend have incompatible data structures.

**Communication check:** Are people talking enough? If someone has been silent for more than an hour, something is wrong — they're either stuck, confused, or disengaged. Check in.

**The fix protocol:** If the health check reveals problems, don't ignore them. Take 15 minutes to fix whatever's broken — reassign tasks, cut scope, or just talk through the frustration. Those 15 minutes will save you hours of compounded problems later.

---

## When to Kick Someone Off the Team

This is the hardest conversation in a hackathon, and it happens more often than people admit. Here's when it's justified and how to handle it.

### When It's Justified

- Someone has been completely absent for more than a third of the hackathon with no communication
- Someone is actively sabotaging the project (refusing to do assigned work, making unilateral changes that break the build)
- Someone is creating a toxic environment (hostility, condescension, refusing to collaborate)
- Someone is asleep when they should be working and it's past the point where they can catch up

### When It's NOT Justified

- Someone is slower than you expected — that's a planning problem, not a them problem
- Someone made a technical mistake — everyone does
- Someone is quiet but still doing their work — introverts aren't broken
- Someone's approach differs from yours — different doesn't mean wrong

### How to Do It

1. Have a direct, private conversation. "Hey, I need to talk to you about something."
2. Be specific about the behavior, not the person. "You've been away for three hours without updating the team" not "You don't care about this."
3. Give them a chance to explain. Maybe there's a legitimate reason.
4. If the behavior continues, be clear: "We're going to move forward without you on this project. I hope that's okay."
5. Don't badmouth them to other teams or judges. Keep it professional.

### The Better Prevention

Most "kicking off" situations are preventable. Set expectations clearly at the start: "If you need to step away, just let us know. If you're stuck, ask for help early. We're all in this together." When expectations are clear, accountability becomes natural rather than confrontational.

---

## Team Rules That Work

These aren't suggestions — they're proven rules that successful hackathon teams follow:

1. **One owner per area.** If everyone owns something, nobody owns it.
2. **Short check-ins only.** 10 minutes max. If you need longer, the problem is scope, not communication.
3. **Decisions are visible.** Write them down. If it's not in writing, it didn't happen.
4. **The MVP is sacred.** Don't sacrifice the core feature for a nice-to-have.
5. **Integrate early and often.** Don't build in isolation for 12 hours and pray it works together.
6. **Rehearse the demo at least twice.** Not once. Twice. The second time catches what the first missed.
7. **Protect people's sleep.** A well-rested teammate produces more than an exhausted one pulling an all-nighter.
8. **No negative energy.** If someone is bringing the mood down, address it directly. Hackathons are hard enough without emotional drag.

---

## Hackathon Team Checklist

Before you start building, make sure every box is checked:

- [ ] Everyone knows the problem we're solving
- [ ] Everyone knows the MVP (minimum viable product)
- [ ] Everyone knows their primary role
- [ ] Everyone knows the backup plan if something fails
- [ ] Everyone knows the demo order and timing
- [ ] Everyone has access to the repo, deploy environment, and shared docs
- [ ] Everyone knows the communication tool and norms
- [ ] Everyone has agreed on the tech stack
- [ ] Everyone knows when the deadline is and what the final hour looks like
- [ ] Everyone has eaten, hydrated, and knows when they're sleeping

---

## The Unspoken Truth About Team Selection

Skills matter, but not as much as you think. The best hackathon teams aren't formed by picking the most technically skilled people — they're formed by picking people who reduce chaos.

Look for people who:
- Respond quickly to messages
- Can explain their ideas simply
- Don't overthink decisions
- Stay calm when things break
- Are comfortable with imperfection
- Take ownership without being asked

Avoid people who:
- Need consensus for every small decision
- Over-engineer everything
- Go silent when stressed
- Blame others when things go wrong
- Care more about the tech than the user

The hackathon team selection tip: **Choose people who reduce chaos, not people who create more meetings.**
