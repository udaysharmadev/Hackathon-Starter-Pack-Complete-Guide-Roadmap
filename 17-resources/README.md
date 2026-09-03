# 17. Resources

> Stop wasting your first 4 hours searching for tools. This is the only resource list you need — curated, opinionated, and built for hackathons, not textbooks. Bookmark it, star it, and come back every time you compete.

---

## Table of Contents

- [Essential Hackathon Resources](#essential-hackathon-resources)
- [Frameworks & Libraries](#frameworks--libraries)
- [Backend & Database Services](#backend--database-services)
- [AI & ML APIs](#ai--ml-apis)
- [Deployment Platforms](#deployment-platforms)
- [Design & UI Resources](#design--ui-resources)
- [Free Stock Assets](#free-stock-assets)
- [API Discovery Platforms](#api-discovery-platforms)
- [Hackathon Platforms](#hackathon-platforms)
- [Learning Resources](#learning-resources)
- [Communities & Discord Servers](#communities--discord-servers)
- [Newsletters & Update Sources](#newsletters--update-sources)
- [Tools for Productivity](#tools-for-productivity)
- [Chrome Extensions for Hackathons](#chrome-extensions-for-hackathons)
- [My Personal Stack](#my-personal-stack)
- [How to Use This Resource Hub](#how-to-use-this-resource-hub)

---

## Essential Hackathon Resources

These are the top 20 resources every hackathon participant should have bookmarked. If you only read one section, read this.

| # | Resource | URL | What It Does | Free Tier | Best For |
|---|----------|-----|--------------|-----------|----------|
| 1 | **Vercel** | [vercel.com](https://vercel.com) | Deploy frontend apps in seconds with zero config | Yes — generous free tier | Next.js / React deploys |
| 2 | **Supabase** | [supabase.com](https://supabase.com) | Firebase alternative with Postgres, Auth, Storage, Realtime | Yes — 500MB DB, 1GB storage, 50K MAU | Full-stack apps needing a backend fast |
| 3 | **Firebase** | [firebase.google.com](https://firebase.google.com) | Google's app platform — Auth, Firestore, Hosting, Functions | Yes — Spark plan with limits | Rapid prototyping with Google ecosystem |
| 4 | **GitHub Copilot** | [github.com/features/copilot](https://github.com/features/copilot) | AI pair programmer that autocompletes your code | Free for students (Education pack) | Writing boilerplate fast |
| 5 | **OpenAI API** | [platform.openai.com](https://platform.openai.com) | GPT-4o, DALL-E, Whisper — the full AI stack | $5 free credits on signup | AI-powered features |
| 6 | **Railway** | [railway.app](https://railway.app) | Deploy backends, databases, and cron jobs | $5 free credit monthly | Backend + database hosting |
| 7 | **Excalidraw** | [excalidraw.com](https://excalidraw.com) | Hand-drawn style whiteboard for wireframes and diagrams | Yes — completely free | Pitch decks, architecture diagrams |
| 8 | **Notion** | [notion.so](https://notion.so) | All-in-one workspace for notes, wikis, project management | Yes — free plan | Team collaboration during hackathon |
| 9 | **Figma** | [figma.com](https://figma.com) | Collaborative design tool for UI/UX | Yes — 3 files free | UI design and prototyping |
| 10 | **Tailwind CSS** | [tailwindcss.com](https://tailwindcss.com) | Utility-first CSS framework | Yes — completely free | Beautiful UI without writing custom CSS |
| 11 | **shadcn/ui** | [ui.shadcn.com](https://ui.shadcn.com) | Beautifully designed, accessible components for React | Yes — open source | Drop-in UI components |
| 12 | **Lucide Icons** | [lucide.dev](https://lucide.dev) | Consistent, customizable icon set | Yes — open source | Quick, clean iconography |
| 13 | **Unsplash** | [unsplash.com](https://unsplash.com) | Free high-resolution stock photos | Yes — free for commercial use | Hero images, backgrounds |
| 14 | **Google Fonts** | [fonts.google.com](https://fonts.google.com) | Free font library with 1500+ typefaces | Yes — completely free | Typography |
| 15 | **Render** | [render.com](https://render.com) | Deploy web services, static sites, databases | Yes — free tier with limits | Backend hosting without config |
| 16 | **Neon** | [neon.tech](https://neon.tech) | Serverless Postgres with branching | Yes — 0.5GB storage free | Database without managing a server |
| 17 | **Vercel AI SDK** | [sdk.vercel.ai](https://sdk.vercel.ai) | TypeScript toolkit for building AI-powered apps | Yes — open source | AI chatbots, streaming responses |
| 18 | **Appwrite** | [appwrite.io](https://appwrite.io) | Open-source BaaS — Auth, DB, Storage, Functions | Yes — self-hostable, free cloud tier | Privacy-focused projects |
| 19 | **TypeScript** | [typescriptlang.org](https://www.typescriptlang.org) | JavaScript with types — catches bugs before runtime | Yes — open source | Any project where you don't want runtime surprises |
| 20 | **Postman** | [postman.com](https://www.postman.com) | API testing and collaboration platform | Yes — free plan | Testing your API endpoints |

---

## Frameworks & Libraries

Pick the right stack before you start coding. The framework you choose will determine how fast you can ship.

### JavaScript / TypeScript

| Framework | Link | One-Line Description | Free Tier | Hackathon Score |
|-----------|------|----------------------|-----------|-----------------|
| **React** | [react.dev](https://react.dev) | Component-based UI library — the industry standard | Open source | ⭐⭐⭐⭐⭐ |
| **Next.js** | [nextjs.org](https://nextjs.org) | React framework with SSR, API routes, and file-based routing | Open source | ⭐⭐⭐⭐⭐ |
| **Vue.js** | [vuejs.org](https://vuejs.org) | Progressive framework — easy to learn, powerful to use | Open source | ⭐⭐⭐⭐ |
| **Svelte** | [svelte.dev](https://svelte.dev) | Compiles away the framework — tiny bundles, fast runtime | Open source | ⭐⭐⭐⭐ |
| **SvelteKit** | [kit.svelte.dev](https://kit.svelte.dev) | Full-stack Svelte with SSR, routing, and deployments | Open source | ⭐⭐⭐⭐ |
| **Astro** | [astro.build](https://astro.build) | Multi-framework UI — ship zero JS by default, island architecture | Open source | ⭐⭐⭐⭐ |
| **Express** | [expressjs.com](https://expressjs.com) | Minimalist Node.js web framework — the classic | Open source | ⭐⭐⭐⭐ |
| **Fastify** | [fastify.io](https://fastify.io) | Fast, low-overhead Node.js framework — 2x faster than Express | Open source | ⭐⭐⭐⭐ |
| **Hono** | [hono.dev](https://hono.dev) | Ultra-fast web framework for edge runtimes — Cloudflare, Deno, Bun | Open source | ⭐⭐⭐⭐ |
| **Bun** | [bun.sh](https://bun.sh) | All-in-one JS runtime — faster npm install, faster bundler, faster everything | Open source | ⭐⭐⭐⭐ |

### Python

| Framework | Link | One-Line Description | Free Tier | Hackathon Score |
|-----------|------|----------------------|-----------|-----------------|
| **FastAPI** | [fastapi.tiangolo.com](https://fastapi.tiangolo.com) | Modern Python web framework — automatic docs, type hints, async | Open source | ⭐⭐⭐⭐⭐ |
| **Flask** | [flask.palletsprojects.com](https://flask.palletsprojects.com) | Lightweight Python framework — minimal boilerplate | Open source | ⭐⭐⭐⭐ |
| **Django** | [djangoproject.com](https://www.djangoproject.com) | "Batteries included" Python framework — ORM, auth, admin panel built in | Open source | ⭐⭐⭐ |
| **Streamlit** | [streamlit.io](https://streamlit.io) | Turn Python scripts into web apps in minutes — perfect for ML demos | Yes — free tier | ⭐⭐⭐⭐⭐ |
| **Gradio** | [gradio.app](https://www.gradio.app) | Build ML demos with a few lines of Python — integrates with Hugging Face | Yes — free tier | ⭐⭐⭐⭐ |
| **Litestar** | [litestar.dev](https://litestar.dev) | High-performance Python API framework — type-safe, fast | Open source | ⭐⭐⭐ |

### Mobile

| Framework | Link | One-Line Description | Free Tier | Hackathon Score |
|-----------|------|----------------------|-----------|-----------------|
| **React Native** | [reactnative.dev](https://reactnative.dev) | Build native iOS/Android with React — biggest community | Open source | ⭐⭐⭐⭐ |
| **Expo** | [expo.dev](https://expo.dev) | Managed React Native — OTA updates, EAS Build, push notifications | Yes — free tier | ⭐⭐⭐⭐⭐ |
| **Flutter** | [flutter.dev](https://flutter.dev) | Google's UI toolkit — beautiful apps, one codebase | Open source | ⭐⭐⭐⭐ |
| **Capacitor** | [capacitorjs.com](https://capacitorjs.com) | Turn any web app into a native mobile app — Ionic's secret weapon | Open source | ⭐⭐⭐ |

---

## Backend & Database Services

The comparison you actually need. No more "which BaaS should I use" debates at 2 AM.

| Service | Auth | Database | Storage | Real-Time | Free Tier Limits | Best For |
|---------|------|----------|---------|-----------|------------------|----------|
| **Supabase** | ✅ Built-in | ✅ Postgres | ✅ S3-backed | ✅ Realtime subscriptions | 500MB DB, 1GB storage, 50K MAU | Full-stack apps, Postgres fans |
| **Firebase** | ✅ Google/Email/Phone | ✅ Firestore (NoSQL) | ✅ Cloud Storage | ✅ Firestore realtime | 1GB storage, 1GB/day data transfer | Rapid prototyping, mobile apps |
| **Appwrite** | ✅ Built-in | ✅ MariaDB | ✅ S3-compatible | ✅ Realtime | Self-host free, cloud free tier | Privacy-first, self-hostable |
| **PocketBase** | ✅ Built-in | ✅ SQLite | ✅ Local file system | ✅ SSE subscriptions | Free — single binary, self-host | Offline-first, simple backends |
| **Neon** | ❌ (use Clerk/Auth.js) | ✅ Serverless Postgres | ❌ | ❌ | 0.5GB storage, 1 compute unit | Serverless Postgres without the hassle |
| **PlanetScale** | ❌ (use Clerk/Auth.js) | ✅ Serverless MySQL | ❌ | ❌ | 5GB storage, 1B reads/month | MySQL without managing servers |
| **MongoDB Atlas** | ❌ (use Clerk/Auth.js) | ✅ Document DB | ✅ GridFS | ✅ Change streams | 512MB storage, shared cluster | Document-heavy, flexible schemas |
| **Railway** | ❌ | ✅ Postgres/MySQL/Redis | ❌ | ❌ | $5 credit/month | Backend hosting + databases together |
| **Render** | ❌ | ✅ Postgres/Redis | ❌ | ❌ | 750 hours/month | Simple backend hosting |
| **Turso** | ❌ | ✅ LibSQL (edge SQLite) | ❌ | ❌ | 500 databases, 9GB storage | Edge databases, low latency |

### Quick Decision Guide

- **Need everything in one place?** → Supabase or Firebase
- **Want Postgres without the ops?** → Neon or Supabase
- **Building a simple prototype?** → PocketBase (single binary, done)
- **Need self-hosting?** → Appwrite or PocketBase
- **Just need a database?** → Neon (Postgres) or PlanetScale (MySQL)
- **Building mobile?** → Firebase (great mobile SDKs) or Supabase

---

## AI & ML APIs

Every hackathon in 2025+ has an AI component. Here's how to pick the right API.

| API | Model Access | Free Credits | Rate Limits | Best Use Case |
|-----|-------------|--------------|-------------|---------------|
| **OpenAI** | GPT-4o, GPT-4o-mini, DALL-E 3, Whisper, TTS | $5 on signup | 10K RPM (varies by model) | General AI features, image generation, transcription |
| **Anthropic Claude** | Claude 4 Sonnet, Claude 4 Opus | $5 on signup | Varies by tier | Long-context reasoning, code generation |
| **Google Gemini** | Gemini 2.5 Pro, Gemini 2.5 Flash | Free tier available | 15 RPM (free) | Multimodal AI, Google ecosystem integration |
| **Groq** | Llama 3.1, Mixtral, Gemma (hosted) | Free tier with limits | 30 RPM (free) | Ultra-fast inference — lowest latency |
| **OpenRouter** | Access to 100+ models via one API | $1 free credit | Varies by model | Model comparison, trying multiple providers |
| **Hugging Face** | Open-source models via Inference API | Free tier available | Rate limited | Open-source models, custom fine-tuning |
| **Replicate** | Run open-source models via API | $5 free credit | Varies | Image/video generation (Stable Diffusion, etc.) |
| **Together AI** | Llama, Mixtral, other open models | $5 free credit | 60 RPM | Cost-effective open-source model hosting |
| **Mistral AI** | Mistral Large, Mistral Small, Codestral | Free tier available | 1 RPM (free) | European AI, code generation |
| **Cohere** | Command R+, Embed, Rerank | Free tier available | 1K calls/month | RAG pipelines, semantic search |

### Quick Decision Guide

- **Just need ChatGPT-like features?** → OpenAI (most documentation, easiest to use)
- **Need fast responses?** → Groq (10x faster than OpenAI for inference)
- **Building a RAG pipeline?** → Cohere (best embedding/rerank models) or OpenAI
- **Want to try open-source models?** → Hugging Face or Together AI
- **Budget constrained?** → Groq free tier or OpenRouter (mix and match)
- **Building for Europe?** → Mistral (GDPR-friendly)

---

## Deployment Platforms

Ship it or it didn't happen. These platforms will get your project live before judging starts.

| Platform | Frontend | Backend | Databases | Free Tier | Deploy Speed | Best For |
|----------|----------|---------|-----------|-----------|--------------|----------|
| **Vercel** | ✅ Excellent | ✅ Serverless functions | ❌ (use Supabase) | 100GB bandwidth, 100 build hours | Instant | Next.js, React, any frontend |
| **Netlify** | ✅ Excellent | ✅ Serverless functions | ❌ (use Supabase) | 100GB bandwidth, 300 build mins | Instant | Static sites, JAMstack |
| **Cloudflare Pages** | ✅ Excellent | ✅ Workers | ✅ D1, KV, R2 | Unlimited bandwidth, 500 builds/month | Instant | Global edge, best free bandwidth |
| **Railway** | ✅ | ✅ Full servers | ✅ Postgres, MySQL, Redis | $5 credit/month | ~30 seconds | Full-stack apps with databases |
| **Render** | ✅ | ✅ Web services | ✅ Postgres, Redis | 750 hours/month | ~1 minute | Simple deployments |
| **Fly.io** | ✅ | ✅ Full containers | ❌ (use Supabase) | 3 shared VMs | ~2 minutes | Container apps, global distribution |
| **DigitalOcean App Platform** | ✅ | ✅ | ✅ Managed DBs | $200 free credit (students) | ~2 minutes | Production-ready deployments |
| **Deno Deploy** | ✅ | ✅ Edge functions | ✅ KV store | 100K requests/day | Instant | Deno, TypeScript at the edge |

### Quick Decision Guide

- **Frontend only?** → Vercel (best DX) or Cloudflare Pages (best free tier)
- **Full-stack with database?** → Railway or Render
- **Need global edge?** → Cloudflare Pages + Workers
- **Student with DigitalOcean credits?** → DigitalOcean App Platform
- **Using Deno?** → Deno Deploy (obviously)

---

## Design & UI Resources

Good design is the difference between "cool project" and "this could be a real product." These tools save hours.

| Resource | What It Is | Hackathon Rating | Time Saved |
|----------|------------|------------------|------------|
| **Figma** | Collaborative design tool — wireframes, prototypes, mockups | ⭐⭐⭐⭐⭐ | 3-5 hours on design |
| **Tailwind CSS** | Utility-first CSS — build any design without leaving your HTML | ⭐⭐⭐⭐⭐ | 5-8 hours on styling |
| **shadcn/ui** | Beautiful, accessible React components — copy-paste, not install | ⭐⭐⭐⭐⭐ | 4-6 hours on UI components |
| **Radix UI** | Unstyled, accessible primitives — pair with Tailwind for custom designs | ⭐⭐⭐⭐ | 3-4 hours on accessibility |
| **Aceternity UI** | Beautiful, animated React components — modern SaaS look | ⭐⭐⭐⭐ | 2-3 hours on animations |
| **Magic UI** | Animated components and copy-paste effects for React | ⭐⭐⭐⭐ | 2-3 hours on micro-interactions |
| **Chakra UI** | Simple, modular, accessible React components | ⭐⭐⭐ | 3-4 hours on component scaffolding |
| **Material UI (MUI)** | React components implementing Material Design — battle-tested | ⭐⭐⭐ | 3-4 hours on enterprise-style UIs |
| **NextUI** | Beautiful, fast, modern React UI library | ⭐⭐⭐⭐ | 2-3 hours on sleek interfaces |
| **DaisyUI** | Tailwind CSS component library — class-based, themeable | ⭐⭐⭐⭐ | 2-3 hours on rapid prototyping |
| **Framer Motion** | Production-ready animation library for React | ⭐⭐⭐⭐ | 2-3 hours on smooth animations |
| **Animate.css** | Ready-to-use CSS animations | ⭐⭐⭐ | 1 hour on entrance/exit animations |
| **Heroicons** | Hand-crafted SVG icons by the Tailwind CSS team | ⭐⭐⭐⭐ | 30 minutes on icon selection |
| **Refactoring UI** | Practical design tips for developers — not a tool, but a mindset shift | ⭐⭐⭐⭐⭐ | Permanent improvement |

### Pro Tips

- **shadcn/ui + Tailwind** is the fastest combo for hackathons — you get beautiful, accessible components without fighting CSS.
- **Aceternity UI** or **Magic UI** for "wow factor" on your landing page — judges notice polish.
- **Don't over-design.** Pick a clean base (shadcn/ui) and add one "wow" element (animated hero).

---

## Free Stock Assets

Never waste time searching for "free images" at 3 AM. These are all you need.

### Images

| Source | URL | What It Offers | License |
|--------|-----|----------------|---------|
| **Unsplash** | [unsplash.com](https://unsplash.com) | 3M+ high-res photos | Free for commercial use |
| **Pexels** | [pexels.com](https://pexels.com) | Photos and videos | Free for commercial use |
| **Pixabay** | [pixabay.com](https://pixabay.com) | Photos, vectors, illustrations, videos | Free for commercial use |
| **StockSnap** | [stocksnap.io](https://stocksnap.io) | Beautiful free stock photos | CC0 — no attribution needed |

### Icons

| Source | URL | Style | Format |
|--------|-----|-------|--------|
| **Lucide** | [lucide.dev](https://lucide.dev) | Clean, consistent | SVG, React components |
| **Heroicons** | [heroicons.com](https://heroicons.com) | Outlined and filled | SVG, React components |
| **Phosphor Icons** | [phosphoricons.com](https://phosphoricons.com) | Flexible weight system | SVG, React, Vue, Svelte |
| **Iconoir** | [iconoir.com](https://iconoir.com) | Open-source, 1500+ icons | SVG, React, Figma |
| **Tabler Icons** | [tabler.io/icons](https://tabler.io/icons) | 5000+ open-source icons | SVG, React, Vue |

### Fonts

| Source | URL | What It Offers |
|--------|-----|----------------|
| **Google Fonts** | [fonts.google.com](https://fonts.google.com) | 1500+ free font families — the standard |
| **Font Share** | [fontshare.com](https://fontshare.com) | Trendy, free fonts for designers |
| **Variable Fonts** | [v-fonts.com](https://v-fonts.com) | Curated variable fonts — one file, any weight |

### Illustrations

| Source | URL | Style |
|--------|-----|-------|
| **unDraw** | [undraw.co](https://undraw.co) | Open-source illustrations, customizable colors |
| **Humaaans** | [humaaans.com](https://www.humaaans.com) | Mix-and-match people illustrations |
| **Storyset** | [storyset.com](https://storyset.com) | Free customizable illustrations by Freepik |
| **LottieFiles** | [lottiefiles.com](https://lottiefiles.com) | Animated illustrations — lightweight JSON |
| **Blush** | [blush.design](https://blush.design) | Create custom illustrations with AI |

### Colors

| Source | URL | What It Does |
|--------|-----|--------------|
| **Coolors** | [coolors.co](https://coolors.co) | Color palette generator — spacebar to generate |
| **Realtime Colors** | [realtimecolors.com](https://realtimecolors.com) | See your palette on a real UI in real-time |
| **ColorHunt** | [colorhunt.co](https://colorhunt.co) | Curated color palettes — filter by mood |
| **Huemint** | [huemint.com](https://huemint.com) | AI-powered brand color generator |

---

## API Discovery Platforms

Need an API for your hackathon? Don't waste time Googling. Start here.

| Platform | URL | What It Does | Best For |
|----------|-----|--------------|----------|
| **RapidAPI** | [rapidapi.com](https://rapidapi.com) | World's largest API marketplace — 40K+ APIs | Finding any API you can think of |
| **API Ninjas** | [api-ninjas.com](https://api-ninjas.com) | Curated collection of free, useful APIs | Quick API lookups, trivia, weather |
| **Public APIs** | [publicapis.io](https://publicapis.io) | Directory of free public APIs | Discovering free APIs by category |
| **APIs.guru** | [apis.guru](https://apis.guru) | Wikipedia of APIs — OpenAPI specs for popular services | Understanding API schemas |
| **Todd Motto APIs List** | [github.com/toddmotto/public-apis](https://github.com/toddmotto/public-apis) | Community-curated list of free APIs | Browsing by category |
| **API List** | [apilist.fun](https://apilist.fun) | Curated, searchable API directory | Modern API discovery |

### Quick Tips

- **Always check rate limits first.** A free API with 100 requests/day is useless for a hackathon demo.
- **Prefer REST over GraphQL** for hackathons — less setup, faster to prototype.
- **Cache responses** during development so you don't burn through API quotas.

---

## Hackathon Platforms

Where the magic happens. Each platform has its own culture, judging criteria, and prize structure.

| Platform | URL | Focus Area | Typical Prize Pool | Best Strategy |
|----------|-----|------------|-------------------|---------------|
| **Devfolio** | [devfolio.co](https://devfolio.co) | Web3, blockchain, crypto | $10K-$100K+ per hackathon | Build on Ethereum/L2, focus on DeFi or NFT utility |
| **Devpost** | [devpost.com](https://devpost.com) | General — university hackathons | $5K-$50K | Build something judges can demo in 2 minutes |
| **MLH** | [mlh.io](https://mlh.io) | University hackathons worldwide | Varies by event | Network hard, attend workshops, win sponsor prizes |
| **DoraHacks** | [dorahacks.io](https://dorahacks.io) | Web3, open source, public goods | $5K-$50K | Focus on real utility, not just tokens |
| **ETHGlobal** | [ethglobal.com](https://ethglobal.com) | Ethereum ecosystem | $50K-$1M+ | Build on Ethereum, chainlink, or IPFS — deep Web3 integration |
| **HackerEarth** | [hackerearth.com](https://hackerearth.com) | Enterprise, AI/ML, blockchain | $5K-$30K | Solve a real business problem, not just a cool tech demo |
| **AngelHack** | [angelhack.com](https://angelhack.com) | Global hackathons, startup-focused | $5K-$20K | Build a MVP that looks like a real startup |
| **Kaggle** | [kaggle.com](https://kaggle.com) | Data science, ML competitions | $5K-$100K+ | High accuracy + clear methodology + good writeup |
| **HackMIT** | [hackmit.org](https://hackmit.org) | Elite university hackathon | Sponsor prizes | Build something technically impressive |
| **TreeHacks** | [treehacks.com](https://treehacks.com) | Stanford's hackathon | Sponsor prizes | Focus on innovation and technical depth |

### Platform-Specific Tips

- **Devfolio**: Web3 projects dominate. If you're building Web3, integrate at least one blockchain.
- **Devpost**: The submission page matters — good demo video + clear README = more judging points.
- **MLH**: Attend the pre-hackathon workshops — they often reveal sponsor-specific prizes.
- **Kaggle**: The notebook quality matters as much as the score. Explain your methodology.

---

## Learning Resources

Learn fast, build faster. These resources are specifically useful for hackathon prep.

### YouTube Channels

| Channel | URL | What They Teach | Watch When |
|---------|-----|----------------|------------|
| **Fireship** | [youtube.com/@Fireship](https://youtube.com/@Fireship) | Quick tech explainers, framework comparisons, coding trends | You need to learn a new tool in 100 seconds |
| **Traversy Media** | [youtube.com/@TraversyMedia](https://youtube.com/@TraversyMedia) | Full tutorials, crash courses, project builds | You need a structured project tutorial |
| **Web Dev Simplified** | [youtube.com/@WebDevSimplified](https://youtube.com/@WebDevSimplified) | Clear, concise web dev tutorials | You need to understand a concept quickly |
| **The Net Ninja** | [youtube.com/@NetNinja](https://youtube.com/@NetNinja) | Full course playlists — React, Vue, Node, Firebase | You need a complete course on a topic |
| **Jack Herrington** | [youtube.com/@Jack_Herrington](https://youtube.com/@Jack_Herrington) | Advanced React, Next.js, performance tips | You need to level up your React skills |
| **Theo** | [youtube.com/@t3dotgg](https://youtube.com/@t3dotgg) | Hot takes on web dev, framework comparisons | You need to decide between frameworks |
| **Web Dev Cody** | [youtube.com/@WebDevCody](https://youtube.com/@WebDevCody) | Full-stack project tutorials, honest reviews | You want real-world project walkthroughs |
| **ByteGrad** | [youtube.com/@ByteGrad](https://youtube.com/@ByteGrad) | Next.js and React tutorials | You're building with Next.js |

### Course Platforms

| Platform | URL | What It Offers | Cost |
|----------|-----|----------------|------|
| **freeCodeCamp** | [freecodecamp.org](https://www.freecodecamp.org) | Full curriculum — frontend, backend, data science | 100% free |
| **The Odin Project** | [theodinproject.com](https://www.theodinproject.com) | Full-stack JavaScript curriculum — project-based | 100% free |
| **CS50** | [cs50.harvard.edu](https://cs50.harvard.edu) | Harvard's intro to CS — best CS course online | Free (certificate $149) |
| **FullStackOpen** | [fullstackopen.com](https://fullstackopen.com) | University of Helsinki — modern full-stack dev | 100% free |
| **Codecademy** | [codecademy.com](https://www.codecademy.com) | Interactive coding lessons — many languages | Free tier available |
| **Exercism** | [exercism.org](https://exercism.org) | Practice problems with mentor feedback | 100% free |

### Documentation Sites (Bookmark These)

| Site | URL | Why It's Essential |
|------|-----|-------------------|
| **MDN Web Docs** | [developer.mozilla.org](https://developer.mozilla.org) | The definitive web reference — if MDN doesn't know, it doesn't exist |
| **Next.js Docs** | [nextjs.org/docs](https://nextjs.org/docs) | Best framework docs — clear examples, great DX |
| **Supabase Docs** | [supabase.com/docs](https://supabase.com/docs) | Excellent docs with copy-paste code snippets |
| **Tailwind CSS Docs** | [tailwindcss.com/docs](https://tailwindcss.com/docs) | Searchable, visual, instant — how docs should be |
| **FastAPI Docs** | [fastapi.tiangolo.com](https://fastapi.tiangolo.com) | Tutorial-driven — read the tutorial, you'll be productive |
| **Vercel Docs** | [vercel.com/docs](https://vercel.com/docs) | Clear deployment guides for every framework |
| **Firebase Docs** | [firebase.google.com/docs](https://firebase.google.com/docs) | Comprehensive — intimidating but thorough |

---

## Communities & Discord Servers

Hackathons are better with people. These communities will help you find teammates, get unstuck, and stay motivated.

### Discord Servers

| Community | URL | Focus | Why Join |
|-----------|-----|-------|----------|
| **MLH Community** | [mlh.io/community](https://mlh.io/community) | Hackathons, student developers | Team matching, hackathon announcements |
| **Reactiflux** | [reactiflux.com](https://reactiflux.com) | React ecosystem | 200K+ members — fastest React help you'll find |
| **Python Discord** | [pythondiscord.com](https://pythondiscord.com) | Python development | 500K+ members — helpful, active community |
| **Tailwind CSS** | [tailwindcss.com/community](https://tailwindcss.com/community) | Tailwind CSS | Design help, component sharing |
| **Supabase** | [supabase.com/community](https://supabase.com/community) | Supabase, Postgres, Auth | Direct help from Supabase team members |
| **Vercel** | [vercel.com/community](https://vercel.com/community) | Next.js, Vercel deployment | Framework help, deployment issues |
| **AI Engineer** | [ai.engineer](https://ai.engineer) | AI/ML engineering | Building AI products, prompt engineering |
| **Open Source AI** | Various | Open-source AI models | Model deployment, fine-tuning help |

### Reddit Communities

| Subreddit | URL | Members | What You'll Find |
|-----------|-----|---------|------------------|
| **r/hackathons** | [reddit.com/r/hackathons](https://reddit.com/r/hackathons) | 50K+ | Hackathon announcements, team finding, post-hack retrospectives |
| **r/webdev** | [reddit.com/r/webdev](https://reddit.com/r/webdev) | 2M+ | Trends, portfolio reviews, career advice |
| **r/learnprogramming** | [reddit.com/r/learnprogramming](https://reddit.com/r/learnprogramming) | 4M+ | Beginner help, resource recommendations |
| **r/nextjs** | [reddit.com/r/nextjs](https://reddit.com/r/nextjs) | 100K+ | Next.js specific help and discussions |
| **r/reactjs** | [reddit.com/r/reactjs](https://reddit.com/r/reactjs) | 800K+ | React ecosystem, component patterns |
| **r/LocalLLaMA** | [reddit.com/r/LocalLLaMA](https://reddit.com/r/LocalLLaMA) | 200K+ | Running open-source LLMs locally |
| **r/SideProject** | [reddit.com/r/SideProject](https://reddit.com/r/SideProject) | 300K+ | Show your project, get feedback |

### Other Communities

| Community | URL | What It Is |
|-----------|-----|------------|
| **Dev.to** | [dev.to](https://dev.to) | Developer blogging platform — write about your hackathon |
| **Hashnode** | [hashnode.com](https://hashnode.com) | Developer blogs with custom domains |
| **Product Hunt** | [producthunt.com](https://producthunt.com) | Launch your hackathon project to the world |
| **Indie Hackers** | [indiehackers.com](https://www.indiehackers.com) | Startup community — post your project, get feedback |

---

## Newsletters & Update Sources

Stay informed without doom-scrolling Twitter. Curated knowledge, delivered to your inbox.

### Hackathon & Developer Newsletters

| Newsletter | URL | Frequency | What You Get |
|------------|-----|-----------|--------------|
| **MLH Newsletter** | [mlh.io/newsletter](https://mlh.io/newsletter) | Weekly | Upcoming hackathons, tips, opportunities |
| **Hacker Newsletter** | [hackernewsletter.com](https://hackernewsletter.com) | Weekly | Best Hacker News stories — curated, not overwhelming |
| **ByteByteGo** | [blog.bytebytego.com](https://blog.bytebytego.com) | Weekly | System design concepts, architecture diagrams |
| **TLDR Newsletter** | [tldr.tech](https://tldr.tech) | Daily | Tech news in 5 minutes — no fluff |
| **The Pragmatic Engineer** | [newsletter.pragmaticengineer.com](https://newsletter.pragmaticengineer.com) | Weekly | Deep dives into engineering culture and practices |
| **Frontend Focus** | [frontendfoc.us](https://frontendfoc.us) | Weekly | Frontend news, tutorials, tools |

### AI & ML Newsletters

| Newsletter | URL | Frequency | What You Get |
|------------|-----|-----------|--------------|
| **The Batch** | [deeplearning.ai/the-batch](https://www.deeplearning.ai/the-batch) | Weekly | Andrew Ng's AI news digest |
| **Ben's Bites** | [bensbites.beehiiv.com](https://bensbites.beehiiv.com) | Daily | AI news, tools, and tutorials |
| **AI Tool Report** | [aitoolreport.com](https://aitoolreport.com) | Weekly | AI tools and use cases |

### Startup & Product Newsletters

| Newsletter | URL | Frequency | What You Get |
|------------|-----|-----------|--------------|
| **Morning Brew** | [morningbrew.com](https://morningbrew.com) | Daily | Business news in a fun, digestible format |
| **Product Hunt Daily** | [producthunt.com/newsletter](https://producthunt.com/newsletter) | Daily | Top products launched today |
| **This Week in Startups** | [thisweekinstartups.com](https://thisweekinstartups.com) | Weekly | Startup ecosystem news |

---

## Tools for Productivity

Hackathons are a sprint. These tools keep you organized and focused when everything is chaos.

| Tool | URL | What It Does | Hackathon Use |
|------|-----|--------------|---------------|
| **Notion** | [notion.so](https://notion.so) | All-in-one workspace — docs, databases, kanban boards | Project planning, meeting notes, task tracking |
| **Linear** | [linear.app](https://linear.app) | Issue tracking — fast, beautiful, keyboard-driven | Task management, bug tracking |
| **Figma** | [figma.com](https://figma.com) | Collaborative design | UI mockups, quick wireframes |
| **Miro** | [miro.com](https://miro.com) | Online whiteboard | Brainstorming, architecture planning |
| **Excalidraw** | [excalidraw.com](https://excalidraw.com) | Hand-drawn style diagrams | Quick sketches, pitch diagrams |
| **Screen Studio** | [screen.studio](https://screen.studio) | Screen recording with zoom effects | Demo video recording |
| **OBS Studio** | [obsproject.com](https://obsproject.com) | Free, open-source screen recording | Live demos, presentation recording |
| **Loom** | [loom.com](https://loom.com) | Quick video messages | Team communication, async updates |
| **Clockify** | [clockify.me](https://clockify.me) | Time tracking | Know where your hackathon hours go |
| **Tldraw** | [tldraw.com](https://tldraw.com) | Simple drawing tool | Quick diagrams, visual communication |

### Productivity Tips

- **Use Notion for project docs.** Create a template before the hackathon: idea, team roles, timeline, deployment checklist.
- **Excalidraw for architecture.** Draw your system diagram in 5 minutes — judges love seeing you thought about architecture.
- **Record your demo early.** Don't wait until the last hour. Record a rough demo video as soon as you have something working.

---

## Chrome Extensions for Hackathons

These extensions save minutes that add up to hours over a weekend.

| Extension | What It Does | Why You Need It |
|-----------|--------------|-----------------|
| **Wappalyzer** | Identify technologies on any website | See what frameworks/tools a competitor is using |
| **WhatFont** | Identify fonts on any website | "What font is that?" — answered instantly |
| **ColorZilla** | Color picker and gradient generator | Grab exact colors from any website |
| **Lighthouse** | Google's performance/SEO/accessibility audit | Make sure your project scores well before submission |
| **JSON Formatter** | Pretty-print JSON responses | Read API responses without going blind |
| **React Developer Tools** | Inspect React component tree | Debug component state and props |
| **Vue.js Devtools** | Inspect Vue component tree | Same as above, but for Vue |
| **Responsive Viewer** | View multiple screen sizes at once | Check responsive design without resizing |
| **GitHub File Navigator** | Browse GitHub repos without cloning | Quickly check dependencies and code patterns |
| **Dark Reader** | Dark mode for every website | Save your eyes during a 48-hour hackathon |

---

## My Personal Stack

If I could only use 10 tools for a hackathon, these are the ones I'd pick. No hesitation.

1. **Next.js** — Frontend framework. File-based routing, API routes, SSR. Done.
2. **Supabase** — Backend-as-a-service. Auth, database, storage, realtime. One dependency.
3. **Tailwind CSS + shadcn/ui** — Styling. Beautiful UI in minutes, not hours.
4. **Vercel** — Deployment. Git push, done. Zero config.
5. **OpenAI API** — AI features. GPT-4o for text, DALL-E for images.
6. **Figma** — Design. Quick wireframes before coding.
7. **Excalidraw** — Architecture diagrams. Pitch deck visuals.
8. **Notion** — Project management. Team sync, notes, timeline.
9. **GitHub Copilot** — Code generation. Autocomplete everything.
10. **Loom** — Demo recording. Quick video for submission.

### Why This Stack?

- **Speed**: You can go from zero to deployed in under 30 minutes.
- **Simplicity**: One framework (Next.js), one backend (Supabase), one deploy target (Vercel).
- **AI-powered**: Copilot writes code, OpenAI powers features, you orchestrate.
- **Presentation**: Figma for design, Excalidraw for diagrams, Loom for demos.

---

## How to Use This Resource Hub

This is a lot of information. Here's how to actually use it without getting overwhelmed.

### Before the Hackathon

1. **Bookmark 5-10 resources** from the Essential section. Don't bookmark everything — you won't use it all.
2. **Set up your stack** using the Frameworks section. Pick Next.js + Supabase + Tailwind if you're unsure.
3. **Deploy a test project** on Vercel. Make sure your deployment pipeline works before the clock starts.
4. **Get your API keys** ready. OpenAI, Supabase, whatever you need. Create accounts now, not during the hackathon.
5. **Join 2-3 Discord servers** from the Communities section. Find teammates early.

### During the Hackathon

1. **Don't browse this list.** You should know your tools before you start.
2. **Use the Deployment section** only if you're stuck on hosting.
3. **Use the AI section** if you need to add AI features quickly.
4. **Use the Design section** if your UI looks bad and you need a quick fix.
5. **Use the Asset section** if you need images, icons, or fonts — don't waste time searching Google.

### After the Hackathon

1. **Write about it.** Use the Learning Resources section to improve, then blog about your experience.
2. **Submit to more hackathons.** Use the Hackathon Platforms section to find your next one.
3. **Update your stack.** Swap out tools that didn't work, add ones that did.

### The Golden Rule

> **Don't let tool selection become procrastination.** Pick your stack in 30 minutes. If it works, use it. If it doesn't, you have 47.5 hours left.

---

*Last updated: September 2026. If something is broken or outdated, open an issue or PR.*
