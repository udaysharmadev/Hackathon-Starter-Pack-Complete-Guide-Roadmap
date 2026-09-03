# API Selector — Find the Right Free APIs for Your Hackathon

Stop guessing. Answer these questions and you'll know exactly which APIs to wire up.

## Quick Decision Matrix (25 Scenarios)

| # | If your project... | You need... | Use these APIs |
|---|---|---|---|
| 1 | Generates text or answers questions | AI/LLM | OpenAI (free trial), Gemini (free tier), Cohere (free) |
| 2 | Shows a map or location | Maps | Leaflet + OpenStreetMap (always free), Mapbox (100K free) |
| 3 | Sends emails or SMS | Notifications | Resend (3K/mo), SendGrid (100/day), Twilio (trial credit) |
| 4 | Has user accounts | Auth | Clerk (10K MAU), Supabase Auth (50K MAU), Auth0 (7K free) |
| 5 | Stores user data | Database | Supabase (500MB), PlanetScale (5GB), Turso (500 rows free) |
| 6 | Handles images or video | Media | Cloudinary (25GB), imgix (100GB), Mux (free trial) |
| 7 | Processes payments | Payments | Stripe (no monthly fee), Lemon Squeezy (built for SaaS) |
| 8 | Searches content | Search | Algolia (10K searches/mo), Typesense Cloud (8K free) |
| 9 | Analyzes images | Vision AI | Google Cloud Vision (1K/mo free), Clarifai (1K ops/mo) |
| 10 | Converts speech to text | Audio | Whisper API (OpenAI, pay-per-use), Deepgram (free tier) |
| 11 | Sends push notifications | Push | Firebase Cloud Messaging (free), OneSignal (10K free) |
| 12 | Needs real-time data | Realtime | Supabase Realtime (free), Pusher (200K messages/day) |
| 13 | Tracks analytics | Analytics | PostHog (1M events/mo free), Plausible (30-day trial) |
| 14 | Needs file storage | Storage | Supabase Storage (1GB), Cloudflare R2 (10GB free) |
| 15 | Handles scheduling | Calendar | Google Calendar API (free), Nylas (free tier) |
| 16 | Scrapes or fetches data | Web scraping | Firecrawl (500 pages/mo free), ScraperAPI (5K free) |
| 17 | Needs translation | i18n | Google Translate API (500K chars/mo free), LibreTranslate (self-hosted) |
| 18 | Generates PDFs | PDF | Puppeteer (free), React-PDF (free), docspal (free API) |
| 19 | Connects social accounts | Social OAuth | GitHub OAuth (free), Google OAuth (free), Discord OAuth (free) |
| 20 | Needs a chat feature | Chat | Stream Chat (1K MAU free), Ably (6M messages/mo free) |
| 21 | Requires QR codes | QR | `qrcode` npm package (local, no API needed) |
| 22 | Needs currency conversion | Finance | ExchangeRate-API (1.5K/mo free), frankfurter.app (free) |
| 23 | Displays weather data | Weather | OpenWeatherMap (1K/day free), wttr.in (free, no key) |
| 24 | Needs stock data | Finance | Alpha Vantage (25/day free), Yahoo Finance (yfinance, no key) |
| 25 | Requires authentication tokens | JWT | jsonwebtoken (free npm lib), jose (free npm lib) |

## API Combination Recipes

These are proven combos. Copy the pattern.

```
Recipe: AI + Maps + Auth = Smart Location App
- Clerk (auth) → identify users
- Gemini (AI) → process user queries
- Leaflet + OSM (maps) → display location results
- Supabase (DB) → save search history

Recipe: Auth + Database + Realtime = Collaborative Tool
- Supabase Auth → user accounts
- Supabase Database → store data
- Supabase Realtime → live sync between users
- No extra API needed — Supabase handles all three

Recipe: AI + Media + Storage = Content Generator
- Cloudinary (media) → upload/process images
- OpenAI (AI) → generate text captions
- Supabase Storage → persist results
- Resend (email) → send finished content to user

Recipe: Auth + Payments + Notifications = SaaS Starter
- Clerk (auth) → login
- Stripe (payments) → subscriptions
- Resend (email) → receipts and alerts
- Firebase FCM (push) → in-app notifications

Recipe: Search + AI + Realtime = Live Knowledge Base
- Algolia (search) → instant search
- Cohere (AI) → rerank results with AI
- Ably (realtime) → live updates as docs change
```

## What You Need → What to Use

| Need | Best Free Option | Runner-Up | Why not the others? |
|---|---|---|---|
| User login | Supabase Auth | Clerk | Firebase Auth locks you into Google ecosystem |
| Database | Supabase | PlanetScale | Turso is SQLite-based, limits complex queries |
| File storage | Cloudinary | Supabase Storage | Cloudinary auto-optimizes images for you |
| Email | Resend | SendGrid | Resend is simpler; SendGrid dashboard is painful |
| AI text | Gemini | OpenAI | Gemini free tier is more generous right now |
| Maps | Leaflet + OSM | Mapbox | Leaflet is fully free; Mapbox hits limits at 100K |
| Payments | Stripe | Lemon Squeezy | Stripe is industry standard; Lemon Squeezy is newer |
| Realtime | Supabase Realtime | Pusher | Supabase is integrated; Pusher is standalone |
| Search | Algolia | Meilisearch (self-host) | Algolia has best DX; Meilisearch is free but self-hosted |
| Push notifications | Firebase FCM | OneSignal | FCM is free forever; OneSignal adds branding |

## Free Tier Comparison (Head-to-Head)

### Auth Providers

| Provider | Free MAU | Social Logins | MFA | Custom Domain |
|---|---|---|---|---|
| Supabase Auth | 50,000 | Unlimited | Yes | Yes |
| Clerk | 10,000 | Unlimited | Yes | Yes |
| Auth0 | 7,000 | Unlimited | Yes | No |
| Firebase Auth | Unlimited* | 3 providers | Paid | Yes |

*Firebase Auth is free but charges after 50K identity platform reads.

### Databases

| Provider | Free Storage | Max Rows | API Type | Good For |
|---|---|---|---|---|
| Supabase | 500MB | Unlimited | REST + Realtime | Full-stack apps |
| PlanetScale | 5GB | Unlimited | SQL | Complex schemas |
| Turso | 500 rows | 500 | SQL (edge) | Low-latency reads |
| Neon | 512MB | Unlimited | Postgres | Postgres-native apps |
| MongoDB Atlas | 512MB | Unlimited | Document | Flexible schemas |

### AI Providers

| Provider | Free Credits/Requests | Rate Limit | Best For |
|---|---|---|---|
| OpenAI | $5 credit (3 months) | 3 RPM (tier 0) | GPT-4 access |
| Gemini | 15 RPM, 1M tokens/day | Very generous | High-volume apps |
| Cohere | 100 calls/month | Low | Reranking, search |
| Mistral | 1 request/second | Moderate | Fast inference |

## Your Selection Worksheet

Copy this and fill it in:

```
My project idea: ___________________________

Must-have capabilities:
[ ] Auth (users)
[ ] Database (storage)
[ ] AI (intelligence)
[ ] Maps (location)
[ ] Email/notifications
[ ] Payments
[ ] Media (images/video)
[ ] Realtime (live updates)
[ ] Search
[ ] Other: ___________

Selected APIs:
1. _____________ for _____________
2. _____________ for _____________
3. _____________ for _____________
4. _____________ for _____________
5. _____________ for _____________

Total free tier budget check:
- API 1: _____ calls/month free
- API 2: _____ calls/month free
- API 3: _____ calls/month free
- Will I hit limits during demo?  YES / NO
```

## Red Flags to Watch For

- **"Free tier requires credit card"** — Stripe, Vercel, and AWS all do this. Have one ready but set spending alerts.
- **"Rate limited to X requests/minute"** — If your demo makes 50 API calls in 10 seconds, check the rate limit first.
- **"Free tier expires after 12 months"** — Some AWS/GCP services do this. Pick services with permanent free tiers.
- **"No serverless support"** — Some APIs require a backend proxy. If you're frontend-only, pick APIs with browser-friendly keys.
