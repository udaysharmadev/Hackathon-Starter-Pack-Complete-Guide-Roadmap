#!/usr/bin/env python3
"""
Stack Advisor — Answer 5 questions, get a hackathon stack recommendation.

Usage:
    python3 stack-advisor.py                 Interactive (5 questions)
    python3 stack-advisor.py --quick web-ai  Presets: web-ai, dashboard,
                                             realtime, python-ml, landing, mobile

Logic mirrors 05-tech-stack-chooser/README.md. Offline, stdlib only.
"""

import argparse

PRESETS = {
    "web-ai": {"label": "AI web app", "stack": "Next.js + API routes + OpenRouter/Gemini + Supabase → deploy on Vercel"},
    "dashboard": {"label": "Dashboard", "stack": "Next.js + Supabase + chart library → deploy on Vercel"},
    "realtime": {"label": "Realtime app", "stack": "Next.js + Supabase Realtime (or Firebase) → deploy on Vercel"},
    "python-ml": {"label": "Python/ML demo", "stack": "FastAPI + Supabase/Postgres + simple frontend → deploy API on Railway/Render"},
    "landing": {"label": "Landing + waitlist", "stack": "Next.js static or Cloudflare Pages + form backend (Supabase/Forms)"},
    "mobile": {"label": "Mobile app", "stack": "Expo (React Native managed) + Supabase/Firebase backend"},
}


def recommend(answers):
    """answers: dict with keys: app_type, realtime, python, mobile, familiar."""
    familiar = answers.get("familiar", "")
    if familiar:
        return (f"Stick with what you know: {familiar}. Rule from section 05 — "
                "never learn a new framework at a hackathon. Add only one new "
                "service (DB or AI API) on top."), "familiar"

    app_type = answers.get("app_type", "web")
    if answers.get("mobile") == "y":
        return PRESETS["mobile"]["stack"], "mobile"
    if app_type == "python-ml" or answers.get("python") == "y":
        return PRESETS["python-ml"]["stack"], "python-ml"
    if answers.get("realtime") == "y":
        return PRESETS["realtime"]["stack"], "realtime"
    if app_type in PRESETS:
        return PRESETS[app_type]["stack"], app_type
    return PRESETS["web-ai"]["stack"], "web-ai"


def interactive():
    print("\n  Stack Advisor — 5 questions\n")
    print("  App types: web-ai, dashboard, realtime, python-ml, landing, mobile")
    app_type = input("  1. App type [web-ai]: ").strip() or "web-ai"
    realtime = input("  2. Need realtime (chat/live)? (y/n) [n]: ").strip().lower() or "n"
    python = input("  3. Is the core logic Python/ML? (y/n) [n]: ").strip().lower() or "n"
    mobile = input("  4. Must it be a native mobile app? (y/n) [n]: ").strip().lower() or "n"
    familiar = input("  5. Stack your team already knows (blank = none): ").strip()

    rec, key = recommend({"app_type": app_type, "realtime": realtime,
                          "python": python, "mobile": mobile, "familiar": familiar})
    label = PRESETS.get(key, {}).get("label", "Recommendation")
    print(f"\n  Recommendation ({label}):\n  → {rec}\n")
    print("  Deploy early (section 10): frontend → Vercel, API → Railway/Render,")
    print("  data/auth → Supabase/Firebase. Add a backup URL + recording.\n")


def main():
    p = argparse.ArgumentParser(description="Recommend a hackathon stack.")
    p.add_argument("--quick", choices=sorted(PRESETS), help="Skip questions, use a preset")
    args = p.parse_args()
    if args.quick:
        print(f"{PRESETS[args.quick]['label']}: {PRESETS[args.quick]['stack']}")
        return
    interactive()


if __name__ == "__main__":
    main()
