#!/usr/bin/env python3
"""
Idea Scorer — Score hackathon ideas against a 7-factor rubric.

Usage:
    python3 idea-scorer.py                    Interactive scoring
    python3 idea-scorer.py --name "My Idea"   Score with name

Scoring dimensions (1-5 each, max 35):
    1. Pain Score — How painful is this problem? (1 = minor inconvenience, 5 = critical need)
    2. Frequency — How often does the problem occur? (1 = rare, 5 = daily)
    3. Urgency — How urgently does it need solving? (1 = can wait, 5 = must fix now)
    4. Clarity — How clear is the problem statement? (1 = vague, 5 = crystal clear)
    5. Buildability — Can you build an MVP in time? (1 = impossible, 5 = easy)
    6. Demo Strength — Will the demo impress judges? (1 = boring, 5 = jaw-dropping)
    7. Judge Appeal — Will judges care about this? (1 = niche, 5 = universal)

Decision thresholds:
    28-35: 🔥 STRONG — Pursue this idea
    20-27: 🟡 GOOD — Refine and strengthen
    13-19: 🟠 WEAK — Consider pivoting
    7-12:  🔴 SKIP — Not worth the time
"""

import sys


RUBRIC = {
    "pain_score": {
        "name": "Pain Score",
        "description": "How painful is this problem?",
        "levels": {
            1: "Minor inconvenience — nice to have",
            2: "Moderate annoyance — people complain sometimes",
            3: "Significant pain — people actively look for solutions",
            4: "Severe pain — people have tried and failed to solve this",
            5: "Critical need — people are paying for bad solutions"
        }
    },
    "frequency": {
        "name": "Frequency",
        "description": "How often does the problem occur?",
        "levels": {
            1: "Rare — once a year or less",
            2: "Occasional — monthly",
            3: "Regular — weekly",
            4: "Frequent — daily",
            5: "Constant — multiple times per day"
        }
    },
    "urgency": {
        "name": "Urgency",
        "description": "How urgently does it need solving?",
        "levels": {
            1: "Can wait — no deadline pressure",
            2: "Mild urgency — eventually needs fixing",
            3: "Moderate — should be solved soon",
            4: "High — people are frustrated now",
            5: "Critical — must fix immediately"
        }
    },
    "clarity": {
        "name": "Clarity",
        "description": "How clear is the problem statement?",
        "levels": {
            1: "Vague — hard to explain in one sentence",
            2: "Somewhat clear — needs context",
            3: "Clear — most people understand it",
            4: "Very clear — obvious to everyone",
            5: "Crystal clear — anyone gets it in 5 seconds"
        }
    },
    "buildability": {
        "name": "Buildability",
        "description": "Can you build an MVP in the time available?",
        "levels": {
            1: "Impossible — months of work needed",
            2: "Very hard — needs a full team and weeks",
            3: "Possible — needs focused effort",
            4: "Easy — can build core features in a day",
            5: "Trivial — can build and polish in hours"
        }
    },
    "demo_strength": {
        "name": "Demo Strength",
        "description": "Will the demo impress judges?",
        "levels": {
            1: "Boring — hard to show visually",
            2: "Mild — some visual elements",
            3: "Good — clear visual demonstration",
            4: "Strong — judges will say 'wow'",
            5: "Jaw-dropping — judges will remember this"
        }
    },
    "judge_appeal": {
        "name": "Judge Appeal",
        "description": "Will judges care about this?",
        "levels": {
            1: "Niche — only experts care",
            2: "Limited — small audience",
            3: "Moderate — relevant to many",
            4: "High — judges will relate",
            5: "Universal — everyone cares"
        }
    }
}


def score_idea(name=None):
    """Interactively score an idea."""
    if not name:
        name = input("\n  Idea name: ").strip()
        if not name:
            print("  Name is required.")
            return

    description = input("  One-line description: ").strip()

    print(f"\n  Scoring: {name}")
    print(f"  Description: {description}\n")

    scores = {}
    total = 0

    for key, rubric in RUBRIC.items():
        print(f"  {rubric['name']}: {rubric['description']}")
        for level, desc in rubric["levels"].items():
            print(f"    {level} — {desc}")

        while True:
            try:
                score = int(input(f"  Your score (1-5): "))
                if 1 <= score <= 5:
                    scores[key] = score
                    total += score
                    break
                else:
                    print("  Please enter 1-5.")
            except ValueError:
                print("  Please enter a number.")

        print()

    # Decision
    if total >= 28:
        verdict = "🔥 STRONG — Pursue this idea!"
        color = "green"
    elif total >= 20:
        verdict = "🟡 GOOD — Refine and strengthen"
        color = "yellow"
    elif total >= 13:
        verdict = "🟠 WEAK — Consider pivoting"
        color = "orange"
    else:
        verdict = "🔴 SKIP — Not worth the time"
        color = "red"

    print("  " + "=" * 50)
    print(f"\n  📊 SCORE: {total}/35\n")
    print(f"  {verdict}\n")

    print("  Breakdown:")
    for key, rubric in RUBRIC.items():
        bar = "█" * scores[key] + "░" * (5 - scores[key])
        print(f"    {rubric['name']:<15} {bar} {scores[key]}/5")

    print()

    # Weakest areas
    weakest = sorted(scores.items(), key=lambda x: x[1])[:2]
    print("  💡 Weakest areas to improve:")
    for key, score in weakest:
        print(f"    - {RUBRIC[key]['name']}: {RUBRIC[key]['levels'][score]}")

    print()
    return total, scores


def main():
    if len(sys.argv) > 2 and sys.argv[1] == "--name":
        score_idea(" ".join(sys.argv[2:]))
    elif len(sys.argv) > 1 and not sys.argv[1].startswith("--"):
        score_idea(" ".join(sys.argv[1:]))
    else:
        print(__doc__)
        while True:
            again = input("\n  Score another idea? (y/n): ").strip().lower()
            if again != "y":
                break
            score_idea()


if __name__ == "__main__":
    main()
