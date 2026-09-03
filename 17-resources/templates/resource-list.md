# Hackathon Resource List

Curated tools, frameworks, APIs, and communities for hackathon builders. Each entry includes what it does, whether it's free, when to use it, and what to use instead.

---

## Frontend Frameworks

| Name | Link | What It Does | Free Tier | Best Use Case | Rating | Alternative |
|------|------|-------------|-----------|---------------|--------|-------------|
| Next.js | https://nextjs.org | React framework with SSR, API routes, file-based routing | Free (open source) | Full-stack web apps, landing pages, dashboards | 5/5 | Remix |
| React | https://reactjs.org | UI library for building component-based interfaces | Free (open source) | Any frontend project | 5/5 | Vue.js |
| Vue.js | https://vuejs.org | Progressive framework for building UIs | Free (open source) | Quick prototypes, simpler projects | 4/5 | Svelte |
| Svelte | https://svelte.dev | Compiler that produces vanilla JS — no virtual DOM | Free (open source) | Lightweight apps, performance-critical UIs | 4/5 | Alpine.js |
| Tailwind CSS | https://tailwindcss.com | Utility-first CSS framework for rapid styling | Free (open source) | Any project needing fast, clean styling | 5/5 | Bootstrap |
| shadcn/ui | https://ui.shadcn.com | Copy-paste React components built on Radix + Tailwind | Free (open source) | Quick UI with professional look | 5/5 | Chakra UI |
| Framer Motion | https://www.framer.com/motion | Animation library for React | Free (open source) | Smooth transitions, micro-interactions | 4/5 | React Spring |

## Backend Frameworks

| Name | Link | What It Does | Free Tier | Best Use Case | Rating | Alternative |
|------|------|-------------|-----------|---------------|--------|-------------|
| FastAPI | https://fastapi.tiangolo.com | Python API framework with auto-docs and type validation | Free (open source) | Python backends, ML model serving | 5/5 | Flask |
| Express.js | https://expressjs.com | Minimal Node.js web framework | Free (open source) | REST APIs, simple backends | 4/5 | Fastify |
| Django | https://www.djangoproject.com | Full-featured Python framework with ORM, admin, auth | Free (open source) | Complex apps needing built-in features | 4/5 | Flask |
| Flask | https://flask.palletsprojects.com | Lightweight Python micro-framework | Free (open source) | Small APIs, quick prototypes | 4/5 | FastAPI |
| Hono | https://hono.dev | Ultrafast web framework for edge runtimes | Free (open source) | Edge computing, Cloudflare Workers | 4/5 | Express.js |
| Gin | https://gin-gonic.com | Fast Go HTTP framework | Free (open source) | High-performance APIs in Go | 4/5 | Echo |

## Databases

| Name | Link | What It Does | Free Tier | Best Use Case | Rating | Alternative |
|------|------|-------------|-----------|---------------|--------|-------------|
| Supabase | https://supabase.com | Open source Firebase alternative with Postgres | 500MB free, 50K monthly active users | Real-time apps, auth + DB in one | 5/5 | Firebase |
| PlanetScale | https://planetscale.com | Serverless MySQL platform with branching | 5GB free, 1B reads/month | Apps needing MySQL, schema branching | 4/5 | Neon |
| Neon | https://neon.tech | Serverless Postgres with branching | 512MB free, 24/7 compute | Postgres apps needing scale | 4/5 | Supabase |
| Firebase | https://firebase.google.com | Google's app platform (Firestore, Auth, Functions) | Generous free tier | Quick MVPs, real-time sync | 4/5 | Supabase |
| MongoDB Atlas | https://www.mongodb.com/atlas | Cloud MongoDB with free tier | 512MB free | Document-heavy apps, flexible schemas | 4/5 | Supabase |
| Turso | https://turso.tech | SQLite for the edge — embedded replicas | 500 databases, 9GB storage | Edge apps, offline-first, local-first | 4/5 | Cloudflare D1 |
| Redis | https://redis.com | In-memory data store for caching and queues | 30MB free on Redis Cloud | Caching, rate limiting, sessions | 5/5 | Valkey |

## Authentication

| Name | Link | What It Does | Free Tier | Best Use Case | Rating | Alternative |
|------|------|-------------|-----------|---------------|--------|-------------|
| NextAuth.js | https://next-auth.js.org | Authentication for Next.js with 50+ providers | Free (open source) | Next.js apps needing social login | 5/5 | Clerk |
| Clerk | https://clerk.com | Drop-in auth UI and API for React | 10K monthly active users free | Quick auth with beautiful UI | 5/5 | NextAuth.js |
| Auth0 | https://auth0.com | Enterprise-grade identity platform | 7,500 free active users | Production apps needing SSO/SAML | 4/5 | Clerk |
| Supabase Auth | https://supabase.com/auth | Built-in auth for Supabase projects | Included with Supabase free tier | Apps already using Supabase | 4/5 | NextAuth.js |

## AI / ML APIs

| Name | Link | What It Does | Free Tier | Best Use Case | Rating | Alternative |
|------|------|-------------|-----------|---------------|--------|-------------|
| OpenAI API | https://platform.openai.com | GPT-4, DALL-E, Whisper, embeddings | $5 free credit (new accounts) | Text generation, vision, embeddings | 5/5 | Anthropic Claude |
| Anthropic Claude | https://console.anthropic.com | Claude 3.5 Sonnet, Opus, Haiku | Free tier available | Long-context analysis, coding | 5/5 | OpenAI |
| Google Gemini | https://ai.google.dev | Google's multimodal AI models | Free tier with rate limits | Multimodal tasks (text + image + audio) | 4/5 | OpenAI |
| Hugging Face | https://huggingface.co | Open source model hub + inference API | Free tier for inference | Running open source models | 4/5 | Replicate |
| Replicate | https://replicate.com | Run open source models via API | Free tier available | Image gen, speech, niche models | 4/5 | Hugging Face |
| Groq | https://groq.com | Ultra-fast LLM inference (Llama, Mixtral) | Free tier with rate limits | Speed-critical AI features | 5/5 | Together AI |
| Together AI | https://together.ai | Run open source models at scale | $5 free credit | Fine-tuning, custom models | 4/5 | Groq |

## Hosting & Deployment

| Name | Link | What It Does | Free Tier | Best Use Case | Rating | Alternative |
|------|------|-------------|-----------|---------------|--------|-------------|
| Vercel | https://vercel.com | Deploy Next.js and frontend apps instantly | Generous free tier | Next.js, static sites, serverless APIs | 5/5 | Netlify |
| Railway | https://railway.app | Deploy any app with zero config | $5 free credit/month | Full-stack apps, databases, workers | 5/5 | Render |
| Render | https://render.com | Cloud hosting for web apps and databases | Free tier for static + web services | Simple deployments, databases | 4/5 | Railway |
| Fly.io | https://fly.io | Deploy apps close to users (edge) | 3 shared VMs free | Global edge apps, WebSockets | 4/5 | Railway |
| Cloudflare Pages | https://pages.cloudflare.com | Deploy static sites and full-stack apps | Free with unlimited bandwidth | Jamstack, edge computing | 5/5 | Vercel |
| Netlify | https://netlify.com | Deploy web apps with Git-based CI/CD | 100GB bandwidth free | Static sites, JAMstack | 4/5 | Vercel |

## Design Tools

| Name | Link | What It Does | Free Tier | Best Use Case | Rating | Alternative |
|------|------|-------------|-----------|---------------|--------|-------------|
| Figma | https://figma.com | Collaborative interface design tool | Free for 3 files | UI/UX design, wireframes, prototypes | 5/5 | Penpot |
| Excalidraw | https://excalidraw.com | Virtual whiteboard for sketching | Free (open source) | Architecture diagrams, quick sketches | 5/5 | Miro |
| FigJam | https://figma.com/figjam | Collaborative whiteboard by Figma | Free for 3 boards | Brainstorming, flowcharts | 4/5 | Miro |
| Canva | https://canva.com | Graphic design for non-designers | Free tier available | Social media posts, pitch decks, handouts | 4/5 | Figma |
| unDraw | https://undraw.co | Open source illustrations | Free | Placeholder graphics, landing pages | 4/5 | Storyset |

## Dev Tools & Utilities

| Name | Link | What It Does | Free Tier | Best Use Case | Rating | Alternative |
|------|------|-------------|-----------|---------------|--------|-------------|
| Postman | https://postman.com | API development and testing | Free tier | Testing API endpoints | 4/5 | Insomnia |
| Doppler | https://doppler.com | Manage environment variables securely | Free tier for individuals | Team secret management | 4/5 | .env files |
| Linear | https://linear.app | Project management for software teams | Free for up to 250 issues | Task tracking during hackathon | 5/5 | Notion |
| Notion | https://notion.so | All-in-one workspace for docs and tasks | Free tier | Planning, notes, wikis | 4/5 | Linear |
| GitHub Copilot | https://github.com/features/copilot | AI pair programmer | Free for students | Code completion, boilerplate generation | 5/5 | Cursor |
| Cursor | https://cursor.com | AI-powered code editor (VS Code fork) | Free tier available | AI-assisted coding, refactoring | 5/5 | GitHub Copilot |
| Warp | https://warp.dev | Modern terminal with AI features | Free tier | Command line, git, scripting | 4/5 | iTerm2 |

## Hackathon-Specific Platforms

| Name | Link | What It Does | Free Tier | Best Use Case | Rating | Alternative |
|------|------|-------------|-----------|---------------|--------|-------------|
| Devpost | https://devpost.com | Hackathon discovery and submission platform | Free | Finding hackathons, submitting projects | 5/5 | Hackathon.com |
| MLH | https://mlh.io | Major League Hacking — student hackathon organizer | Free | Finding and joining hackathons | 5/5 | Devpost |
| HackMIT | https://hackmit.org | MIT's annual hackathon (apply to attend) | Free | Prestigious hackathon experience | 5/5 | Hack the North |
| GitHub Education | https://education.github.com | Free tools and credits for students | Free for students | Student dev packs, free hosting | 5/5 | N/A |
| Stripe for Startups | https://stripe.com/startups | Payment processing with startup credits | Free processing up to threshold | Adding payments to your hackathon project | 4/5 | Square |

## Learning Resources

| Name | Link | What It Does | Free Tier | Best Use Case | Rating | Alternative |
|------|------|-------------|-----------|---------------|--------|-------------|
| freeCodeCamp | https://freecodecamp.org | Free coding bootcamp with certifications | Free | Learning web dev fundamentals | 5/5 | The Odin Project |
| The Odin Project | https://theodinproject.com | Full-stack curriculum (Ruby/JS) | Free | Structured full-stack learning | 5/5 | freeCodeCamp |
| Fireship | https://youtube.com/@Fireship | Fast-paced tech tutorials | Free | Quick framework overviews, comparisons | 5/5 | Traversy Media |
| Web Dev Simplified | https://youtube.com/@WebDevSimplified | Clear web development tutorials | Free | Deep dives into specific concepts | 4/5 | Fireship |
| CS50 | https://cs50.harvard.edu | Harvard's intro to computer science | Free | Fundamentals, algorithms, problem-solving | 5/5 | MIT OCW |
| Roadmap.sh | https://roadmap.sh | Visual learning paths for tech roles | Free | Deciding what to learn next | 5/5 | N/A |

## Communities

| Name | Link | What It Does | Free Tier | Best Use Case | Rating | Alternative |
|------|------|-------------|-----------|---------------|--------|-------------|
| Discord (hackathon servers) | Search "hackathon" on Disboard | Find teammates, get help, share projects | Free | Team recruitment, real-time help | 4/5 | Slack |
| r/hackathons | https://reddit.com/r/hackathons | Reddit community for hackathon discussion | Free | Advice, experience sharing | 4/5 | Discord |
| Indie Hackers | https://indiehackers.com | Community of founders building products | Free | Inspiration, feedback, co-founder search | 4/5 | Hacker News |
| Hacker News | https://news.ycombinator.com | Tech news and discussion | Free | Getting feedback on launched projects | 4/5 | Indie Hackers |
| Twitter/X Tech | https://twitter.com | Follow #buildinpublic for hackathon builders | Free | Sharing progress, finding teammates | 4/5 | LinkedIn |

---

## How to Use This List

1. **Before the hackathon:** Skim the categories. Bookmark 3-5 tools you want to try.
2. **During setup (Hour 1):** Pick one from each category. Don't overthink it.
3. **When stuck:** Check the "Alternative" column — there's always another option.
4. **After the hackathon:** Rate your tools. Update this list with what actually worked.

**The rule:** Pick fast, build fast, iterate fast. The tool doesn't win the hackathon — your idea and execution do.
