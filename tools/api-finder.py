#!/usr/bin/env python3
"""
API Finder — Suggest hackathon APIs from a curated offline index.

Usage:
    python3 api-finder.py --need "realtime chat + auth"
    python3 api-finder.py --list-categories
    python3 api-finder.py                      Interactive mode

Matches against the categories documented in
06-free-apis-mega-list/api-database.md. Offline, stdlib only.
Always confirm free tier + limits on the official docs before building.
"""

import argparse
import sys

APIS = [
    {"name": "OpenRouter", "cats": ["ai", "llm", "chatbot", "text"], "use": "Multi-model LLM access via one API", "docs": "https://openrouter.ai"},
    {"name": "Gemini API", "cats": ["ai", "llm", "vision", "multimodal"], "use": "Multimodal AI (text/image)", "docs": "https://aistudio.google.com"},
    {"name": "Groq", "cats": ["ai", "fast", "realtime", "llm"], "use": "Ultra-fast LLM inference for live demos", "docs": "https://groq.com"},
    {"name": "Hugging Face Inference", "cats": ["ai", "ml", "ocr", "nlp", "vision"], "use": "Open ML models via hosted API", "docs": "https://huggingface.co"},
    {"name": "Supabase", "cats": ["db", "auth", "realtime", "backend", "postgres"], "use": "Postgres + auth + realtime + storage", "docs": "https://supabase.com"},
    {"name": "Firebase", "cats": ["db", "auth", "realtime", "backend", "hosting"], "use": "Auth + Firestore + hosting fast path", "docs": "https://firebase.google.com"},
    {"name": "Neon", "cats": ["db", "postgres", "sql"], "use": "Serverless Postgres", "docs": "https://neon.tech"},
    {"name": "MongoDB Atlas", "cats": ["db", "nosql"], "use": "Hosted NoSQL for flexible schemas", "docs": "https://mongodb.com"},
    {"name": "Clerk", "cats": ["auth", "login"], "use": "Drop-in auth UI + session", "docs": "https://clerk.com"},
    {"name": "Stripe", "cats": ["payments", "fintech", "billing"], "use": "Payments + payment links", "docs": "https://stripe.com"},
    {"name": "Razorpay", "cats": ["payments", "fintech", "india"], "use": "India-first payments", "docs": "https://razorpay.com"},
    {"name": "Twilio", "cats": ["sms", "voice", "notifications"], "use": "SMS/voice reminders", "docs": "https://twilio.com"},
    {"name": "SendGrid", "cats": ["email", "notifications"], "use": "Transactional email", "docs": "https://sendgrid.com"},
    {"name": "Cloudinary", "cats": ["media", "images", "upload"], "use": "Image upload + optimization", "docs": "https://cloudinary.com"},
    {"name": "Mapbox", "cats": ["maps", "geo", "location"], "use": "Maps + routing + geocoding", "docs": "https://mapbox.com"},
    {"name": "OpenWeather", "cats": ["weather", "data"], "use": "Current + forecast weather", "docs": "https://openweathermap.org"},
    {"name": "CoinGecko", "cats": ["crypto", "finance", "data"], "use": "Free crypto prices (no key for basic)", "docs": "https://coingecko.com"},
    {"name": "Alpha Vantage", "cats": ["stocks", "finance", "data"], "use": "Stock data (tight free limits — cache!)", "docs": "https://alphavantage.co"},
    {"name": "REST Countries", "cats": ["data", "geo", "utility"], "use": "Country data, no key needed", "docs": "https://restcountries.com"},
    {"name": "NASA APIs", "cats": ["data", "space", "gov"], "use": "Public space/satellite data", "docs": "https://api.nasa.gov"},
]

CATEGORIES = sorted({c for a in APIS for c in a["cats"]})


def find(need):
    tokens = [t.strip().lower() for t in need.replace("+", " ").replace(",", " ").split() if t.strip()]
    scored = []
    for api in APIS:
        hay = " ".join(api["cats"] + [api["name"].lower(), api["use"].lower()])
        score = sum(1 for t in tokens if t in hay)
        # partial matches
        score += sum(0.5 for t in tokens if any(t[:4] in c for c in api["cats"] if len(t) >= 4))
        if score > 0:
            scored.append((score, api))
    scored.sort(key=lambda x: -x[0])
    return [a for _, a in scored[:6]]


def main():
    p = argparse.ArgumentParser(description="Suggest hackathon APIs (offline index).")
    p.add_argument("--need", help="Describe what you need, e.g. 'realtime chat auth'")
    p.add_argument("--list-categories", action="store_true")
    args = p.parse_args()

    if args.list_categories:
        print("Categories: " + ", ".join(CATEGORIES))
        return

    need = args.need or input("What do you need? (e.g. 'auth + realtime chat'): ").strip()
    if not need:
        print("Describe your need, e.g. --need 'maps + sms reminders'")
        sys.exit(1)

    results = find(need)
    if not results:
        print("No matches. Try keywords like: ai, auth, db, realtime, maps, payments, sms, weather.")
        print("Categories: " + ", ".join(CATEGORIES))
        sys.exit(0)

    print(f"\nTop matches for: {need}\n")
    for i, a in enumerate(results, 1):
        print(f"  {i}. {a['name']} — {a['use']}")
        print(f"     Docs: {a['docs']}")
    print("\nFallback rule: cache one fixture response per API and add a")
    print("'Load sample data' button so the demo survives outages/rate limits.")
    print("Confirm free tier + limits on the official docs before you commit.")


if __name__ == "__main__":
    main()
