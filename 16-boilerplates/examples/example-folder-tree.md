# Example Folder Structures — 3 Project Types

Each structure includes explanations of WHY every folder exists. Pick the one closest to your project type and adapt it.

---

## 1. AI SaaS App (Next.js + PostgreSQL + OpenAI)

Built for projects where AI is the core value — not a bolted-on feature.

```
ai-saas/
├── app/                          # Next.js App Router — all routes live here
│   ├── (auth)/                   # Route group: auth pages (no layout collision)
│   │   ├── login/page.tsx        #   Login form
│   │   ├── signup/page.tsx       #   Signup form
│   │   └── layout.tsx            #   Auth-specific layout (no sidebar)
│   ├── (dashboard)/              # Route group: main app pages
│   │   ├── page.tsx              #   Dashboard home — metrics, recent activity
│   │   ├── projects/page.tsx     #   Project list with search/filter
│   │   ├── settings/page.tsx     #   User/org settings
│   │   └── layout.tsx            #   Dashboard layout (sidebar + header)
│   ├── api/                      # API route handlers
│   │   ├── auth/                 #   NextAuth.js endpoints
│   │   ├── projects/             #   CRUD for projects
│   │   ├── generate/             #   POST — triggers AI generation
│   │   └── webhooks/             #   Stripe, email service callbacks
│   └── layout.tsx                # Root layout — html, body, providers
│
├── components/                   # Shared React components
│   ├── ui/                       # Low-level primitives (Button, Input, Card)
│   │   ├── button.tsx
│   │   ├── input.tsx
│   │   └── card.tsx
│   ├── dashboard/                # Dashboard-specific components
│   │   ├── MetricCard.tsx        #   Single metric display
│   │   ├── ActivityFeed.tsx      #   Recent activity list
│   │   └── ProjectGrid.tsx       #   Grid of project cards
│   └── ai/                       # AI-related UI components
│       ├── PromptInput.tsx       #   Text area for prompt entry
│       ├── GenerationResult.tsx  #   Displays AI output with formatting
│       └── LoadingStream.tsx     #   Streaming text animation
│
├── lib/                          # Shared utilities and configs
│   ├── prisma.ts                 # Prisma client singleton (prevents connection leaks)
│   ├── auth.ts                   # NextAuth config and helpers
│   ├── openai.ts                 # OpenAI client with retry logic
│   ├── stripe.ts                 # Stripe client setup
│   └── utils.ts                  # Generic helpers (formatDate, cn, etc.)
│
├── models/                       # Database schema and business logic
│   ├── schema.prisma             # Prisma schema — your database blueprint
│   ├── user.model.ts             # User-specific queries and helpers
│   └── project.model.ts          # Project-specific queries and helpers
│
├── prompts/                      # AI prompt templates — KEEP THESE HERE
│   ├── system.md                 # System prompt for all generations
│   ├── generate-project.md       # Template for new project generation
│   └── improve.md                # Template for iteration/improvement
│                                 # Why separate? You'll tweak prompts daily.
│                                 # Mixing them in code makes A/B testing painful.
│
├── hooks/                        # Custom React hooks
│   ├── useProjects.ts            # Fetch/cache project data
│   ├── useGeneration.ts          # Handle AI generation with loading states
│   └── useSubscription.ts        # Check plan limits, usage
│
├── types/                        # TypeScript type definitions
│   ├── project.ts                # Project type interfaces
│   ├── user.ts                   # User type interfaces
│   └── api.ts                    # API request/response types
│
├── public/                       # Static assets (served at /)
│   ├── images/                   # Logos, icons, illustrations
│   ├── fonts/                    # Self-hosted fonts (if any)
│   └── favicon.ico
│
├── prisma/                       # Database tooling
│   ├── seed.ts                   # Seed script — creates test data
│   └── migrations/               # Auto-generated migration files
│
├── .env.example                  # Template — NEVER commit .env itself
├── .gitignore
├── next.config.js
├── tailwind.config.ts
├── tsconfig.json
├── package.json
└── README.md
```

**Why this structure works for AI projects:**

- `prompts/` is separate from `lib/` — prompts change constantly, you don't want to hunt through code to tweak them
- `models/` separates database logic from API routes — your routes stay thin and testable
- `components/ai/` keeps AI-specific UI isolated — if you swap OpenAI for Anthropic, only these components change
- `(auth)` and `(dashboard)` route groups keep layouts clean without nested folders

---

## 2. Real-Time Collaboration Tool (WebSockets + CRDT)

Built for projects where multiple users editing simultaneously is the core feature.

```
collab-tool/
├── app/
│   ├── page.tsx                  # Landing page / marketing
│   ├── (app)/                    # Main application
│   │   ├── layout.tsx            #   App shell — sidebar, header, socket provider
│   │   ├── dashboard/page.tsx    #   All rooms/projects overview
│   │   ├── room/[id]/page.tsx    #   Individual room — the main editor view
│   │   └── settings/page.tsx     #   User/org settings
│   └── api/
│       ├── rooms/                #   CRUD for rooms (REST)
│       ├── auth/                 #   NextAuth endpoints
│       └── webhooks/             #   Service callbacks
│
├── rooms/                        # Room management logic (server-side)
│   ├── room-manager.ts           # Create, join, leave rooms — manages state
│   ├── presence.ts               # Who's in the room, cursor positions, status
│   └── permissions.ts            # Who can edit, view, or admin a room
│
├── socket/                       # WebSocket infrastructure
│   ├── server.ts                 # WebSocket server setup (ws or socket.io)
│   ├── handlers/                 # Event handlers — one file per event type
│   │   ├── join-room.ts          #   User joins a room
│   │   ├── leave-room.ts         #   User leaves (cleanup, notify others)
│   │   ├── cursor-move.ts        #   Broadcast cursor position
│   │   ├── content-change.ts     #   Document edit received
│   │   └── undo-redo.ts          #   Undo/redo operations
│   ├── middleware.ts              # Auth check — verify token before connect
│   └── rooms.ts                  # Active room registry (in-memory or Redis)
│
├── sync/                         # Data synchronization engine
│   ├── crdt/                     # Conflict-free Replicated Data Types
│   │   ├── yjs-provider.ts       #   Yjs setup — the CRDT library
│   │   ├── awareness.ts          #   Who sees what, when
│   │   └── persistence.ts        #   Save CRDT state to database
│   ├── diff.ts                   # Compute diffs for partial updates
│   └── reconciliation.ts        # Handle out-of-order messages
│
├── components/                   # UI components
│   ├── editor/                   # Editor-specific
│   │   ├── EditorCanvas.tsx      #   Main editing surface
│   │   ├── Toolbar.tsx           #   Formatting options
│   │   └── BlockHandle.tsx       #   Drag handle, add block
│   ├── presence/                 # Collaboration indicators
│   │   ├── UserAvatar.tsx        #   Colored avatar in corner
│   │   ├── CursorOverlay.tsx     #   Other users' cursors
│   │   └── OnlineList.tsx        #   Sidebar list of who's here
│   └── ui/                       # Shared primitives
│
├── lib/
│   ├── prisma.ts
│   ├── redis.ts                  # Redis client — pub/sub for multi-server
│   ├── auth.ts
│   └── utils.ts
│
├── hooks/
│   ├── useSocket.ts              # Connect/disconnect WebSocket
│   ├── useRoom.ts                # Room state + presence
│   └── useCrdt.ts                # Yjs document binding
│
├── types/
│   ├── room.ts                   # Room, User, Permission types
│   ├── socket-events.ts          # All WebSocket event definitions (shared client/server)
│   └── crdt.ts                   # CRDT operation types
│
├── public/
│   └── ...
│
├── prisma/
│   ├── schema.prisma
│   └── seed.ts
│
├── docker-compose.yml            # Redis + Postgres for local dev
├── .env.example
├── next.config.js
├── package.json
└── README.md
```

**Why this structure works for real-time apps:**

- `socket/` is completely separate from `app/` — the WebSocket server runs independently from Next.js, so you can scale them separately
- `handlers/` inside `socket/` — one file per event keeps the server file from becoming a 500-line mess
- `sync/crdt/` is isolated — CRDT logic is complex, you want it testable without spinning up a WebSocket server
- `rooms/` is server-side only — never imported by client components, prevents accidental data leaks
- `types/socket-events.ts` is shared between client and server — one source of truth for event names and payloads

---

## 3. Mobile-First PWA (React + Capacitor or Pure PWA)

Built for projects where 60%+ of users are on phones, and offline support matters.

```
mobile-pwa/
├── public/
│   ├── manifest.json             # PWA manifest — app name, icons, theme color
│   ├── sw.js                     # Service worker — offline caching strategy
│   ├── icons/                    # App icons at every required size
│   │   ├── icon-72x72.png
│   │   ├── icon-96x96.png
│   │   ├── icon-128x128.png
│   │   ├── icon-144x144.png
│   │   ├── icon-192x192.png     #   Android splash
│   │   └── icon-512x512.png     #   Android splash large
│   ├── images/                   # Splash screens, placeholders
│   └── fonts/                    # Self-hosted fonts for offline use
│
├── src/
│   ├── components/               # Reusable UI components
│   │   ├── layout/               # App shell components
│   │   │   ├── BottomNav.tsx     #   Mobile bottom navigation
│   │   │   ├── Header.tsx        #   Top bar with actions
│   │   │   ├── PullToRefresh.tsx #   Pull-down gesture to refresh
│   │   │   └── AppShell.tsx      #   Wraps all pages with nav + header
│   │   ├── feedback/             # User feedback components
│   │   │   ├── Toast.tsx         #   Temporary notification
│   │   │   ├── Skeleton.tsx      #   Loading placeholder
│   │   │   └── EmptyState.tsx    #   "Nothing here yet" screen
│   │   └── ui/                   # Primitives (Button, Input, etc.)
│   │
│   ├── pages/                    # Route pages (or screens)
│   │   ├── Home.tsx              #   Main feed / landing
│   │   ├── Detail.tsx            #   Single item view
│   │   ├── Profile.tsx           #   User profile
│   │   ├── Settings.tsx          #   App settings
│   │   └── Offline.tsx           #   Shown when no connection
│   │
│   ├── hooks/                    # Custom React hooks
│   │   ├── useOnlineStatus.ts    #   navigator.onLine wrapper + event listener
│   │   ├── useLocalStorage.ts    #   Persist state to localStorage
│   │   ├── useInstallPrompt.ts   #   "Add to Home Screen" prompt handling
│   │   ├── useShare.ts           #   Web Share API wrapper
│   │   └── useHaptic.ts          #   Vibration feedback (navigator.vibrate)
│   │
│   ├── services/                 # Data and API layer
│   │   ├── api.ts                #   HTTP client (fetch wrapper with auth)
│   │   ├── cache.ts              #   IndexedDB/localStorage caching
│   │   ├── push.ts               #   Push notification registration
│   │   └── sync.ts               #   Offline queue — sync when back online
│   │
│   ├── context/                  # React context providers
│   │   ├── AuthContext.tsx        #   Current user state
│   │   ├── ThemeContext.tsx       #   Dark/light mode
│   │   └── NetworkContext.tsx     #   Online/offline state shared across app
│   │
│   ├── utils/                    # Pure utility functions
│   │   ├── formatters.ts         #   Date, currency, text formatting
│   │   ├── validators.ts         #   Input validation (email, phone, etc.)
│   │   └── constants.ts          #   API URLs, feature flags, config
│   │
│   ├── assets/                   # Source assets (before optimization)
│   │   ├── images/               #   Source images
│   │   └── icons/                #   SVG icons (inline or sprite)
│   │
│   ├── styles/                   # Global styles
│   │   ├── globals.css           #   Tailwind imports + base styles
│   │   └── animations.css        #   Keyframe animations, transitions
│   │
│   ├── App.tsx                   # Root component — providers + router
│   └── main.tsx                  # Entry point — renders App into DOM
│
├── tests/
│   ├── unit/                     # Component and hook tests
│   │   ├── hooks/
│   │   │   ├── useOnlineStatus.test.ts
│   │   │   └── useLocalStorage.test.ts
│   │   └── components/
│   │       └── BottomNav.test.ts
│   └── e2e/                      # End-to-end (Playwright or Cypress)
│       ├── navigation.test.ts
│       └── offline.test.ts
│
├── .env.example
├── index.html                    # Vite entry HTML — includes manifest link
├── vite.config.ts
├── tsconfig.json
├── package.json
└── README.md
```

**Why this structure works for mobile-first PWAs:**

- `hooks/` is top-level, not buried in `components/` — hooks are used everywhere, keep them accessible
- `services/sync.ts` handles the offline queue — when the network drops, writes queue up; when it returns, they sync. This is the hardest part of PWAs, give it its own file
- `components/layout/BottomNav.tsx` — mobile navigation lives at the bottom (thumb zone), not the top. This is a mobile-first decision baked into the folder structure
- `context/NetworkContext.tsx` is shared — every component that needs online/offline state pulls from one source, not 10 individual `navigator.onLine` checks
- `public/sw.js` is separate from any framework — service workers should be framework-agnostic so you can update the SW without rebuilding the app

---

## Quick Decision Guide

| Your project is... | Use this structure | Key insight |
|---|---|---|
| AI-focused with API integrations | #1 AI SaaS | Separate prompts from code, keep models clean |
| Multi-user real-time | #2 Collab | Isolate socket/ and sync/ from everything else |
| Mobile-first, offline-capable | #3 PWA | Services + hooks are your foundation |
| Simple hackathon MVP | None of these | Just use `app/`, `components/`, `lib/`. Don't over-architect. |

**The hackathon reality check:** You probably don't need all these folders. Start with the 5 that matter for YOUR project. Add folders when files start getting lost. A flat structure you understand beats a deep structure you have to navigate.
