# Example Hackathon Homepage: "TrackIntern"

This is a detailed breakdown of a hackathon homepage that won "Best UI/UX" at a 200-person hackathon. Every design decision is explained so you can replicate the approach.

---

## The 3-Second Rule Test

Before we dive into sections, here's the test we applied: **Can a judge understand what this app does in 3 seconds?** We tested by showing the homepage to strangers for 3 seconds, then hiding it. If they couldn't describe the app, we redesigned. It took 4 iterations to pass.

---

## Section 1: Hero (Above the Fold)

**What it contained:**
- Headline: "Never lose track of your internship hunt"
- Subheadline: "One dashboard to track every application, deadline, and status — so you can focus on landing the role."
- CTA button: "Start Tracking Free" (indigo-500 background, white text, rounded-md, 48px height)
- Secondary link: "See how it works" (underlined, gray-600, jumps to features section)

**Background:** Clean white. No gradients, no images, no distractions.

**Why these choices:**
- The headline speaks to a pain point, not a feature. "Track your internships" is boring. "Never lose track" implies you're currently losing track — that's relatable.
- The subheadline explains the "how" in one sentence. Judges read this while the presenter talks.
- Single CTA eliminates decision paralysis. One button, one action.
- White background was intentional — it loads instantly, looks clean on projectors, and doesn't compete with the app screenshots below.

**Typography:**
- Headline: Inter Bold, 48px (36px on mobile), gray-900, line-height 1.1
- Subheadline: Inter Regular, 20px (16px on mobile), gray-500, line-height 1.6
- CTA: Inter SemiBold, 16px, white

**Spacing:**
- Top padding: 120px (pushes hero below any potential sticky nav)
- Bottom padding: 80px
- Headline to subheadline: 24px
- Subheadline to CTA: 32px

---

## Section 2: Social Proof Bar

**What it contained:**
- "Trusted by 200+ students at [University Name]"
- Three small logos of campus organizations (club logos we had permission to use)

**Why it existed:** Even though we were a new hackathon project, referencing a specific university made it feel real. The logos were grayscale and small — they added credibility without dominating.

**Design choices:**
- Background: gray-50 (subtle contrast from white hero)
- Logos: 40px height, grayscale, 60% opacity
- Text: Inter Regular, 14px, gray-400, uppercase, letter-spacing 1px

**Mobile:** Logo row became a single line with smaller logos. We hid one logo on screens under 375px to prevent cramping.

---

## Section 3: Feature Cards (3-Column Grid)

**What it contained:**
Three cards, each with an SVG icon, a 3-word headline, and a one-sentence description:

1. **Track Deadlines** — "Never miss a closing date again. Set reminders and see what's due."
2. **Status Dashboard** — "Applied, interview, offer, rejected — see where you stand at a glance."
3. **Smart Reminders** — "Get notified 3 days before deadlines so you're never scrambling."

**Why three cards:** Research shows 3 is the sweet spot for feature lists. Two feels thin, four feels overwhelming. Three is scannable.

**Design choices:**
- Cards: white background, gray-50 border (1px), rounded-lg, shadow-sm
- On hover: shadow-md, slight translateY(-2px) — subtle lift effect
- Icons: custom SVGs, 48x48px, indigo-500 color, no background circle
- Headline: Inter SemiBold, 18px, gray-900
- Description: Inter Regular, 14px, gray-500
- Card padding: 32px internal
- Grid gap: 24px
- Max width: 1100px centered

**Why no images/screenshots in cards:** Screenshots in feature cards often look cluttered at hackathon scales. Simple icons are cleaner and load faster. We saved screenshots for the demo section below.

**Mobile:** Cards stacked vertically with full width. Gap reduced to 16px.

---

## Section 4: Live App Preview

**What it contained:**
- A browser-frame mockup (just a gray top bar with three dots) showing a real screenshot of our dashboard
- Below the screenshot: "Built with Next.js, Tailwind CSS, and PostgreSQL" (tech stack callout)

**Why we included this:** Judges want to see the actual app, not just marketing copy. A browser-frame screenshot feels more authentic than a floating image with drop shadows.

**Design choices:**
- Browser frame: gray-200 top bar (32px height), white body, rounded-t-lg
- Screenshot: full-width within the frame, no cropping
- Tech stack text: Inter Regular, 13px, gray-400, centered below frame
- Section background: gray-50
- Top/bottom padding: 80px

**Mobile:** The browser frame scaled down proportionally. We tested on iPhone SE — the screenshot was still readable because we kept the dashboard UI large.

---

## Section 5: How It Works (3 Steps)

**What it contained:**
Three numbered steps in a horizontal row:

1. **Sign up in 10 seconds** — "Just email and password. No long forms."
2. **Add your internships** — "Company, role, deadline. That's it."
3. **Never miss a deadline** — "We remind you 3 days before each one closes."

**Why this section exists:** It answers "is this complicated to use?" before the judge even asks. The numbers (10 seconds, 3 days) make it concrete.

**Design choices:**
- Numbers: Inter Bold, 48px, indigo-500 (large and prominent)
- Headline: Inter SemiBold, 18px, gray-900
- Description: Inter Regular, 14px, gray-500
- Steps connected by a thin gray line (1px, gray-200) between them
- Section padding: 80px top/bottom

**Mobile:** Steps stacked vertically, connecting lines removed. Numbers stayed large — they're the visual anchor.

---

## Section 6: Final CTA

**What it contained:**
- Headline: "Ready to organize your internship hunt?"
- CTA button: "Get Started — It's Free" (same indigo-500 style as hero)
- No secondary options — just one button

**Why another CTA:** Some judges scroll through the entire page before deciding to engage. The final CTA catches them at the bottom. Repeating the same button style creates visual consistency.

**Design choices:**
- Background: white (same as hero — bookend effect)
- Headline: Inter Bold, 32px, gray-900
- Top padding: 80px, bottom: 120px (generous breathing room)

---

## Color Palette (Exact Values)

| Token | Hex | Usage |
|-------|-----|-------|
| Primary | #6366F1 | Buttons, icons, accents (indigo-500) |
| Primary hover | #4F46E5 | Button hover state (indigo-600) |
| Background | #FFFFFF | Main background |
| Surface | #F9FAFB | Section alternating bg (gray-50) |
| Border | #E5E7EB | Card borders (gray-200) |
| Text primary | #111827 | Headlines (gray-900) |
| Text secondary | #6B7280 | Descriptions (gray-500) |
| Text muted | #9CA3AF | Tech stack, labels (gray-400) |

**Why this palette:** It's Tailwind's default, which means zero custom CSS. Every color is a utility class. Judges saw a cohesive, professional design — they didn't know it was just `text-gray-900` and `bg-indigo-500`.

---

## Typography System

| Element | Font | Weight | Size | Line Height |
|---------|------|--------|------|-------------|
| H1 (Hero) | Inter | Bold (700) | 48px / 36px mobile | 1.1 |
| H2 (Section) | Inter | Bold (700) | 32px / 24px mobile | 1.2 |
| H3 (Card) | Inter | SemiBold (600) | 18px | 1.4 |
| Body | Inter | Regular (400) | 16px / 14px mobile | 1.6 |
| Small | Inter | Regular (400) | 13px | 1.5 |
| Button | Inter | SemiBold (600) | 16px | 1.0 |

**Why Inter:** It's free, it's readable at all sizes, and it's already in Tailwind's default config. No custom font loading needed.

---

## Spacing System

We used a consistent 8px-based spacing scale:

- Section padding: 80px vertical (120px for hero bottom)
- Card internal padding: 32px
- Gap between cards: 24px
- Gap between headline and description: 8-12px
- Container max-width: 1100px centered with auto margins

**Why consistency matters:** Judges notice subconsciously when spacing is irregular. A 32px gap here and a 27px gap there looks sloppy even if they can't pinpoint why. Using a system eliminates that.

---

## What We Cut (And Why)

1. **Animated gradient background** — looked cool but distracted from content. Slowed mobile rendering.
2. **Testimonial section** — we had no real users yet. Fake testimonials feel dishonest.
3. **Pricing section** — it's a free hackathon project. Pricing confuses people.
4. **Footer with links** — unnecessary for a hackathon demo. Saved vertical space.
5. **Dark mode toggle** — cool engineering effort, zero demo value. Judges don't care about dark mode in a 60-second pitch.

**Rule of thumb:** If a section doesn't help a judge understand the app in 3 seconds, cut it.
