#!/usr/bin/env python3
"""
README Generator — Answer questions, get a judge-ready README.md.

Usage:
    python3 readme-generator.py                    Interactive, prints to stdout
    python3 readme-generator.py --out README_NEW.md  Write to file

Covers what judges check (section 13): problem, demo, live link, setup,
screenshots, tech, team. Stdlib only.
"""

import argparse
import datetime

TEMPLATE = """# {name}

> {oneline}

**Live demo:** {live_url}
**Demo login (if needed):** `{demo_login}`
**Video (60-90s backup):** {video_url}

## Problem

{problem}

## What it does

{what}

## Demo script (90 seconds)

1. {step1}
2. {step2}
3. {step3}

## Tech stack

- {stack}

## Run locally

```bash
{setup}
```

## Screenshots

| Screen | Image |
|---|---|
| Main flow | `assets/screenshot-1.png` |
| Result | `assets/screenshot-2.png` |

## Team

{team}

## What's next

- {next1}
- {next2}

---
_Generated with tools/readme-generator.py on {date}. See 13-github-for-hackathons/ for the full checklist._
"""


def ask(prompt, default=""):
    suffix = f" [{default}]" if default else ""
    val = input(f"  {prompt}{suffix}: ").strip()
    return val or default


def main():
    p = argparse.ArgumentParser(description="Generate a hackathon README.")
    p.add_argument("--out", help="Write output to file instead of stdout")
    args = p.parse_args()

    print("\n  README Generator — fill 10 fields (Enter = keep default/blank)\n")
    data = {
        "name": ask("Project name", "My Hackathon Project"),
        "oneline": ask("One-liner (user + problem + solution)", "A tool that saves time on X"),
        "live_url": ask("Live URL", "https://yourproject.vercel.app"),
        "demo_login": ask("Demo login", "demo@hack.local / demo1234"),
        "video_url": ask("Backup video URL", "(add after recording)"),
        "problem": ask("Problem (2-3 sentences)", "Who wastes what on what, and why current fixes fail."),
        "what": ask("What it does (2-3 sentences)", "Core loop: input → action → result."),
        "step1": ask("Demo step 1", "Open the live URL (already logged in as demo user)"),
        "step2": ask("Demo step 2", "Run the golden-path action with seeded data"),
        "step3": ask("Demo step 3", "Show the result + impact"),
        "stack": ask("Stack", "Next.js + Supabase + Vercel"),
        "setup": ask("Setup commands (use \\n for new lines)", "npm install\\nnpm run dev"),
        "team": ask("Team (names + roles)", "Name — build, Name — design/pitch"),
        "next1": ask("Next step 1", "Harden auth + validation"),
        "next2": ask("Next step 2", "Pilot with 10 real users"),
        "date": datetime.date.today().isoformat(),
    }
    data["setup"] = data["setup"].replace("\\n", "\n")

    out = TEMPLATE.format(**data)
    if args.out:
        with open(args.out, "w") as f:
            f.write(out)
        print(f"\n  Wrote {args.out}\n")
    else:
        print("\n" + out)


if __name__ == "__main__":
    main()
