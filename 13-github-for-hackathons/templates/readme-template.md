# README Template for Hackathon Projects

Copy this entire file into your repo's `README.md`. Replace every `[bracketed item]` with your actual content. Delete sections that don't apply — but try to keep all of them. Judges check READMEs.

---

```markdown
<div align="center">

# [Project Name]

### [One-line value proposition — what does it do and why should I care?]

[![Built at](https://img.shields.io/badge/Built%20at-[Hackathon Name]-blueviolet)](https://[hackathon-url])
[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen)](#contributing)
[![Stars](https://img.shields.io/github/stars/[your-username]/[repo]?style=social)](https://github.com/[your-username]/[repo])

[![Tech Stack](https://img.shields.io/badge/Next.js-black?logo=next.js)](https://nextjs.org)
[![Tech Stack](https://img.shields.io/badge/TypeScript-blue?logo=typescript)](https://typescriptlang.org)
[![Tech Stack](https://img.shields.io/badge/PostgreSQL-316192?logo=postgresql)](https://postgresql.org)
[![Tech Stack](https://img.shields.io/badge/OpenAI-412991?logo=openai)](https://openai.com)

[SCREENSHOT OR GIF — place a screenshot or demo GIF here. Use 1200x630 for social media preview.]

</div>

---

## Problem

**[1-2 sentences about the problem you're solving.]**

[Add a relatable scenario or stat. Make the reader feel the pain. Example: "Students waste an average of 2.5 hours per week searching for available study spaces on campus. Most of this time is spent physically walking between buildings, checking rooms that turn out to be occupied."]

## Solution

**[1-2 sentences about your solution.]**

[Explain your approach simply. Avoid jargon. Example: "StudySpot uses real-time occupancy data from existing building sensors to show available study spaces on a live campus map. Students open the app, see green pins for open rooms, and navigate directly there."] 

### How it works

1. **[Step 1]** — [What happens] (e.g., "User opens the app and sees a map of their campus")
2. **[Step 2]** — [What happens] (e.g., "AI analyzes sensor data and shows room availability in real-time")
3. **[Step 3]** — [What happens] (e.g., "User taps a room to see details: capacity, amenities, noise level")
4. **[Step 4]** — [What happens] (e.g., "Navigation directs them to the nearest entrance")

## Live Demo

🔗 **[Live Demo Link](https://[your-deployment-url])**

> [Note if there's anything special about accessing the demo — e.g., "Use test account: demo@university.edu / password123" or "Best viewed on mobile"]

## Screenshots

| Dashboard | Map View | Details |
|-----------|----------|---------|
| ![Dashboard](screenshots/dashboard.png) | ![Map](screenshots/map.png) | ![Details](screenshots/details.png) |

> To add screenshots: place PNG/JPG files in a `screenshots/` folder in your repo, then reference them above.

## Features

- ✅ [Feature 1] — [Brief description]
- ✅ [Feature 2] — [Brief description]
- ✅ [Feature 3] — [Brief description]
- ✅ [Feature 4] — [Brief description]
- ✅ [Feature 5] — [Brief description]
- 🔜 [Planned Feature] — [What you'd add with more time]

## Tech Stack

| Layer | Technology | Why |
|-------|-----------|-----|
| Frontend | [e.g., Next.js 14] | [Why you chose it] |
| Backend | [e.g., FastAPI] | [Why you chose it] |
| Database | [e.g., PostgreSQL] | [Why you chose it] |
| AI/ML | [e.g., OpenAI GPT-4] | [Why you chose it] |
| Auth | [e.g., NextAuth.js] | [Why you chose it] |
| Hosting | [e.g., Vercel] | [Why you chose it] |

## Architecture

```
┌─────────────┐     ┌─────────────┐     ┌─────────────┐
│   Frontend  │────▶│   Backend   │────▶│  Database   │
│  (Next.js)  │     │  (FastAPI)  │     │ (PostgreSQL)│
└─────────────┘     └──────┬──────┘     └─────────────┘
                           │
                           ▼
                    ┌─────────────┐
                    │  External   │
                    │    APIs     │
                    └─────────────┘
```

> Replace this with your actual architecture. Tools: [Excalidraw](https://excalidraw.com), [dbdiagram.io](https://dbdiagram.io), [draw.io](https://draw.io). Export as PNG and commit to `screenshots/` folder.

## Setup

### Prerequisites

- Node.js >= [version]
- [Database] (e.g., PostgreSQL >= 14)
- [Any other dependencies]

### Installation

```bash
# Clone the repo
git clone https://github.com/[your-username]/[repo-name].cd
cd [repo-name]

# Install dependencies
npm install    # or pip install -r requirements.txt, etc.

# Set up environment variables
cp .env.example .env
# Edit .env with your API keys

# Set up the database
npx prisma db push    # or your migration command

# Start the dev server
npm run dev
```

### Environment Variables

| Variable | Description | Required |
|----------|-------------|----------|
| `DATABASE_URL` | Your database connection string | Yes |
| `OPENAI_API_KEY` | OpenAI API key for AI features | Yes |
| `NEXTAUTH_SECRET` | Random string for auth encryption | Yes |
| `NEXTAUTH_URL` | Your app URL (e.g., http://localhost:3000) | Yes |

> Never commit `.env` files. The `.env.example` file should list all required variables without actual values.

## Project Structure

```
[repo-name]/
├── src/
│   ├── components/      # UI components
│   ├── pages/           # Route pages
│   ├── lib/             # Utility functions
│   ├── hooks/           # Custom React hooks
│   └── styles/          # CSS/styling
├── api/                 # Backend API routes
├── prisma/              # Database schema
├── public/              # Static assets
├── screenshots/         # Demo screenshots
├── .env.example         # Environment variable template
├── package.json
└── README.md
```

## What We Built in [X] Hours

| Hours | What | Who |
|-------|------|-----|
| 0-4 | [Setup, core features] | [Names] |
| 4-12 | [Feature development] | [Names] |
| 12-18 | [Integration, polish] | [Names] |
| 18-24 | [Bug fixes, demo prep] | [Names] |

## Challenges & Learnings

- **[Challenge 1]**: [What went wrong and how you fixed it]
- **[Challenge 2]**: [What surprised you and what you learned]
- **[Challenge 3]**: [What you'd do differently next time]

## What's Next

If we had more time, we'd:

1. [Feature/improvement 1]
2. [Feature/improvement 2]
3. [Feature/improvement 3]

## Team

| Name | Role | LinkedIn | GitHub |
|------|------|----------|--------|
| [Name] | [Role] | [LinkedIn URL] | [GitHub URL] |
| [Name] | [Role] | [LinkedIn URL] | [GitHub URL] |

## Contributing

Contributions welcome! Steps:

1. Fork this repo
2. Create a branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License — see [LICENSE](LICENSE) for details.

---

<div align="center">

Built with ❤️ at [Hackathon Name] by [Team Name]

[![Twitter](https://img.shields.io/badge/Twitter-@handle-blue)](https://twitter.com/[handle])
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Company-0A66C2)](https://linkedin.com/company/[company])

</div>
```

---

## README Checklist Before Submission

- [ ] All `[brackets]` replaced with actual content
- [ ] Screenshots/GIF added and displaying correctly
- [ ] All links work (demo, repo, badges)
- [ ] No secrets or API keys in the README
- [ ] Setup instructions actually work (test on a fresh machine or ask someone to follow them)
- [ ] Architecture diagram is accurate
- [ ] Team section is complete with correct info
- [ ] At least one badge is present (hackathon name, license, or tech stack)
- [ ] Code blocks render correctly
- [ ] README looks good on mobile (many judges review on phones)
