# AI Prompt Engineering for Hackathons

## The Secret Weapon Nobody Talks About

Here's a truth most hackathon guides won't tell you: the teams winning aren't always the best coders. They're the ones who know how to talk to AI. Prompt engineering isn't a nice-to-have anymore—it's the difference between shipping a half-baked demo and a polished product in 24 hours.

I've seen solo developers outperform entire teams because they could get Cursor to generate exactly what they needed in seconds. I've also watched brilliant engineers waste 3 hours fighting with Copilot because they typed garbage prompts. The tool doesn't matter if you don't know how to use it.

This section gives you the frameworks, prompts, and strategies to turn AI into your hackathon superpower.

---

## Why Prompt Engineering Matters at Hackathons

### The Math Is Simple

Let's say you need to build a user authentication system. Writing it from scratch takes 2-4 hours, even experienced. With good prompts, you can have a working auth flow in 15-20 minutes. That's 2+ hours saved on ONE feature. Across a 24-hour hackathon, effective prompt engineering can save you 8-12 hours of coding time.

That's not an exaggeration. That's time you can spend on your actual differentiator—the thing that makes your project unique.

### Quality Gained

It's not just speed. A well-crafted prompt produces code that:

- Follows best practices you might forget under pressure
- Includes error handling you'd skip at 2 AM
- Uses consistent patterns across your codebase
- Comes with types, tests, and documentation built in

### The Real Cost of Bad Prompts

Bad prompts don't just waste time—they actively hurt your project. Vague instructions produce vague code. You end up with:

- Generic solutions that don't fit your specific use case
- Missing edge cases that crash during your demo
- Inconsistent code styles that make refactoring a nightmare
- Security holes that judges will notice

---

## The Prompt Framework: CTCF

Every effective prompt follows four components. Think CTCF—Context, Task, Constraints, Format.

### Context
What's the project? What tech stack are you using? What have you already built? AI doesn't remember your last conversation (unless you're using Claude with projects). Give it the backstory.

### Task
What exactly do you need? Be specific. "Build a login page" is weak. "Create a React login form component with email/password fields, form validation, error states, and a submit handler that calls our /api/auth endpoint" is strong.

### Constraints
What are the limits? Tech stack, design system, performance requirements, accessibility needs. Constraints force AI to give you relevant solutions instead of generic ones.

### Format
How do you want the output? Single file? Multiple files? With comments? As a step-by-step guide? Tell AI exactly how you want the answer delivered.

---

## 50+ Hackathon-Specific Prompts

### Category 1: Code Generation (10 Prompts)

**1. CRUD API Endpoint**
```
Context: Building a Next.js app with Prisma ORM and PostgreSQL.
Task: Create a REST API endpoint for creating new blog posts.
Constraints: Use Next.js App Router, include input validation with Zod,
return proper HTTP status codes, handle database errors gracefully.
Format: Single file with inline comments explaining each section.
```

**2. Authentication Flow**
```
Context: React + Express app, need JWT-based auth.
Task: Implement complete login/register flow including:
- Register endpoint with password hashing
- Login endpoint with JWT generation
- Auth middleware for protected routes
- React context for auth state management
Constraints: Use bcryptjs for hashing, jsonwebtoken for JWT,
store tokens in httpOnly cookies, include refresh token logic.
Format: Separate files for backend middleware and React context,
with usage examples.
```

**3. WebSocket Real-Time Chat**
```
Context: Node.js backend, React frontend, need real-time messaging.
Task: Create a WebSocket server with rooms, typing indicators,
and message history. Include the React client hook.
Constraints: Use socket.io, implement reconnection logic,
handle user disconnections gracefully, persist last 50 messages.
Format: Server file + client hook + usage example in a React component.
```

**4. Data Processing Pipeline**
```
Context: Processing CSV uploads for a data visualization dashboard.
Task: Build a pipeline that reads CSV files, validates data types,
handles missing values, and transforms data for chart rendering.
Constraints: Handle files up to 10MB, support date/number/string columns,
output JSON compatible with Chart.js. Use streaming for large files.
Format: Single utility module with clear function separation.
```

**5. Payment Integration**
```
Context: Next.js e-commerce hackathon project, need Stripe integration.
Task: Create Stripe checkout flow with:
- Price calculation with tax
- Checkout session creation
- Webhook handler for payment confirmation
- Order confirmation page
Constraints: Use Stripe v2024 SDK, handle test mode,
include error states for failed payments, follow Stripe best practices.
Format: Separate files for API routes, webhook handler, and React components.
```

**6. Image Upload & Processing**
```
Context: User profile system needs avatar upload with resizing.
Task: Build image upload endpoint that:
- Accepts JPEG/PNG up to 5MB
- Resizes to multiple sizes (thumb, medium, large)
- Generates WebP versions
- Stores in local uploads folder
Constraints: Use Sharp library, generate unique filenames,
validate file types server-side, include progress feedback.
```

**7. Search Functionality**
```
Context: Building a searchable product catalog in React.
Task: Implement debounced search with:
- API endpoint with pagination
- Frontend search component with loading states
- Keyboard navigation support
- Recent searches stored in localStorage
Constraints: Debounce 300ms, 20 results per page,
highlight matching text in results, support Ctrl+K shortcut.
```

**8. Form with Multi-Step Wizard**
```
Context: Registration form with 4 steps in React.
Task: Create a multi-step form wizard with:
- Progress indicator
- Step validation before advancing
- Form state persistence across steps
- Review step before submission
Constraints: Use react-hook-form, Zustand for state,
animate step transitions, handle browser back button.
```

**9. Dashboard Charts Component**
```
Context: Admin dashboard needs data visualization.
Task: Create reusable chart components for:
- Line chart (time series data)
- Bar chart (category comparison)
- Pie chart (distribution)
Constraints: Use Recharts, responsive design,
dark/light theme support, loading skeleton states,
handle empty data gracefully.
```

**10. Background Job Processor**
```
Context: Need to process email sending without blocking API.
Task: Implement job queue system with:
- Job creation endpoint
- Worker that processes jobs sequentially
- Retry logic with exponential backoff
- Status tracking endpoint
Constraints: Use Bull queue with Redis, max 3 retries,
job progress tracking, graceful shutdown handling.
```

---

### Category 2: UI/Component Creation (10 Prompts)

**1. Landing Page Hero Section**
```
Task: Create a responsive hero section with gradient background,
animated text reveal on scroll, CTA button with hover effect,
and a floating illustration. Use Tailwind CSS, Framer Motion
for animations. Mobile-first design. Include dark mode variant.
```

**2. Navigation Bar**
```
Task: Build a responsive navbar with:
- Logo on left, links center, auth buttons right
- Mobile hamburger menu with slide-in drawer
- Scroll-based background opacity change
- Active link highlighting
- Dropdown menus for nested navigation
Constraints: Use Tailwind, no external nav libraries,
accessible (ARIA labels), smooth transitions.
```

**3. Data Table with Sorting/Filtering**
```
Task: Create a feature-rich data table component:
- Column sorting (click header to toggle)
- Text search filter per column
- Row selection with checkboxes
- Pagination with page size selector
- Export to CSV button
Constraints: Support 1000+ rows without lag,
virtual scrolling for performance, keyboard navigable.
```

**4. Modal Dialog System**
```
Task: Build a modal system supporting:
- Confirmation dialogs
- Form modals
- Full-screen modals
- Nested modals (max 2 levels)
Constraints: Trap focus inside modal, close on Escape,
click outside to close, body scroll lock,
accessible (role="dialog", aria-modal).
```

**5. Toast Notification System**
```
Task: Create toast notifications with:
- Success, error, warning, info variants
- Auto-dismiss with configurable duration
- Stack management (max 3 visible)
- Swipe to dismiss on mobile
- Action buttons within toasts
Constraints: Use portal for rendering,
animate in/out, no external toast library.
```

**6. Settings/Preferences Page**
```
Task: Build a settings page with:
- Sidebar navigation for settings categories
- Toggle switches for boolean options
- Dropdown selects for enum options
- Color picker for theme customization
- Auto-save with debounce
- Reset to defaults button
Constraints: Persist to localStorage, responsive layout,
group related settings visually.
```

**7. Profile Card Component**
```
Task: Create a user profile card with:
- Avatar with online status indicator
- Name, bio, location display
- Stats row (followers, following, projects)
- Action buttons (follow, message, share)
- Skeleton loading state
Constraints: Support different sizes (sm, md, lg),
hover animation, accessible markup.
```

**8. File Upload Zone**
```
Task: Build a drag-and-drop file upload component:
- Drag zone with visual feedback
- File list with preview thumbnails
- Progress bars for each file
- Remove individual files
- File type and size validation
Constraints: Support multiple files, handle errors gracefully,
accessible (keyboard upload), no external upload library.
```

**9. Pricing Card Section**
```
Task: Create a pricing section with 3 tiers:
- Feature comparison grid
- Popular tier highlighted
- Monthly/annual toggle with discount
- CTA buttons with hover effects
- Responsive: cards stack on mobile
Constraints: Use Tailwind, animate toggle transition,
include tooltip for feature details.
```

**10. Notification Center**
```
Task: Build a notification center dropdown:
- Bell icon with unread count badge
- Notification list grouped by date
- Mark as read/unread toggle
- Clear all button
- Notification preferences link
Constraints: Real-time updates simulation,
animate new notifications sliding in,
handle empty state gracefully.
```

---

### Category 3: API Integration (8 Prompts)

**1. REST API Client with Error Handling**
```
Task: Create a reusable API client module:
- GET, POST, PUT, DELETE methods
- Automatic JWT token attachment
- Request/response interceptors
- Retry logic for 5xx errors
- Request timeout handling
- Type-safe responses with TypeScript generics
Constraints: Use fetch API (no axios), export as singleton,
include request cancellation support.
```

**2. OAuth2 Social Login**
```
Task: Implement Google OAuth2 login flow:
- Redirect to Google consent screen
- Handle callback with authorization code
- Exchange code for tokens
- Fetch user profile
- Create/update local user record
Constraints: Use passport.js, store refresh tokens securely,
handle token expiration, support multiple providers.
```

**3. GraphQL Client Setup**
```
Task: Set up Apollo Client for a React app:
- Configure cache with normalized entities
- Implement authentication link
- Add error handling link
- Set up optimistic updates
- Create common query/mutation hooks
Constraints: Use Apollo Client v3, TypeScript,
include loading/error states in hooks.
```

**4. Third-Party API Wrapper**
```
Task: Create a typed wrapper for the OpenWeatherMap API:
- Current weather by city/coordinates
- 5-day forecast
- Air quality index
- Rate limiting (100 calls/min)
Constraints: Cache responses for 10 minutes,
handle API errors gracefully, TypeScript types for all responses,
environment variable for API key.
```

**5. Webhook Handler**
```
Task: Build a webhook receiver for Stripe events:
- Verify webhook signature
- Parse event types (payment_intent.succeeded, etc.)
- Update database records
- Return 200 quickly, process async
Constraints: Use raw body for signature verification,
queue heavy processing, log all events for debugging.
```

**6. Real-Time Data Sync**
```
Task: Implement real-time data synchronization:
- Server-Sent Events for updates
- Optimistic local updates
- Conflict resolution strategy
- Offline queue for failed syncs
Constraints: Handle reconnection, batch updates,
debounce frequent changes, handle out-of-order events.
```

**7. File Download with Progress**
```
Task: Create file download utility with progress tracking:
- Fetch with ReadableStream
- Progress callback with percentage
- Cancel support
- Blob save to disk
Constraints: Handle large files (100MB+),
show download speed, retry on network error,
support range requests.
```

**8. API Rate Limiter**
```
Task: Implement client-side rate limiting:
- Token bucket algorithm
- Queue excess requests
- Respect Retry-After headers
- Visual indicator when rate limited
Constraints: Per-endpoint limits, configurable,
don't lose queued requests, graceful degradation.
```

---

### Category 4: Debugging (8 Prompts)

**1. Generic Error Diagnosis**
```
Task: I'm getting this error in my React app:
"TypeError: Cannot read properties of undefined (reading 'map')"
It happens when the API response is empty. How do I fix this?
My component renders a list from props.data.items.map().
Include the fix and explain why it broke.
```

**2. API Response Mismatch**
```
Task: My API returns { data: [...] } but my frontend expects [...].
Console shows: "data.map is not a function"
Here's my fetch call and component code:
[paste code]
Help me fix the data extraction and add proper error handling.
```

**3. CSS Layout Breaking**
```
Task: My flexbox layout works on desktop but collapses on mobile.
Here's my CSS:
[paste CSS]
The sidebar should be 250px on desktop and hidden on mobile.
What's causing the collapse and how do I fix it with Tailwind?
```

**4. State Not Updating**
```
Task: My React state isn't updating after an API call.
I'm using useState, calling setState inside an async function,
but the component doesn't re-render. Here's my code:
[paste code]
Explain the issue and show the correct approach.
```

**5. Memory Leak in React**
```
Task: My component causes a warning: "Can't perform a React state
update on an unmounted component." It fetches data on mount
and has a setInterval for polling. How do I clean this up?
Include the corrected useEffect with proper cleanup.
```

**6. Database Query Slow**
```
Task: This Prisma query takes 3 seconds for 1000 records:
[paste query]
The User table has 50k records, Post has 200k.
How do I optimize this? Add indexes, use select, or restructure?
```

**7. Authentication Token Expired**
```
Task: Users report being logged out randomly. My JWT expires
after 1 hour but I have no refresh mechanism. The frontend
stores the token in localStorage. Implement a refresh token
flow that silently refreshes before expiration.
```

**8. Build/Bundle Error**
```
Task: My Vite build fails with:
"JavaScript heap out of memory"
The build works in dev mode. My bundle includes 3 large libraries.
How do I analyze what's bloating the bundle and fix it?
Include steps for using rollup-plugin-visualizer.
```

---

### Category 5: Documentation (7 Prompts)

**1. README Generator**
```
Task: Generate a professional README.md for my project:
- Project name: [name]
- One-line description: [description]
- Tech stack: [list]
- Features: [list]
Include: badge row, quick start, environment variables,
API reference, contributing guide, license.
Format: Clean markdown with proper heading hierarchy.
```

**2. API Documentation**
```
Task: Generate API documentation for these endpoints:
[paste endpoint list]
Include for each: method, URL, request body schema,
response schema, example curl command, error codes.
Format: OpenAPI-style markdown table.
```

**3. Code Comments**
```
Task: Add concise JSDoc comments to this function:
[paste function]
Include: description, @param with types, @returns,
@example usage. Keep comments brief—no fluff.
```

**4. Changelog**
```
Task: Generate a changelog from these git commits:
[paste commits]
Format: Keep a Changelog convention.
Group into: Added, Changed, Fixed, Removed.
Write user-facing descriptions, not developer jargon.
```

**5. Architecture Decision Record**
```
Task: Write an ADR for choosing PostgreSQL over MongoDB for
our hackathon project. We need complex queries, ACID compliance,
and our data is relational. Include: context, decision,
consequences (positive and negative), status.
Format: Standard ADR template.
```

**6. Onboarding Guide**
```
Task: Write a 5-minute onboarding guide for new contributors:
- Prerequisites
- Clone and setup instructions
- Development server startup
- Running tests
- Common issues and fixes
Assume the reader knows basic Git but not this specific project.
```

**7. Pitch Deck Script**
```
Task: Write a 3-minute pitch script for this project:
[paste project description]
Include: hook (10 sec), problem (30 sec), solution (60 sec),
demo callout (30 sec), traction (30 sec), ask (20 sec).
Tone: conversational, confident, not salesy.
```

---

### Category 6: Pitch/Script Writing (7 Prompts)

**1. Elevator Pitch (30 seconds)**
```
Task: Write a 30-second elevator pitch for [project].
We solve [problem] for [audience] using [technology].
What makes us different is [differentiator].
Tone: confident, clear, no buzzwords. Under 80 words.
```

**2. Demo Script**
```
Task: Create a demo script for a 5-minute live demo:
[paste feature list]
Structure: setup context (30 sec), core feature walk (2 min),
advanced feature (1 min), wrap-up (30 sec).
Include transition phrases and what to click at each step.
```

**3. Judge Q&A Prep**
```
Task: Generate 10 likely judge questions for [project]
and concise answers for each. Questions should cover:
technical approach, scalability, market size, competition,
team background, monetization. Answers: 2-3 sentences each.
```

**4. Problem Statement**
```
Task: Write a compelling problem statement for:
[project description]
Include: who has the problem, how big is it,
what's the current workaround, why it matters now.
Tone: urgent but factual. 150 words max.
```

**5. Value Proposition**
```
Task: Create a one-sentence value proposition:
For [target user] who [need], [product] is a [category]
that [key benefit]. Unlike [competitor], we [differentiator].
Make it memorable and specific.
```

**6. Social Media Announcement**
```
Task: Write a Twitter/X thread (5 tweets) announcing our
hackathon win/project launch. Include: hook tweet,
problem, solution, tech highlight, CTA.
Tone: excited but professional. Use emojis sparingly.
```

**7. Blog Post Outline**
```
Task: Create a blog post outline for "How we built [project]
in 24 hours at [hackathon name]." Include: intro,
technical deep-dive sections, challenges overcome,
lessons learned, conclusion. Target: 1500 words.
```

---

## Prompt Quality Ladder

### Code Generation

**BAD:** "Make me a login page"

**GOOD:** "Create a React login component with email and password fields"

**GREAT:** "Create a React login component with email/password fields using react-hook-form for validation. Include: email format validation, password minimum 8 chars, show/hide password toggle, loading state on submit, error message display, 'Forgot password?' link, and responsive design using Tailwind. The form should call POST /api/auth/login with FormData and store the JWT in an httpOnly cookie via the response. Include TypeScript interfaces for form data and API response."

### UI/Component Creation

**BAD:** "Make a nice navbar"

**GOOD:** "Build a responsive navigation bar with mobile hamburger menu"

**GREAT:** "Build a responsive navigation bar using Tailwind CSS with: logo on left, centered nav links (Home, About, Projects, Contact), auth buttons on right (Login/Signup). Mobile breakpoint at md: hamburger icon that toggles a slide-in drawer from the right. Include: scroll-based background opacity transition (transparent to white), active link underline animation, dropdown for 'Projects' with 3 sub-items, ARIA labels for accessibility, and smooth 200ms transitions on all interactive elements."

### API Integration

**BAD:** "Connect to an API"

**GOOD:** "Create a fetch wrapper for REST API calls"

**GREAT:** "Create a TypeScript API client module using fetch with: generic typed request method supporting GET/POST/PUT/DELETE, automatic Authorization header from stored JWT, request interceptor for logging, response interceptor that handles 401 (redirect to login) and 5xx (retry 3 times with exponential backoff), configurable timeout (default 10s), request cancellation via AbortController, and centralized error handling that extracts API error messages. Export as singleton instance."

### Debugging

**BAD:** "My code doesn't work"

**GOOD:** "I'm getting a TypeError: Cannot read properties of undefined"

**GREAT:** "I'm getting 'TypeError: Cannot read properties of undefined (reading map)' in my UserList component at line 23. The component receives data from useEffect fetch to /api/users. The error only happens when the API returns an empty array wrapped in { users: [] }. My component expects a flat array. Here's the relevant code: [paste]. What's the fix and how do I prevent similar issues?"

### Documentation

**BAD:** "Write docs for this"

**GOOD:** "Generate a README for my project"

**GREAT:** "Generate a README.md for a Next.js 14 e-commerce project called 'ShopFast'. Include: shield badges (build, license, PRs welcome), one-paragraph description, feature list (6 items), tech stack with versions, quick start (clone, install, env setup, dev server), environment variables table (4 vars with descriptions), project structure tree, deployment section (Vercel), contributing guidelines, and MIT license. Use clean markdown with proper heading hierarchy."

### Pitch/Script Writing

**BAD:** "Write me a pitch"

**GOOD:** "Write a 2-minute pitch for my hackathon project"

**GREAT:** "Write a 2-minute pitch script for 'CodeCollab', a real-time collaborative code editor for remote pair programming. Structure: Hook (15 sec) - 'How many hours have you lost to screen-sharing nightmares?', Problem (30 sec) - remote dev collaboration tools are broken, Solution (45 sec) - live cursor sync, shared terminal, AI pair programmer, Demo callout (15 sec) - 'Watch this', Ask (15 sec) - seeking beta testers. Tone: conversational, no buzzwords, include stage directions in brackets."

---

## When AI Fails You: Manual Coding Survival Guide

AI isn't perfect. Here's when and why it fails, and what to do about it.

### Common Failure Modes

**1. Hallucinated APIs**
AI invents functions that don't exist. Always verify against official docs.
*Survival move:* Keep official documentation open in a tab. Test every API call immediately.

**2. Outdated Patterns**
AI might suggest deprecated React methods or old library versions.
*Survival move:* Check the library's changelog. Use `npx npm-check-updates` to verify versions.

**3. Circular Logic**
AI generates code that calls itself infinitely or creates dependency cycles.
*Survival move:* Draw the call graph on paper. If a function calls another that calls the first, you have a problem.

**4. Over-Engineering**
AI adds unnecessary abstraction layers when you need a simple function.
*Survival move:* Ask for the simplest possible version. "Write this without any abstractions or design patterns."

**5. Context Loss**
AI forgets what you told it 5 prompts ago and contradicts earlier decisions.
*Survival move:* Summarize your architecture in a single prompt before asking for new code. Include key decisions.

### The Manual Coding Emergency Kit

When AI completely fails, you need fallback strategies:

**Copy from Documentation**
Most libraries have example code in their docs. Copy it, modify it. It's faster than writing from scratch.

**Use Template Generators**
```bash
npx create-next-app@latest my-app
npx create-expo-app my-app
npx degit user/repo#branch folder
```

**Stack Overflow Snippets**
Search for your exact error message. Copy-paste the highest-voted answer. Adapt it.

**Built-In Browser Features**
`navigator.clipboard`, `IntersectionObserver`, `WebSocket` — many things you think you need a library for, the browser already does.

**ChatGPT Fallback**
If one AI tool fails, try another. Claude, GPT-4, and Gemini have different strengths.

---

## Tool-Specific Tips

### Cursor

**Best for:** Full codebase awareness, multi-file edits

**Pro Tips:**
- Use `@codebase` to let Cursor search your entire project for context
- The `.cursorrules` file is gold — add your project conventions there
- Use Cmd+K for inline edits, Cmd+L for chat
- Composer mode for multi-file changes: describe what you want across files

**Power Prompt:**
```
@codebase I need to add a notification system. Search the codebase for
existing patterns, then create the necessary files following the same
conventions. Include database migration, API routes, and React components.
```

### GitHub Copilot

**Best for:** Inline completions, boilerplate generation

**Pro Tips:**
- Write a comment describing what you want, then let Copilot autocomplete
- Use `// copilot:` directives for specific behavior
- Tab to accept, Esc to dismiss — build the muscle memory
- Copilot Chat is better than inline for complex questions

**Power Prompt (in Copilot Chat):**
```
Explain this function, then suggest improvements for error handling
and performance. Apply the improvements directly.
```

### Claude

**Best for:** Long context, nuanced reasoning, architecture decisions

**Pro Tips:**
- Claude handles massive context windows — paste entire files without worry
- Use Projects to maintain context across sessions
- Ask Claude to think through tradeoffs before generating code
- Great for code review: paste your code and ask for issues

**Power Prompt:**
```
I'm building a real-time collaboration feature. Here's my current
architecture: [paste]. Before writing code, analyze potential bottlenecks,
race conditions, and scalability issues. Then suggest the optimal approach
with code examples.
```

### v0 (Vercel)

**Best for:** UI component generation from descriptions

**Pro Tips:**
- Describe the component visually: "A card with avatar, name, bio, and follow button"
- Reference real products: "Like Twitter's profile card but simpler"
- Iterate: generate, copy code, tweak, regenerate if needed
- Works great with shadcn/ui components

**Power Prompt:**
```
A dashboard sidebar navigation component with: logo at top,
nav items with icons and labels, collapsible section for sub-items,
user avatar and settings at bottom. Use shadcn/ui components,
dark theme, hover states, active indicator line on left.
```

### Bolt.new

**Best for:** Full-stack app scaffolding in one prompt

**Pro Tips:**
- Be extremely specific about tech stack in the first prompt
- Include database schema if you need one
- Bolt handles deployment — use it for rapid prototyping
- Iterate on the generated code within the platform

**Power Prompt:**
```
Build a project management app with: Next.js 14, PostgreSQL via Prisma,
Tailwind CSS, authentication with next-auth. Features: project CRUD,
task boards with drag-and-drop, team invitations, real-time updates.
Include database schema, API routes, and responsive UI.
```

---

## Common Prompt Mistakes at Hackathons

### 1. Being Too Vague
**Mistake:** "Make it look good"
**Fix:** "Add a gradient background from blue-600 to purple-600, rounded corners (12px), subtle box shadow, and hover scale effect"

### 2. Not Providing Context
**Mistake:** "Fix this bug" (without sharing the code or error)
**Fix:** Always include: the error message, relevant code, what you expected, what actually happened

### 3. Asking for Too Much at Once
**Mistake:** "Build my entire app"
**Fix:** Break into features. One prompt per component or endpoint.

### 4. Not Iterating
**Mistake:** Accepting the first AI output without testing
**Fix:** Generate → Test → Refine. Three rounds minimum for complex code.

### 5. Ignoring Existing Code
**Mistake:** Not mentioning your existing patterns
**Fix:** "Follow the same patterns used in src/components/Button.tsx"

### 6. Forgetting Edge Cases
**Mistake:** "Create a form" (no mention of validation, errors, loading)
**Fix:** Always include: loading states, error states, empty states, edge cases

### 7. Not Specifying Tech Stack
**Mistake:** "Create a dashboard" (AI might use Angular when you need React)
**Fix:** Always lead with your tech stack

### 8. Accepting Hallucinated Code
**Mistake:** Using AI-generated code without verifying it runs
**Fix:** Test every function immediately. If it doesn't work, tell AI the exact error.

---

## The 3 AM Prompt

It's 3 AM. You're exhausted. You've been coding for 16 hours. Your brain isn't working, but you still need AI to produce something useful. Here's how.

### The Exhaustion Framework

**1. Be Exhaustingly Specific**
Your tired brain can't hold context. Write it all down:
```
Project: [name]
Tech: [exact versions]
Current state: [what's built]
What I need RIGHT NOW: [single feature]
Error if any: [paste it]
```

**2. Use Template Prompts**
Keep these saved in your notes:

For UI:
```
Create a [component type] with [specific features].
Use [tech stack]. Match the style of [existing component].
Include loading, error, and empty states.
```

For API:
```
Create a [method] endpoint for [resource].
Input: [schema]. Output: [schema].
Handle errors: [list]. Validate: [rules].
```

For Debug:
```
Error: [exact message]
File: [path]
Line: [number]
Code: [paste]
Expected: [what should happen]
```

**3. The "Explain First" Trick**
When you're too tired to write good prompts, ask AI to explain your code back to you first. Then ask for changes. This forces AI to understand your context without you having to type it all out.

```
Explain what this code does, then add error handling for:
1. Network failures
2. Invalid responses
3. Timeout after 5 seconds
```

**4. Copy-Paste Your Error**
When you can't think, just paste the error. AI is great at interpreting error messages even with zero context from you.

**5. The Nuclear Option**
If all else fails, paste your entire file and say: "This file has a bug at line X. Fix it." Sometimes brute force works when finesse fails.

### Sleep vs. Push Through

Here's the real talk: if you're hallucinating bugs that don't exist, take a 20-minute nap. Set an alarm. You'll catch more bugs rested than exhausted. The AI can wait. Your brain can't.

---

## Quick Reference Card

| Situation | Prompt Pattern |
|-----------|---------------|
| Need a component | "Create a [type] with [features]. Use [tech]. Include [states]." |
| API integration | "Connect to [API] for [purpose]. Handle [errors]. Cache [what]." |
| Bug fix | "Error: [message] in [file]. Code: [paste]. Fix it." |
| Refactor | "Simplify [function]. Remove [abstractions]. Keep [functionality]." |
| Documentation | "Document [what] for [audience]. Include [sections]. Tone: [style]." |
| Pitch | "Write a [duration] pitch for [project]. Structure: [outline]." |

---

## Final Thought

Prompt engineering at hackathons isn't about being clever with words. It's about being clear about what you need. The best hackathon prompt is one that produces working code on the first try. That means being specific, providing context, and iterating fast.

Master this, and AI becomes the teammate that never sleeps, never gets frustrated, and never needs a coffee break. Use it wisely, and you'll ship things that would've been impossible 24 hours ago.
