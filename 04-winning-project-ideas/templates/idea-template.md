# Idea Template

Fill this out before you write a single line of code. Share it with your team. Get alignment. Then build.

---

## Problem
*What specific pain does the user experience? Be concrete — include numbers, time wasted, money lost.*

**Template prompt:** "Users spend [X hours/week/dollars] dealing with [specific problem]. Current solutions are [bad because Y]."

---

## User
*Who exactly is this for? One sentence. Not "everyone" — that's no one.*

**Template prompt:** "This is for [specific role] who needs to [specific task] but currently has to [painful workaround]."

---

## MVP
*What is the absolute minimum you can ship in the hackathon timeframe? Write the ONE thing that makes this project work. Cut everything else.*

**Template prompt:** "In [X hours], we will build [one feature] that lets the user [one action] and produces [one output]."

---

## Architecture
*High-level diagram. What talks to what? What data flows where?*

Keep it simple:
```
[User] → [Frontend] → [API] → [Database]
                    ↘ [External API / Sponsor Tool]
```

**Rules:**
- One page, one box per component
- Show data flow with arrows
- Label your sponsor integration clearly
- If it's more than 6 boxes, you've overcomplicated it

---

## APIs
*What external services are you using? List them with their free tier limits.*

| API | What it does | Free tier limit | Auth method |
|-----|-------------|-----------------|-------------|
| OpenAI | GPT-4 for text generation | 3 RPM / 10K tokens/day | API key |
| Stripe | Payments | $100 in test mode | Secret key |
| Twilio | SMS/WhatsApp | 1 free trial number | Account SID |
| Supabase | DB + Auth + Realtime | 500MB / 50K MAU | JWT |

**Sponsor API check:** If the hackathon has a sponsor track, make sure at least ONE of these APIs is the sponsor's.

---

## Deployment
*Where does this live? Can a judge access it without installing anything?*

| Platform | Cost | Pros | Cons |
|----------|------|------|------|
| Vercel | Free | Fast, auto-deploy from GitHub | No backend runtime (use API routes) |
| Railway | $5 free credit | Full backend, databases | Costs add up |
| Fly.io | Free tier | Global edge, Docker support | Steeper learning curve |
| Render | Free tier | Easy setup | Cold starts on free plan |

**Your choice:** _________________________
**Backup choice:** _________________________

---

## Demo Flow
*Map out exactly what the judge will see in your 2–3 minute demo. Every second counts.*

**Minute 1: The Hook**
- Open the app → show the problem (e.g., empty dashboard)
- Take one action → show the solution (e.g., data fills in)
- One-liner: "This is [product] — it [solves X problem] for [Y user]."

**Minute 2: The Features**
- Feature 1: [specific action] → [visible result]
- Feature 2: [specific action] → [visible result]
- Sponsor integration: [specific action] → [visible result]

**Minute 3: The Close**
- Show the architecture (quick, 10 seconds)
- State the impact: "This would save [X users] [Y hours/dollars]"
- One future feature: "With more time, we'd add [Z]"

**The 30-Second Rule:** If a judge can't understand your project in the first 30 seconds, your demo is too complicated. Cut features until it's obvious.

---

## Judge Appeal
*Why will judges care? Map your project to the judging criteria.*

| Judging Criterion | How your project scores |
|-------------------|------------------------|
| Innovation | [What's new/different about your approach?] |
| Impact | [How many people does this help? How much?] |
| Technical complexity | [What's hard about what you built?] |
| Design | [How polished is the UI/UX?] |
| Presentation | [How compelling is your pitch?] |
| Sponsor alignment | [How deeply do you use the sponsor's tech?] |

---

## Scaling Path
*If this won the hackathon and you had 6 months, what would you build next?*

**Phase 1 (Month 1–2):** [Core product polish + 10 beta users]
**Phase 2 (Month 3–4):** [Scale to 100 users + paid tier]
**Phase 3 (Month 5–6):** [API / platform play + integrations]

---

## Risk Assessment

| Risk | Likelihood | Impact | Mitigation |
|------|-----------|--------|------------|
| API rate limits during demo | Medium | High | Cache responses, use mock data backup |
| Teammate drops out | Low | Critical | Document everything, pair on core features |
| Deployment fails last minute | Medium | High | Deploy early, test multiple platforms |
| Sponsor API is down | Low | Medium | Have a fallback API or mock data |
| Scope creep | High | High | Lock MVP scope NOW, write it down |

---

## Sponsor Alignment Check

- [ ] At least one sponsor API/tool is integrated
- [ ] The sponsor integration is VISIBLE in the demo (not hidden)
- [ ] You can explain in one sentence how the sponsor's tech powers your project
- [ ] You've checked the sponsor's specific bonus prizes
- [ ] Your submission mentions the sponsor by name

---

# Filled Example 1: AI Project

## Problem
Developers spend 45 minutes per code review reading through files, looking for security issues and bugs. 60% of these issues are repetitive patterns that AI could catch instantly.

## User
Mid-level backend developer at a startup doing 3–4 code reviews per week.

## MVP
A GitHub bot that scans pull requests, highlights security vulnerabilities and common bugs inline, and suggests fixes. Works in under 10 seconds per PR.

## Architecture
```
[GitHub Webhook] → [Cloud Function] → [OpenAI API]
      ↓                                    ↓
[PR Differ] → [Analysis] → [Inline Comments] → [GitHub API]
```

## APIs
| API | What it does | Free tier limit |
|-----|-------------|-----------------|
| OpenAI | Code analysis + fix suggestions | 10K tokens/day |
| GitHub | PR access + commenting | 1K requests/hour |
| Supabase | Store review history | 500MB |

## Demo Flow
**Minute 1:** Show a PR with a SQL injection vulnerability → bot auto-comments with fix
**Minute 2:** Show a PR with 5 common bugs → bot catches all 5 with severity ratings
**Minute 3:** Show dashboard of review stats → "This PR saved 40 minutes"

## Judge Appeal
- **Innovation:** AI code review isn't new, but real-time GitHub integration with inline fixes is
- **Impact:** 45 min saved per review × 4 reviews/week = 3 hours/week per developer
- **Technical complexity:** Diff parsing, AST analysis, OpenAI prompt engineering

---

# Filled Example 2: Civic Tech Project

## Problem
Voters in local elections have no easy way to compare candidates on issues they care about. 70% of young voters skip local elections because they don't know who aligns with their views.

## User
18–30 year old voter who cares about 2–3 specific issues but doesn't have time to research every candidate.

## MVP
A 2-minute quiz that matches voters to local candidates based on their priorities. Shows a side-by-side comparison on the issues that matter most.

## Architecture
```
[User Quiz] → [Matching Algorithm] → [Results Page]
                                         ↓
[Scraped Data] → [Candidate DB] → [Comparison View]
```

## APIs
| API | What it does | Free tier limit |
|-----|-------------|-----------------|
| Census API | District lookup by address | Unlimited |
| Google Civic Info | Candidate data | 1K/day |
| Supabase | Quiz responses + candidate DB | 500MB |

## Demo Flow
**Minute 1:** Take the quiz (3 questions) → get matched to 3 candidates
**Minute 2:** Side-by-side comparison on your top issue → clear winner shown
**Minute 3:** Share your results → "I matched with [Candidate A] on climate policy"

## Judge Appeal
- **Impact:** Could increase youth voter turnout in local elections
- **Innovation:** Simple quiz format vs. complex ballot guides
- **Sponsor fit:** Uses Google Civic Info API directly

---

# Filled Example 3: Health Tech Project

## Problem
Elderly patients miss medication doses 50% of the time because current pill reminder apps are too complicated, have tiny text, and require smartphone literacy.

## User
Adult children (30–50) managing medication for aging parents who struggle with technology.

## MVP
A WhatsApp bot that sends medication reminders via voice messages in the user's preferred language. Family members get a daily compliance report via SMS.

## Architecture
```
[Medication Schedule] → [Cron Job] → [Twilio WhatsApp API]
                                           ↓
[Elderly Parent] ← [Voice Message Reminder]
                                           ↓
[Twilio SMS] → [Family Member Dashboard]
```

## APIs
| API | What it does | Free tier limit |
|-----|-------------|-----------------|
| Twilio WhatsApp | Voice reminders | $15 trial credit |
| Twilio SMS | Family notifications | $15 trial credit |
| ElevenLabs | Natural voice synthesis | 10K chars/month |

## Demo Flow
**Minute 1:** "Here's Mom's pill schedule" → show simple config screen
**Minute 2:** Simulate 8 AM reminder → WhatsApp voice message plays
**Minute 3:** "Here's Dad's compliance this week" → family dashboard with green/red grid

## Judge Appeal
- **Impact:** Affects 6.5 million Americans who help manage elderly parents' care
- **Innovation:** WhatsApp as interface (no app download, works on any phone)
- **Design:** Accessibility-first — large text, voice-first, multilingual

---

*Fill out ONE of these before building. If you can't fill it out clearly, your idea isn't clear enough to build.*
