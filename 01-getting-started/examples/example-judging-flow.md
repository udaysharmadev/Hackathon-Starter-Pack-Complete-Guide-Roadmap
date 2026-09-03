# Example Judging Flow: "MediTrack" — A Pharmacy Reminder App

This is a real walkthrough of how a team won 2nd place at a 200-person health-tech hackathon. We'll follow them from pitch to Q&A.

---

## The Project

**MediTrack** is a mobile app that reminds elderly patients to take their medications on time and alerts a family member if a dose is missed. Built in 36 hours with React Native, Firebase, and Twilio SMS.

---

## Stage 1: The Problem (30 seconds)

The team opened with this exact line:

> "Every year, 125,000 Americans die because they don't take their medications correctly. That's not a drug problem — it's a reminder problem."

They didn't start with their tech. They started with a number. Judges immediately leaned in. One judge later said, "I was hooked at 125,000."

**What they did right:** One sentence. One shocking stat. No jargon. No "we built an app that...".

**What they would change:** They wish they'd added a 5-second personal story — like "My grandma nearly ended up in the ER last year because she doubled up on blood pressure meds."

---

## Stage 2: The Live Demo (90 seconds)

They ran a live demo with this exact flow:

1. **Opened the app** as "Grandma Rose" — showed a clean home screen with today's pills listed
2. **Tapped "Take Now"** on a pill — checked off instantly, UI updated with a green checkmark
3. **Waited 10 seconds** — showed a push notification appearing on a second phone (the "family member" device): "Grandma Rose missed her 2pm Lisinopril"
4. **Showed the SMS fallback** — the family member also got a text via Twilio: "ALERT: Missed dose. Tap to call Grandma."
5. **Showed the dashboard** — a simple chart showing adherence over the past week (85% compliance)

The entire demo took 90 seconds. Judges could see both phones. No slides. No code. Just the product working.

**What they did right:** They used two physical phones side by side. Judges could see the cause-and-effect in real time. The SMS fallback was a killer feature because it showed they thought about users without smartphones.

**What they would change:** The notification took 10 seconds instead of the expected 3. They should've pre-sent a test notification before going on stage. A 10-second dead air moment kills momentum.

---

## Stage 3: Why Current Solutions Are Painful (45 seconds)

They showed three screenshots:

1. **Pill organizer boxes** — "These don't remind you. They just organize the problem."
2. **Pharmacy apps like Medisafe** — "These are great for tech-savvy users. But my 82-year-old grandma can't set one up."
3. **Phone alarms** — "No tracking. No accountability. If she misses it, nobody knows."

Key line: "Existing solutions assume the patient is the problem. We assume the communication gap is the problem."

**What they did right:** They acknowledged competitors instead of pretending they were the first to think of this. Then they differentiated cleanly: "We're not replacing Medisafe. We're filling the gap Medisafe ignores — the family connection."

**What they would change:** They spent too long on the pill organizer joke. Should've cut it to 10 seconds and given more time to the Medisafe comparison.

---

## Stage 4: The Key Improvement (45 seconds)

They showed a single slide with three metrics:

| Metric | Competitors | MediTrack |
|---|---|---|
| Setup time | 10-15 min | 45 seconds |
| Missed dose alert | None / push only | SMS + push + family call |
| Tech required | Smartphone app | Works on basic phone via SMS |

Then they said: "We reduced setup from 15 minutes to 45 seconds by letting the doctor's office pre-configure everything. The patient just scans a QR code on their prescription bottle."

**What they did right:** One slide. Three numbers. The comparison was visual and immediate. Judges didn't have to do mental math.

**What they would change:** They should've shown the QR code scan live. A 5-second live action of scanning a bottle and seeing it populate would've been more powerful than the slide.

---

## Stage 5: Impact, Adoption, and Future (45 seconds)

They closed with:

> "There are 50 million Americans over 65. 80% take at least one prescription daily. If we capture just 1% of that market in year one, that's 400,000 patients — and a potential $4.8M ARR at $1/month per family plan."

Then they showed their adoption roadmap:
- **Month 1-3:** Partner with 2 senior living facilities in their city (they already had letters of intent)
- **Month 4-6:** Integrate with Epic (the largest EHR system) via FHIR API
- **Month 7-12:** Scale to 50 facilities through a pharmacy distribution deal

They ended with: "We're not just building an app. We're building the communication layer between patients, families, and pharmacies."

**What they did right:** They had real numbers, not虚构的 (fabricated) projections. The letters of intent from actual facilities showed traction. The Epic integration showed they understood the healthcare ecosystem.

**What they would change:** They'd add a one-line demo video playing behind them during this section — just the app running on loop — to keep visual interest while talking numbers.

---

## The Q&A (2 minutes)

Judge 1: "What's your HIPAA compliance story?"
**Their answer:** "We're using Firebase with encryption at rest and in transit. We're not storing any medical records — just medication names and schedules. We're consulting with a healthcare compliance attorney this week to confirm our classification."
**Score:** Solid. They didn't fake knowledge. They showed they were actively working on it.

Judge 2: "Why wouldn't a family just set up phone reminders?"
**Their answer:** "They can. But there's no tracking. If Mom says she took her pill, you have to trust her. With MediTrack, you see the data. And if she misses one, you get a text within 2 minutes — not a phone call at 9pm asking 'did you take your meds?'"
**Score:** Great. They acknowledged the simple alternative and showed why their approach added value beyond it.

Judge 3: "What's your unfair advantage?"
**Their answer:** "One team member's mom runs a senior living facility with 200 residents. We have a built-in test group and a distribution channel. We're not theorizing about users — we have 12 residents already testing our prototype on paper."
**Score:** This won them the 2nd place spot. Real users. Real access. Not hypothetical.

---

## What They Would Do Differently (Full Retrospective)

1. **Start with the story, not the stat.** Lead with "My grandma almost ended up in the ER." The stat comes second.
2. **Pre-test the demo.** Run the notification 5 minutes before going on stage so there's no 10-second delay.
3. **Show, don't tell the QR code.** Do a live scan on stage. 5 seconds. Huge impact.
4. **Cut 15 seconds from the competitor section.** Give it to the QR demo or a patient testimonial video.
5. **End with a patient quote, not a market size.** End emotionally, not financially. Let the judge's last thought be "this matters," not "this could make money."

---

## Key Takeaway

The winning formula wasn't the tech. It was: **problem → live demo → why it's broken now → your fix → real-world traction**. Every section had one clear point. Nothing was repeated. The demo was visual. The numbers were real. The Q&A was honest.

You don't need to be a senior engineer to win. You need to be a clear communicator with a working prototype and real users.
