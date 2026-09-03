# Team Roles & Responsibilities

Four roles, each with clear ownership. In a 24-hour hackathon, ambiguity kills velocity. This document defines who does what, when they do it, and how to resolve conflicts.

---

## Role Definitions

### 1. Builder (Tech Lead)
Owns the codebase. Makes architecture decisions. Unblocks technical problems. If the app crashes, they fix it. If a library doesn't work, they find the alternative.

### 2. Designer
Owns the user experience. UI components, color palette, spacing, accessibility. Makes the app look like it wasn't built in 24 hours. Also owns the demo flow and presentation slides.

### 3. Pitch Lead
Owns the story. Writes the pitch script, handles Q&A prep, coordinates the demo. The pitch lead speaks during judging — not because they're smarter, but because they've practiced the most.

### 4. Integrator
Owns the glue. Connects frontend to backend, manages API contracts, handles deployment, keeps the README updated. The integrator is the person who knows what's broken before anyone else.

---

## RACI Matrix

**R** = Responsible (does the work), **A** = Accountable (signs off), **C** = Consulted, **I** = Informed

| Task | Builder | Designer | Pitch Lead | Integrator |
|------|---------|----------|------------|------------|
| Project setup & scaffolding | **R** | C | I | **A** |
| Core feature development | **R** | C | I | C |
| UI/UX design | C | **R/A** | I | I |
| Component implementation | C | **R** | I | **A** |
| API design & endpoints | **R** | I | I | **A** |
| Database/data model | **R** | I | I | **A** |
| Testing & debugging | **R** | C | I | **R** |
| Deployment (staging) | I | I | I | **R/A** |
| Deployment (production) | C | I | **A** | **R** |
| Pitch script writing | I | C | **R/A** | I |
| Demo flow design | C | **R** | **A** | C |
| Live demo execution | I | C | **R** | C |
| Q&A preparation | C | I | **R/A** | C |
| README & documentation | I | I | C | **R/A** |
| Slide design | C | **R** | **A** | I |
| Judge communication | I | I | **R/A** | I |
| Git management | C | I | I | **R/A** |
| Time management (overall) | I | I | **R/A** | C |
| Risk & blocker management | C | C | **A** | **R** |
| Post-hackathon follow-up | C | C | **R** | **R** |

---

## What Each Role Does: Hour-by-Hour

### Hour 1-3: Setup & Planning

| Role | Tasks |
|------|-------|
| **Builder** | Initialize repo, set up project structure, install dependencies, create boilerplate, verify dev environment works |
| **Designer** | Research similar products, sketch wireframes (even on paper), define color palette, set up Figma/design file |
| **Pitch Lead** | Research judges' backgrounds, study past winners, draft problem statement, start assembling pitch narrative |
| **Integrator** | Set up GitHub repo with branches, create `.env.example`, set up CI/deployment pipeline, write initial README |

### Hour 4-10: Build Phase

| Role | Tasks |
|------|-------|
| **Builder** | Core feature #1, core feature #2, write tests for critical paths |
| **Designer** | Design key screens, create UI components, prototype interactions, review builder output for UX |
| **Pitch Lead** | Write first draft of pitch, create slide deck outline, prepare demo storyboard |
| **Integrator** | Connect frontend to backend, manage API integration, handle auth, fix deployment issues |

### Hour 11-18: Integration & Polish

| Role | Tasks |
|------|-------|
| **Builder** | Bug fixes, performance optimization, edge case handling |
| **Designer** | Polish UI, responsive design, accessibility pass, final screenshot captures |
| **Pitch Lead** | Refine pitch timing, practice delivery, prepare Q&A answers, backup plan for demo |
| **Integrator** | Final deployment, environment variables check, domain/URL setup, README finalization |

### Hour 19-24: Demo Prep & Delivery

| Role | Tasks |
|------|-------|
| **Builder** | Last-minute bug fixes, stand by for live demo issues, have rollback plan ready |
| **Designer** | Final slide polish, prepare handout materials, ensure demo device looks good |
| **Pitch Lead** | Full run-through 2x, memorize opening/closing, calibrate timing, breathe |
| **Integrator** | Verify deployment is live, test all URLs, have backup server/device ready |

---

## Communication Protocols

### Stand-Up Check-ins (Every 2-3 Hours)
Each person answers three questions in 30 seconds:
1. What did I just finish?
2. What am I working on next?
3. Am I blocked on anything?

### Blocker Escalation
```
Level 1: Try to fix it yourself (15 min max)
Level 2: Ask the Integrator (they'll know if it's systemic)
Level 3: Ask the Builder (if it's core architecture)
Level 4: Team huddle (5 min max, then someone owns the fix)
```

### Code Review Rules
- No code goes to `main` without at least one review
- Reviewer's job is to find bugs, not rewrite code
- If a review takes more than 5 minutes, it's too big — break it up
- Emergency hotfixes: push to `main`, but comment what you did and why

### Decision-Making Protocol
- **Technical decisions**: Builder decides (with Integrator input)
- **Design decisions**: Designer decides (with Pitch Lead input)
- **Presentation decisions**: Pitch Lead decides (with Designer input)
- **Anything affecting timeline**: Pitch Lead decides (they're tracking time)
- **Tie votes**: Flip a coin. Speed over perfection.

---

## Conflict Resolution Scripts

**When two people disagree on architecture:**
> "Let's write down the two options with pros and cons. We have 5 minutes. Then Builder decides and we move on. No grudges."

**When the designer and builder disagree on UI:**
> "Ship the builder's version now, polish it later. Function before form at hour 8. Form before function at hour 18."

**When someone is blocking others:**
> "Hey, I need this API endpoint working by [time] or I can't proceed. Can we pair on this for 15 minutes?"

**When the pitch lead changes the demo flow:**
> "This is a presentation decision — I'm going to own this call. I hear your concern, and if the judges ask about [topic], we'll have you answer."

**When morale drops (it will, around hour 16):**
> "We're tired, but we're 60% done. Let's take 15 minutes, grab food, and come back with fresh eyes. The best ideas come when you stop forcing them."

---

## Role Switching Guide (2-3 Person Teams)

When you don't have 4 people, roles overlap. Here's how to adapt:

### 2-Person Team

| Person | Primary Roles | Secondary Roles |
|--------|---------------|-----------------|
| **Person A** | Builder + Integrator | Pitch backup |
| **Person B** | Designer + Pitch Lead | Git management |

**Key adjustments:**
- Builder handles all technical decisions, deployment, AND API work. It's a lot — prioritize ruthlessly.
- Designer handles all visual work AND the pitch. Practice the pitch while doing design work (literally talk through it out loud).
- Pair program for the first 2 hours to align on technical decisions.

### 3-Person Team

| Person | Primary Roles | Secondary Roles |
|--------|---------------|-----------------|
| **Person A** | Builder | Deployment (shared with Integrator) |
| **Person B** | Designer | Pitch backup |
| **Person C** | Integrator + Pitch Lead | Git management |

**Key adjustments:**
- Integrator and Pitch Lead is a natural combo — both own communication (API = technical communication, pitch = human communication).
- Builder can focus purely on code. Let them zone out.
- Designer handles slides, demo flow, and UI. They'll be busiest in the last 4 hours.

### Solo (The Hard Mode)

If you're going solo (we don't recommend it, but respect):
- **Hours 1-2**: Plan everything. Write your pitch first. Build toward the pitch, not the other way around.
- **Hours 3-16**: Build. Use a boilerplate. Don't reinvent anything.
- **Hours 17-20**: Polish UI, write README, deploy.
- **Hours 21-24**: Practice pitch, prepare backup demo, sleep for 1 hour.

---

## Role Assessment Quiz

Not sure which role fits you? Answer these honestly:

1. "I get excited about code architecture" → **Builder**
2. "I notice when padding is 12px instead of 16px" → **Designer**
3. "I've won (or bombed) a speech contest" → **Pitch Lead**
4. "I've set up a CI/CD pipeline for fun" → **Integrator**
5. "I notice all of the above" → **You're the team lead. Pick Integrator + team lead.**
