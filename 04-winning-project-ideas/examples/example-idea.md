# Example Idea Cards

Two fully fleshed-out project ideas ready for a hackathon. Each includes everything you need to start building immediately.

---

## Idea Card 1: "ClearTalk" — AI Meeting Summarizer for Remote Teams

### Problem Statement

Remote workers spend an average of 31 hours per month in meetings. 71% of those meetings are considered unproductive (Harvard Business Review). The biggest issue isn't the meetings themselves — it's that no one remembers what was decided, who's responsible for what, or what the follow-up actions are. Meeting notes exist, but they're inconsistent, incomplete, and usually abandoned after the first week.

### User Persona

**Name:** Sarah, 29
**Role:** Product Manager at a 40-person SaaS startup
**Context:** Runs 4-6 meetings per day across 3 time zones. Uses Zoom and Google Meet. Takes notes in Notion but often forgets. Her team frequently asks "what did we decide in yesterday's standup?" She spends 30 minutes after each meeting writing up notes that nobody reads.

**Pain level:** She's losing 2+ hours per week to post-meeting admin. Her team misses action items. Projects slip because "nobody was assigned that."

### MVP Scope (What You Build in 36 Hours)

**Core features (must-have):**
1. Connect to Zoom or Google Meet via API
2. Record and transcribe the meeting in real-time
3. Auto-generate: key decisions, action items (with assignees), and a 3-sentence summary
4. Display results on a clean web dashboard
5. Send summary via email to all participants

**Nice-to-have (if time allows):**
- Slack integration: post summary to a channel automatically
- Search across past meetings
- Highlight "open questions" that need follow-up

**Out of scope for MVP:**
- Support for 10+ participants
- Real-time collaborative editing
- Mobile app

### Tech Stack

| Layer | Technology | Why |
|---|---|---|
| Frontend | Next.js + Tailwind CSS | Fast to build, clean UI, easy deploy to Vercel |
| Backend | Next.js API routes | No separate backend needed for MVP |
| Database | Supabase (Postgres) | Free tier, real-time subscriptions, easy auth |
| AI/Transcription | Whisper API (OpenAI) | Best open-source transcription, $0.006/minute |
| Summarization | GPT-4o-mini | Fast, cheap ($0.15/1M input tokens), good at structured extraction |
| Meeting API | Zoom SDK / Google Meet API | OAuth-based, well-documented |
| Email | Resend | Free tier (3K emails/month), simple API |
| Auth | Clerk | Free for hackathons, Google SSO in 10 minutes |
| Hosting | Vercel | Free hobby tier, instant deploys |

### Architecture

```
User joins Zoom meeting
        ↓
Zoom webhook fires → your server
        ↓
Audio stream → Whisper API → transcript (JSON with timestamps)
        ↓
Transcript → GPT-4o-mini prompt → structured summary
        ↓
Summary → Supabase (stored) + Dashboard (displayed) + Resend (emailed)
```

### Demo Flow (90 seconds)

1. **Open the dashboard** → show a list of "past meetings" (pre-seeded demo data)
2. **Click "Start Live"** → join a mock Zoom call with 2 other team members
3. **Talk for 60 seconds** → "Should we launch the new pricing page next Tuesday or Thursday?"
4. **End the meeting** → show the dashboard updating in real-time
5. **Results appear:** Decision: Launch Thursday. Action: Sarah to finalize copy by Wednesday. Action: Dev team to deploy by Thursday 9am. Summary: Team aligned on Thursday launch pending copy and deployment readiness.
6. **Click "Send"** → show the email arriving in inbox with the formatted summary

**Key moment:** The AI correctly extracted "Thursday" as the decision, not "Tuesday or Thursday" (the options). That shows judges the AI actually understands context.

### Why This Wins

- **Real pain:** Every remote worker has felt this. Judges will personally relate.
- **Visual demo:** Live meeting → real-time transcription → auto-generated summary. Judges see it happening.
- **Measurable impact:** "Saves 2 hours per week per employee × 40 employees = 160 hours/month = $8,000/month at $50/hour average."
- **Clear monetization:** $10/user/month after free tier. Easy to explain to judges.
- **Not just another wrapper:** The real-time transcription + structured extraction is genuinely useful, not just "ChatGPT but for meetings."

### Risk Assessment

| Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|
| Zoom API rate limits during demo | Medium | High | Pre-record a backup transcript. Have the "live" flow as plan A, recorded data as plan B. |
| Whisper transcription errors | Low | Medium | Use a clear microphone. Pick a topic you know well so errors are obvious and fixable in post. |
| GPT-4o-mini hallucinates action items | Medium | Medium | Use a strict JSON schema in the prompt. Validate output has "decisions," "actions," and "summary" keys. |
| Vercel cold start delays | Low | Low | Keep the server warm by hitting the API every 5 minutes before demo. |

### Sponsor Alignment

- **Zoom:** Use their SDK → eligible for Zoom hackathon tracks
- **OpenAI:** Use Whisper + GPT → eligible for OpenAI hackathon tracks
- **Supabase:** Use their database → eligible for Supabase hackathon tracks
- **Vercel:** Deploy there → eligible for Vercel hackathon tracks

If the hackathon is sponsored by any of these companies, this project hits multiple sponsor tracks simultaneously.

---

## Idea Card 2: "CivicPulse" — Real-Time Community Issue Reporter for Local Government

### Problem Statement

Citizens report potholes, broken streetlights, graffiti, and other infrastructure issues through 311 systems. But the experience is broken: you call a phone number, wait on hold, describe the issue to a human, and never hear back. 40% of 311 reports in major cities go unacknowledged within 30 days (Brookings Institute). People stop reporting because they feel ignored. Meanwhile, cities spend $2.3B annually on 311 systems that don't work.

### User Persona

**Name:** Marcus, 34
**Role:** Rent-stabilized apartment tenant in Chicago
**Context:** There's a pothole on his block that's been growing for 3 months. He's called 311 twice — no response. His neighbor's been flooded because of a clogged storm drain. Nobody's coming. He wants to report it and track whether anyone actually fixes it. He also wants to see if his neighbors are reporting similar issues — maybe the whole block has drainage problems.

**Pain level:** He feels powerless. The system designed to help him doesn't work. He's considering just moving.

### MVP Scope (What You Build in 36 Hours)

**Core features (must-have):**
1. Photo upload + AI categorization (pothole, graffiti, broken light, etc.)
2. Auto-detect location via phone GPS
3. Generate a formatted 311 report (ready to copy-paste or auto-submit)
4. Public dashboard showing all reports in a neighborhood
5. Status tracking: reported → acknowledged → in progress → resolved

**Nice-to-have (if time allows):**
- Trend heatmap: "12 reports of flooding in your zip code this month"
- City council member auto-email based on district
- Community upvoting: "I also see this issue"

**Out of scope for MVP:**
- Direct API integration with actual 311 systems (varies by city)
- User accounts or authentication
- Mobile app (responsive web only)

### Tech Stack

| Layer | Technology | Why |
|---|---|---|
| Frontend | Next.js + Tailwind + Mapbox | Map-based UI is essential. Mapbox has a free tier (50K loads/month) |
| Backend | Next.js API routes | Keeps it simple |
| Database | Supabase (Postgres + PostGIS) | PostGIS enables spatial queries ("show reports near me") |
| Image Analysis | Google Cloud Vision API | Free tier: 1K requests/month. Detects and categorizes images automatically |
| Hosting | Vercel | Free, fast, instant |
| Auth | Clerk (anonymous mode) | Optional — users don't need accounts to report |
| Email | Resend | For city council auto-emails |

### Architecture

```
User opens app → sees map of their neighborhood
        ↓
User taps "Report Issue" → takes photo → GPS auto-fills location
        ↓
Image → Google Cloud Vision → categorized as "pothole"
        ↓
Report saved to Supabase with: photo, location, category, timestamp
        ↓
Dashboard shows: all reports near user, trend data, status updates
        ↓
(Optional) City council email auto-generated with formatted report
```

### Demo Flow (90 seconds)

1. **Open the dashboard** → show a map of a real neighborhood with 8-10 pre-seeded reports (potholes, broken lights, graffiti)
2. **Tap "New Report"** → take a photo of a cracked sidewalk (or use a test photo on your phone)
3. **Watch the AI categorize it** → "Detected: Sidewalk damage. Confidence: 94%."
4. **Location auto-fills** → "1234 N. State Street, Ward 42"
5. **Show the public dashboard** → "47 issues reported in this ward this month. 12 are potholes. 3 are broken lights. Average resolution time: 45 days."
6. **Show the trend** → "Pothole reports up 340% since January. City has resolved 2 of 12."
7. **Show the city council email** → "Auto-generated email to Alderman Smith with all 12 pothole reports, photos, and locations. Ready to send."

**Key moment:** The trend data. Judges will see that this isn't just a reporting tool — it's a transparency tool. Cities can't ignore problems when the data is public and visual.

### Why This Wins

- **Civic impact:** Judges love projects that improve democracy and community engagement. This isn't a toy — it's infrastructure.
- **Visual demo:** A map with colored pins, trend charts, and photo-based reports. Very visual. Judges can see the problem and the solution simultaneously.
- **Data-driven story:** "47 issues reported, 2 resolved" is a headline. This project tells a story with numbers.
- **Real adoption potential:** Cities are legally required to respond to 311 reports. This tool makes that process transparent and trackable. A alderman or city council member could adopt this immediately.
- **Not just an app:** It's a platform. Once multiple people in a neighborhood report issues, the data becomes a tool for community organizing. That's a story judges remember.

### Risk Assessment

| Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|
| Google Cloud Vision misidentifies images | Medium | Medium | Use clear, well-lit photos. Have a manual category fallback (dropdown). |
| Mapbox free tier exceeded during demo | Low | High | Use Leaflet + OpenStreetMap as a free fallback (no API key needed). |
| Judges ask "why not just use 311?" | High | High | Lead with the data transparency angle. "311 tells you to call. We tell you the whole neighborhood has the same problem." |
| No real city data for demo | Medium | Medium | Seed with real 311 data from Chicago's open data portal (data.cityofchicago.org) — it's public and free. |

### Sponsor Alignment

- **Google Cloud:** Use Cloud Vision API → eligible for Google hackathon tracks
- **Mapbox:** Use their map SDK → eligible for Mapbox hackathon tracks
- **Supabase:** Use PostGIS → eligible for Supabase hackathon tracks
- **Open source angle:** If the hackathon values open source, this project naturally fits — cities can self-host it

This project also aligns with themes of: social impact, sustainability, smart cities, and government innovation. Many hackathons have specific tracks for these.

---

## How to Pick Between These Two

| If the hackathon is... | Build... |
|---|---|
| AI/ML focused | ClearTalk |
| Social impact / civic tech | CivicPulse |
| Sponsored by Zoom or OpenAI | ClearTalk |
| Sponsored by Google | Either (both use Google APIs) |
| No specific theme | ClearTalk (easier demo, more universal pain) |
| In a city with known 311 issues | CivicPulse (local relevance wins) |
| 24 hours or less | ClearTalk (simpler scope) |
| 48 hours | CivicPulse (more time for data seeding and map polish) |
