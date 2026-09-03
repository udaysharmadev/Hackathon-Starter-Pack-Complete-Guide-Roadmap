# 13. GitHub for Hackathons

Your GitHub repo is your project's first impression. Judges, recruiters, and collaborators will look at it — and they'll form an opinion within 10 seconds. A messy repo with an empty README screams "we ran out of time." A clean repo with screenshots, a live demo link, and clear setup instructions says "we're professionals." This section covers how to make your repo work as hard as your code does.

---

## Git Workflow for Hackathons

You don't need a complex branching strategy for a 24-hour project. But you do need *some* structure, or you'll end up with merge conflicts at 4 AM that nobody can fix.

### The Simple Branch Strategy

```
main          ← always working, always deployable
├── feat/auth ← feature branches for major pieces
├── feat/ui
└── fix/api
```

- **main** is your production branch. Never push directly to it. It should always work.
- **Feature branches** are for individual work. Create one when you start a significant piece of work (authentication, a new page, API integration). Merge it back to main when it's tested and working.
- **Fix branches** are for quick bugfixes. Same process — branch, fix, test, merge.

### When to Merge

Merge back to main whenever:
- A feature is complete and tested
- You've fixed a bug that affects other people's work
- It's been more than 2 hours since your last merge (long-lived branches are dangerous at hackathons)

Don't merge when:
- The code is halfway done
- You haven't tested it at all
- It breaks the build (obvious, but you'd be surprised)

### Commit Message Conventions

Keep it simple and consistent:

```
feat: add user authentication with JWT
fix: resolve login redirect loop
ui: polish landing page responsive design
docs: add setup instructions to README
refactor: simplify API route structure
chore: update dependencies
```

The prefix tells your teammates what kind of change it is at a glance. At a hackathon, this is more useful than detailed descriptions because people are scanning, not reading.

**The golden rule:** Commit often. Small, frequent commits are infinitely better than one massive commit at the end. If something breaks, you can roll back to the last working state instead of losing everything.

### The No-Go Rules

- Never force-push to main. Ever.
- Never commit `.env` files, API keys, or secrets. Use `.env.example` with placeholders.
- Never commit `node_modules/`, `__pycache__/`, or build artifacts. Use `.gitignore` from the start.
- Never work on main for more than 30 minutes without committing.

---

## README Anatomy: Section by Section

A winning hackathon README isn't a novel — it's a sales page. Here's what each section should contain, annotated with exactly what judges and recruiters are looking for.

### 1. Title and One-Liner

```markdown
# 🧠 MindMap AI
**Turn your messy notes into visual mind maps using AI**
```

**What this does:** Immediately tells the reader what the project is. No jargon, no buzzwords. The subtitle explains the value in plain English.

### 2. Live Demo Link + Screenshot

```markdown
🔗 **[Live Demo](https://mindmap-ai.vercel.app)** | 🎥 **[Video Demo](https://youtube.com/...)**

![MindMap AI Screenshot](./assets/screenshot.png)
```

**What this does:** Judges want to see it working in under 5 seconds. Put the live link at the very top. The screenshot should show the most impressive screen — not the landing page, not the login screen. Show the thing that makes your project special.

### 3. Problem Statement

```markdown
## The Problem
Students and professionals take hundreds of notes but never organize them. 
Existing mind map tools require manual input, defeating the purpose of quick note-taking.
```

**What this does:** Frames the project in terms of real human need. Judges score "problem relevance" separately from "technical execution." Don't skip this.

### 4. What We Built

```markdown
## What We Built
MindMap AI is a web app that:
- 📸 Accepts photo uploads of handwritten or typed notes
- 🤖 Uses GPT-4 to extract key concepts and relationships
- 🗺️ Generates interactive mind maps automatically
- 📤 Exports to PDF, PNG, or Markdown
```

**What this does:** Bullet points are scannable. Judges review 20–40 projects. They're not reading paragraphs. Each bullet should describe a feature that's visible in the demo.

### 5. Tech Stack

```markdown
## Tech Stack
- **Frontend:** React, Tailwind CSS, D3.js (for mind map visualization)
- **Backend:** Node.js, Express
- **AI:** OpenAI GPT-4 API
- **Database:** PostgreSQL (via Supabase)
- **Deployment:** Vercel, Railway
```

**What this does:** Shows technical breadth without overwhelming. If you used a sponsor's API, mention it here — sponsors notice.

### 6. Architecture Diagram

```markdown
## Architecture
![Architecture Diagram](./assets/architecture.png)
```

**What this does:** A simple diagram (even hand-drawn and photographed) shows that you understand how your pieces fit together. Use Mermaid, Excalidraw, or draw.io. It doesn't need to be fancy — it needs to exist.

### 7. Setup Instructions

```markdown
## Getting Started
```bash
git clone https://github.com/yourteam/mindmap-ai.git
cd mindmap-ai
cp .env.example .env  # Add your API keys
npm install
npm run dev
```

**What this does:** If a judge or recruiter wants to run your project locally, they should be able to in under 2 minutes. Three commands max. If your setup requires more than that, you've overcomplicated it.

### 8. Screenshots and GIFs

```markdown
## Screenshots
| Upload Notes | AI Processing | Generated Mind Map |
|---|---|---|
| ![Upload](./assets/upload.png) | ![Processing](./assets/processing.gif) | ![Mindmap](./assets/mindmap.png) |
```

**What this does:** Visual proof that the project works. GIFs of the core interaction are worth more than any description. Use tools like Loom, OBS, or Kap to record short clips.

### 9. What's Next

```markdown
## What's Next
- [ ] Mobile app with camera capture
- [ ] Collaborative mind maps (real-time editing)
- [ ] Integration with Notion and Obsidian
```

**What this does:** Shows judges that you've thought beyond the hackathon. This signals product thinking, not just coding ability.

### 10. Team and Contributions

```markdown
## Team
- **Alice Chen** — Backend & AI integration ([@alice](https://github.com/alice))
- **Bob Kumar** — Frontend & UI/UX ([@bob](https://github.com/bob))
- **Carol Smith** — Pitch & presentation ([@carol](https://github.com/carol))
```

**What this does:** Gives credit and shows who did what. Recruiters browsing repos will check individual contributions.

### 11. License

```markdown
## License
MIT License — see [LICENSE](./LICENSE) for details.
```

**What this does:** Signals that this is a real project, not a throwaway hack.

---

## License Guide: Which License for What

| License | When to Use | Key Feature |
|---|---|---|
| **MIT** | Default for hackathons. Simple, permissive, everyone can use it. | Maximum freedom — anyone can use, modify, and distribute |
| **Apache 2.0** | Projects that might have patent implications or you want patent protection. | Includes explicit patent grant — good for AI/ML projects with potential IP |
| **GPL v3** | You want derivatives to also be open source. | Copyleft — if someone uses your code, their project must also be GPL |
| **BSD 2-Clause** | Similar to MIT but slightly different language. | Minimal restrictions, very permissive |
| **Creative Commons** | For non-code assets (designs, documentation, datasets). | Not for software — for creative works |
| **No License** | Technically means "all rights reserved." Don't do this. | Your code can't be legally used by anyone |

**The hackathon default:** MIT. It's what judges expect, it's what recruiters recognize, and it doesn't create legal complications. If you're building something with AI models or patents, consider Apache 2.0. Don't overthink this — just pick one and include a LICENSE file.

---

## GitHub Actions: CI/CD for Hackathon Projects

GitHub Actions can automate your deployment so that every push to main automatically deploys your project. This is easier than it sounds.

### The Minimal CI/CD Setup

Create `.github/workflows/deploy.yml`:

```yaml
name: Deploy

on:
  push:
    branches: [main]

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with:
          node-version: 20
      - run: npm ci
      - run: npm test
      - run: npm run build
      - uses: amondnet/vercel-action@v25
        with:
          vercel-token: ${{ secrets.VERCEL_TOKEN }}
          vercel-org-id: ${{ secrets.VERCEL_ORG_ID }}
          vercel-project-id: ${{ secrets.VERCEL_PROJECT_ID }}
```

**What this does:** Every time you push to main, GitHub automatically runs your tests, builds your project, and deploys it to Vercel. No manual deploy commands. No "oh wait, I forgot to deploy."

### Why This Matters at a Hackathon

- Your demo link is always up to date
- You never have to remember to deploy
- If something breaks, you can see exactly which commit caused it
- Judges can click your live link at any time and see the latest version

### One-Click Deploy Badges

Add a deploy badge to your README:

```markdown
[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https://github.com/yourteam/mindmap-ai)
```

This lets anyone deploy a copy of your project with one click. Judges love this because it means your project is reproducible.

---

## Repo as a Product Page Mindset

The biggest shift in thinking: **your repo is not a code dump — it's a product landing page.**

Think about what a product landing page does:
- Explains the value proposition immediately
- Shows the product in action
- Makes it easy to get started
- Builds trust through visuals and social proof

Your repo should do the same:

**Value proposition** → The README title and subtitle
**Product in action** → Screenshots, GIFs, and video demo
**Easy to get started** → Setup instructions
**Trust signals** → Architecture diagram, tech stack, contribution guidelines

When you view your repo this way, you stop thinking about it as "where I store my code" and start thinking about it as "the first thing a judge sees." That shift changes everything about how you organize and present it.

---

## Issue Tracking for Hackathon Teams

You don't need Jira. You don't even need a complex system. But you do need something more structured than "I'll remember what I was working on."

### The Minimum Viable Issue System

Use GitHub Issues with labels:

| Label | Color | Meaning |
|---|---|---|
| `urgent` | Red | Must be done before demo |
| `backend` | Blue | Backend work |
| `frontend` | Green | Frontend work |
| `design` | Purple | UI/UX work |
| `pitch` | Yellow | Presentation work |
| `blocked` | Orange | Can't proceed without something |

### How to Use It

1. At the start, create 3–5 issues for the core features
2. Assign each issue to an owner
3. When you finish something, close the issue with a short comment
4. When you're blocked, add the `blocked` label and describe what you need
5. At hour 12, review all open issues and cut anything that's not critical

**The rule:** If it's not an issue, it doesn't exist. Verbal agreements disappear. Written issues persist.

---

## How Judges Actually Review Repos

Judges don't have time to read every line of code. Here's what they actually do:

1. **Click the live demo link.** If it's broken, you've lost points immediately. Make sure it works.
2. **Look at the README.** They scan for a clear problem statement, screenshots, and a tech stack. If the README is empty or confusing, they move on.
3. **Check the repo structure.** They look for clean organization, meaningful commit history, and a `.gitignore` that works.
4. **Glance at the code.** They're not reading every file. They'll open one or two files to check code quality, naming conventions, and whether there are comments or documentation.
5. **Look at the team.** Who contributed what? Are there meaningful commits from multiple people?

**The 10-second test:** Open your repo in an incognito window. Can you figure out what the project does, see it working, and understand the tech stack within 10 seconds? If not, your README needs work.

### What Judges Don't Care About

- How many commits you made (quality, not quantity)
- Whether you used the "right" framework (there is no right framework)
- How complex your code is (simple and working beats complex and broken)
- Whether you followed every best practice (at a hackathon, shipping matters more than perfection)

---

## GitHub Profile Optimization

Your GitHub profile is your technical resume. Recruiters check it. Judges check it. Here's how to make it work for you.

### The Profile README

GitHub lets you create a special repository with the same name as your username. The README in that repo appears on your profile page. Use it.

**What to include:**
- A one-liner about who you are and what you do
- Current projects (link your hackathon projects here)
- Technologies you work with
- How to reach you

### Contribution Graph

The green squares on your profile matter more than you think. Consistent contributions signal that you code regularly — not just during hackathons. If your contribution graph is empty except for one week in March (when a hackathon happened), it looks like you only code under pressure.

**The fix:** Even 15 minutes of daily coding will keep your graph active. Side projects, open source contributions, or even just committing small improvements to existing projects.

### Pinned Repositories

Pin your best 6 repositories. For hackathon participants, this should include:
1. Your best hackathon project
2. A personal project that shows depth
3. An open source contribution
4. A project that demonstrates a specific skill you want to be hired for

### The Badges and Stats

Include shields.io badges in your profile README to show your tech stack visually. They're free, they look professional, and they help recruiters quickly identify your skills.

---

## Common Mistakes

- **Empty README:** The single most damaging thing. A repo without a README is invisible.
- **No live link:** If you can't deploy it, judges assume it doesn't work.
- **No screenshots:** A project with no visuals looks unfinished even if it's complete.
- **Broken links:** Check every link before submitting. A broken demo link during judging is devastating.
- **Messy commit history:** "fix", "fix again", "final fix", "FINAL FINAL fix" — this tells judges you don't know what you're doing.
- **No explanation of core value:** If the README doesn't explain why this project matters, judges won't figure it out on their own.
- **Secrets in the repo:** Accidentally committed an API key? Judges will see it as a security red flag. Use environment variables and `.env.example`.
- **No license:** Without a license, your code is technically "all rights reserved." This looks amateurish.

---

## Best Practice

The repo itself should help a judge understand the project faster. Think of it as a self-service demo — someone should be able to read the README, click the live link, and understand everything without talking to you. That's the mark of a well-organized hackathon project.
