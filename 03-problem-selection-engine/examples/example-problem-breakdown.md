# Example Problem Breakdown: Scored Using the 7-Factor System

Each problem is scored on 7 factors, 1-5 each. Total out of 35. Here's how three real problem ideas stack up.

---

## Problem A: "MediTrack — Medication Reminder for Elderly Patients"

### The Idea
A mobile app that reminds elderly patients to take their medications on time and alerts family members if a dose is missed. Uses SMS as a fallback for users without smartphones.

### The 7-Factor Scorecard

| Factor | Score | Reasoning |
|---|---|---|
| **1. Pain Intensity** | 5/5 | 125,000 Americans die annually from medication non-adherence. This is life-or-death. The pain is extreme and well-documented. |
| **2. Frequency** | 5/5 | Patients take pills 1-4 times per day, every day. The problem occurs multiple times daily, 365 days a year. You can't get more frequent than this. |
| **3. Willingness to Pay** | 4/5 | Families pay for peace of mind. Apps like Medisafe have 50M+ downloads. Senior care is a $400B market. Families will pay $5-15/month. The missing point is that insurance doesn't cover reminder apps yet. |
| **4. Market Size** | 5/5 | 50M Americans over 65. 80% take daily prescriptions. Global elderly care market is $1.2T. Even a niche capture is massive. |
| **5. Competition** | 3/5 | Medisafe, PillPack (Amazon), MyTherapy all exist. But none focus on the family-alert loop via SMS. Differentiation is real but not unassailable. |
| **6. MVP Feasibility** | 4/5 | React Native + Firebase + Twilio SMS = buildable in 36 hours. The core loop (remind → track → alert) is straightforward. Hard part: HIPAA compliance at scale, but MVP doesn't need full compliance. |
| **7. Demo Wow Factor** | 4/5 | Two phones side by side — take a pill on one, see an alert on the other. Very visual. Judges can see the result instantly. Not a 3D render or a complex dashboard. |

### **Total: 30/35 (HIGH — Pursue this)**

**Verdict:** This scores HIGH. The pain is real, the market is huge, the MVP is buildable, and the demo is visual. The competition score keeps it from a perfect 35, but the family-alert differentiator is strong enough. **Build this.**

---

## Problem B: "StudySync — AI Study Group Matcher for College Students"

### The Idea
An app that matches college students into optimal study groups based on course, schedule, learning style, and GPA. Uses an AI matching algorithm to pair students who complement each other.

### The 7-Factor Scorecard

| Factor | Score | Reasoning |
|---|---|---|
| **1. Pain Intensity** | 2/5 | Studying alone is inconvenient, not painful. Nobody dies or loses money because they don't have a study group. Students can just text classmates. The pain is mild — more of a "nice to have." |
| **2. Frequency** | 3/5 | Students study for exams 2-3 times per semester per course. That's maybe 10-15 times per semester. Not daily. Not even weekly. Frequency is moderate at best. |
| **3. Willingness to Pay** | 1/5 | Students are the worst-paying demographic. They'll use free alternatives (group chats, Discord servers). Monetization path is unclear. Ad-supported? Students hate ads. Freemium? What's the premium feature? |
| **4. Market Size** | 3/5 | 20M college students in the US. Sounds big, but the addressable market is students who (a) don't already have study groups, (b) are willing to use an app for this, and (c) would pay for it. Realistic addressable: maybe 2M. |
| **5. Competition** | 2/5 | GroupMe, Discord, WhatsApp groups, campus Reddit. The "competition" isn't other apps — it's the existing behavior of texting "anyone studying for the final?" in a group chat. Very hard to displace. |
| **6. MVP Feasibility** | 4/5 | A matching algorithm is straightforward. Collect course, schedule, and learning style → run matching → display results. Technical MVP is buildable in 24 hours. But getting users to fill out profiles is the real challenge. |
| **7. Demo Wow Factor** | 2/5 | The demo is: fill out a form → see a list of matched students. Not very visual. Not very exciting. Judges would see a list of names and think "cool, but so what?" |

### **Total: 17/35 (MEDIUM — Needs Pivoting)**

**Verdict:** This scores MEDIUM. The core problem (lonely studying) is real but not intense enough to drive behavior change. The killer issue is willingness to pay (1/5) and competition from existing behavior (2/5). **How to pivot:**

- **Option 1:** Narrow the focus to a specific pain point. Instead of "study group matching," try "find a lab partner for your chemistry final tomorrow." That's urgent, specific, and solves a time-sensitive problem.
- **Option 2:** Add a revenue model that doesn't require student payment. Sell anonymized study pattern data to universities. Partner with textbook companies for sponsored recommendations.
- **Option 3:** Change the user. Instead of students, target tutors. "Find students who need help in your subject, in your area, at your rate." Tutors will pay for leads.

Without pivoting, this problem will leave you with a working app that nobody uses after the hackathon.

---

## Problem C: "CryptoPortfolio — Real-Time Multi-Chain Portfolio Tracker"

### The Idea
A dashboard that aggregates your crypto holdings across 15+ blockchains (Ethereum, Solana, Polygon, Arbitrum, etc.) and shows real-time portfolio value with P&L tracking and tax-loss harvesting suggestions.

### The 7-Factor Scorecard

| Factor | Score | Reasoning |
|---|---|---|
| **1. Pain Intensity** | 2/5 | Tracking crypto is annoying, not painful. Most crypto holders use CoinMarketCap or Zapper for free. The "pain" is having 5 tabs open instead of 1. Mild inconvenience. |
| **2. Frequency** | 3/5 | Crypto traders check portfolios daily, but passive holders check maybe weekly. Frequency varies wildly by user type. For the average holder, it's moderate. |
| **3. Willingness to Pay** | 2/5 | Free tools already exist (CoinMarketCap, Zapper, DeBank). Users expect this to be free. The few who pay ($10-20/month) are professional traders who already have tools they trust. |
| **4. Market Size** | 3/5 | ~300M crypto users globally. But most don't need a portfolio tracker — they use exchanges (Coinbase, Binance) that already show balances. Real addressable: maybe 10M users who self-custody across multiple chains. |
| **5. Competition** | 1/5 | Zapper, DeBank, CoinMarketCap Portfolio, Zerion, Rotki — all exist and are free. This is one of the most saturated spaces in crypto. You'd be building the 6th or 7th option. |
| **6. MVP Feasibility** | 2/5 | Aggregating data across 15+ chains requires 15+ API integrations, each with different formats. Real-time data requires WebSocket connections or constant polling. Tax-loss harvesting requires understanding tax law in multiple jurisdictions. This is a 3-month project, not a 36-hour hack. |
| **7. Demo Wow Factor** | 2/5 | The demo is a dashboard with numbers. Crypto judges have seen 50 dashboards this year. Nothing visual or novel. "Here's my portfolio balance" is not a demo — it's a spreadsheet. |

### **Total: 15/35 (LOW — Skip it)**

**Verdict:** This scores LOW. The competition is brutal (1/5), the MVP is too complex for a hackathon (2/5), and the wow factor is low (2/5). Even if you build it, judges will say "I can do this with Zapper for free." **Skip this problem entirely.**

**Why smart teams fall for this:**
- They're crypto enthusiasts and assume everyone cares about crypto
- The tech sounds cool (multi-chain aggregation!)
- They overestimate how unique their approach is
- They underestimate how good existing free tools already are

**The litmus test:** If you can describe your competitor in one sentence and it sounds like "it's like [existing tool] but for [niche]," you're in trouble. Judges will ask "why wouldn't I just use [existing tool]?" and you won't have a good answer.

---

## Quick Reference: What Each Score Range Means

| Score | Action |
|---|---|
| **28-35** | **BUILD IT.** Strong problem, clear path to demo, real market. Don't hesitate. |
| **20-27** | **PIVOT IT.** The core idea has merit but one or two factors are dragging it down. Reframe the problem, narrow the scope, or change the user. |
| **15-19** | **SKIP IT.** You're fighting uphill on too many fronts. Save your energy for a better problem. |
| **7-14** | **RUN.** This is either not a real problem or completely unbuildable at a hackathon. Move on immediately. |

---

## The Math Matters

Don't just eyeball the scores. Add them up. A problem that feels "pretty good" might actually score 19/35 when you're honest about competition and willingness to pay. Trust the system over your gut — your gut is biased toward ideas you personally find interesting, not ideas that win hackathons.
