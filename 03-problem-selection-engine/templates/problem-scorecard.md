# Problem Scorecard

Rate each dimension 1–5. Multiply by the weight. Total the weighted scores. Pick the problem with the highest total.

---

## Scoring Rubric

### Pain Score (Weight: 2x)
How badly does this problem hurt the user?

| Score | What it means |
|-------|---------------|
| 1 | "That's annoying, I guess" — minor inconvenience |
| 2 | People complain about it occasionally |
| 3 | Regular frustration, people work around it |
| 4 | Significant pain, current solutions are terrible |
| 5 | "I'd pay money RIGHT NOW to fix this" — crushing pain |

### Frequency (Weight: 1.5x)
How often does the user hit this problem?

| Score | What it means |
|-------|---------------|
| 1 | Once a year or less (birthday problem) |
| 2 | A few times a month |
| 3 | Weekly — it's a regular nuisance |
| 4 | Daily — it's part of the routine |
| 5 | Multiple times per day — constant friction |

### Urgency (Weight: 1.5x)
Does the user need this fixed NOW or can it wait?

| Score | What it means |
|-------|---------------|
| 1 | "Nice to have" — could wait forever |
| 2 | Would fix it this month if available |
| 3 | Would fix it this week |
| 4 | Needs it today or tomorrow |
| 5 | Emergency — broken right now, blocking everything |

### Clarity (Weight: 1x)
How well can you explain this problem in one sentence?

| Score | What it means |
|-------|---------------|
| 1 | "It's complicated, let me explain..." — needs 5 minutes |
| 2 | Takes a paragraph to describe |
| 3 | One clear sentence, but needs context |
| 4 | One sentence, anyone gets it |
| 5 | One tweet — instantly obvious to everyone |

### Buildability (Weight: 2x)
Can you actually build this in the hackathon timeframe?

| Score | What it means |
|-------|---------------|
| 1 | Impossible — needs months of research |
| 2 | Hard — you'd need a PhD or a lot of infrastructure |
| 3 | Doable but tight — you'd need to cut corners |
| 4 | Comfortable — you can build a solid MVP |
| 5 | Easy — you could build it in your sleep |

### Demo Strength (Weight: 2x)
How visually compelling is this project when shown to judges?

| Score | What it means |
|-------|---------------|
| 1 | Terminal output only — hard to explain |
| 2 | Basic UI but not exciting |
| 3 | Decent UI, clear user flow |
| 4 | Beautiful demo, "wow" moment in first 30 seconds |
| 5 | Spectacular — judges will remember this tomorrow |

### Sponsor Fit (Weight: 1.5x)
How well does this project use the sponsor's API or platform?

| Score | What it means |
|-------|---------------|
| 1 | Doesn't use the sponsor's tech at all |
| 2 | Uses it as an add-on, not core |
| 3 | Reasonably integrated — sponsor would notice |
| 4 | Sponsor's tech is central to the solution |
| 5 | "Built for us" — couldn't exist without the sponsor's platform |

### Judge Appeal (Weight: 1x)
How much will judges care about this problem?

| Score | What it means |
|-------|---------------|
| 1 | Niche problem, judges won't relate |
| 2 | Some judges might care |
| 3 | Broad appeal — most judges get it |
| 4 | Judges will nod along — universal problem |
| 5 | Judges will want to use it themselves |

---

## Weighted Calculation Formula

**Total = (Pain × 2) + (Frequency × 1.5) + (Urgency × 1.5) + (Clarity × 1) + (Buildability × 2) + (Demo Strength × 2) + (Sponsor Fit × 1.5) + (Judge Appeal × 1)**

**Maximum possible score: 100**
**Minimum possible score: 11.5**

### Decision Thresholds

| Score Range | Verdict | Action |
|-------------|---------|--------|
| 75–100 | Strong idea | Build it. No second-guessing. |
| 60–74 | Good idea | Proceed, but watch for weak spots |
| 45–59 | Mediocre | Pivot or combine with another idea |
| 30–44 | Weak | Abandon this and brainstorm more |
| Below 30 | Bad idea | Run, don't walk |

### Red Flags (Automatic Dealbreakers)

Even if your score is high, watch out:
- **Buildability ≤ 2**: You probably can't finish it. Doesn't matter how good the idea is.
- **Demo Strength ≤ 2**: Judges won't "get it." Your demo is your lifeline.
- **Pain Score ≤ 2**: You're solving a problem nobody has. Pivot.
- **Sponsor Fit ≤ 1**: You'll lose sponsor prizes. Not worth it if sponsor tracks are the main prize pool.

---

## Filled Example Scorecard

**Problem: "Students waste 2 hours/week finding and applying to hackathons"**

| Dimension | Raw (1–5) | Weight | Weighted |
|-----------|-----------|--------|----------|
| Pain Score | 4 | 2x | 8.0 |
| Frequency | 4 | 1.5x | 6.0 |
| Urgency | 3 | 1.5x | 4.5 |
| Clarity | 5 | 1x | 5.0 |
| Buildability | 4 | 2x | 8.0 |
| Demo Strength | 4 | 2x | 8.0 |
| Sponsor Fit | 3 | 1.5x | 4.5 |
| Judge Appeal | 4 | 1x | 4.0 |
| **TOTAL** | | | **48.0** |

**Verdict: Mediocre — but Buildability and Demo Strength are strong. Consider combining with another idea or pivoting to a different angle on the same problem.**

---

## Decision Matrix (Idea Comparison)

| Idea | Pain | Freq | Urgent | Clear | Build | Demo | Sponsor | Judge | **Total** |
|------|------|------|--------|-------|-------|------|---------|-------|-----------|
| Hackathon finder | 4 | 4 | 3 | 5 | 4 | 4 | 3 | 4 | **48.0** |
| Meal prep for devs | 3 | 5 | 2 | 5 | 4 | 3 | 2 | 3 | **35.5** |
| Code review bot | 4 | 4 | 4 | 4 | 3 | 4 | 5 | 4 | **49.5** |
| Fake news detector | 5 | 3 | 5 | 3 | 2 | 5 | 3 | 5 | **43.0** |

**Winner: Code review bot — highest score, strong sponsor fit, easy to demo.**

---

## How to Use This

1. Write 3–5 problem ideas at the top
2. Fill out one scorecard per idea (takes ~5 minutes each)
3. Compare totals in the Decision Matrix
4. Pick the winner — don't overthink it
5. If two ideas are within 5 points, pick the one with higher Buildability

*The best hackathon project is the one you actually ship, not the one with the highest theoretical score.*
