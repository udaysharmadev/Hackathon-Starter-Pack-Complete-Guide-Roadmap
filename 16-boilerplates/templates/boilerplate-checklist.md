# Boilerplate Checklist

Use this when setting up your project in the first 2 hours. Pick your stack from below, then check off every item before writing a single feature.

---

## Universal Setup Checklist

These apply to every stack regardless of framework.

- [ ] Git repo initialized with `.gitignore` (Node, Python, or platform-appropriate)
- [ ] `README.md` created with project title and one-line description
- [ ] `.env.example` file created with all required variables (no real keys)
- [ ] `.env` added to `.gitignore`
- [ ] Folder structure created (see stack-specific sections below)
- [ ] Linter/formatter configured (ESLint, Prettier, Ruff, etc.)
- [ ] Pre-commit hook installed (optional but saves headaches)
- [ ] License file added (MIT is the hackathon default)
- [ ] Team members added as collaborators on the repo
- [ ] Branch protection: no direct pushes to `main`

---

## Next.js / React Stack

### Minimum Viable Boilerplate

```bash
npx create-next-app@latest my-app --typescript --tailwind --app
```

### Folder Structure

```
my-app/
├── src/
│   ├── app/            # Pages and routes
│   │   ├── layout.tsx  # Root layout
│   │   ├── page.tsx    # Home page
│   │   └── api/        # API routes
│   ├── components/     # Reusable UI components
│   │   ├── ui/         # Button, Input, Card, etc.
│   │   └── features/   # Feature-specific components
│   ├── lib/            # Utilities, helpers, config
│   │   ├── utils.ts
│   │   └── api.ts
│   ├── hooks/          # Custom React hooks
│   ├── types/          # TypeScript type definitions
│   └── styles/         # Global styles (if not using Tailwind)
├── public/             # Static assets (images, icons)
├── prisma/             # Database schema (if using Prisma)
├── .env.example
├── .gitignore
├── next.config.js
├── tailwind.config.ts
├── tsconfig.json
└── package.json
```

### Checklist

- [ ] `create-next-app` with TypeScript and Tailwind
- [ ] `components/ui/` folder with at least: Button, Input, Card, Modal
- [ ] `lib/api.ts` with fetch wrapper and base URL config
- [ ] `lib/utils.ts` with common helpers (formatDate, classNames, etc.)
- [ ] `types/` folder with initial type definitions
- [ ] API route template in `app/api/`
- [ ] Tailwind config customized with your color palette
- [ ] `next.config.js` with image domains configured
- [ ] Vercel deployment configured (or Dockerfile if self-hosting)

---

## Flask / Python Stack

### Minimum Viable Boilerplate

```bash
mkdir my-app && cd my-app
python -m venv venv
source venv/bin/activate
pip install flask python-dotenv
```

### Folder Structure

```
my-app/
├── app/
│   ├── __init__.py      # App factory
│   ├── routes/          # Route handlers
│   │   ├── __init__.py
│   │   └── main.py
│   ├── models/          # Data models
│   │   └── __init__.py
│   ├── services/        # Business logic
│   │   └── __init__.py
│   ├── utils/           # Helpers
│   │   └── __init__.py
│   └── templates/       # Jinja2 templates (if server-rendered)
├── static/              # CSS, JS, images
├── tests/               # Test files
├── .env.example
├── .gitignore
├── requirements.txt
├── run.py               # Entry point
└── README.md
```

### Checklist

- [ ] Virtual environment created and activated
- [ ] `requirements.txt` with all dependencies
- [ ] App factory pattern in `__init__.py`
- [ ] Blueprint structure for routes
- [ ] `run.py` with `if __name__ == "__main__"` guard
- [ ] CORS configured (if API serves a separate frontend)
- [ ] Error handlers for 404, 500
- [ ] `static/` folder with favicon and placeholder CSS
- [ ] `.env.example` with all required environment variables
- [ ] Gunicorn in `requirements.txt` for production deployment

---

## FastAPI / Python Stack

### Minimum Viable Boilerplate

```bash
mkdir my-app && cd my-app
python -m venv venv
source venv/bin/activate
pip install fastapi uvicorn python-dotenv pydantic
```

### Folder Structure

```
my-app/
├── app/
│   ├── __init__.py
│   ├── main.py          # FastAPI app instance
│   ├── routes/          # Route handlers
│   │   └── v1/          # Versioned routes
│   │       └── endpoints.py
│   ├── models/          # Pydantic models
│   │   └── schemas.py
│   ├── services/        # Business logic
│   ├── core/            # Config, security, dependencies
│   │   ├── config.py
│   │   └── deps.py
│   └── utils/
├── tests/
├── alembic/             # Database migrations (if using SQL)
├── .env.example
├── .gitignore
├── requirements.txt
├── Dockerfile
└── README.md
```

### Checklist

- [ ] FastAPI app created in `main.py`
- [ ] Pydantic models for request/response in `models/schemas.py`
- [ ] CORS middleware configured
- [ ] Health check endpoint at `/health`
- [ ] API versioning structure (v1, v2, etc.)
- [ ] Error handling middleware
- [ ] `Dockerfile` with multi-stage build
- [ ] `requirements.txt` pinned versions
- [ ] OpenAPI docs accessible at `/docs`
- [ ] Uvicorn configured for production (workers, host, port)

---

## Flutter / Dart Stack

### Minimum Viable Boilerplate

```bash
flutter create my_app
cd my_app
```

### Folder Structure

```
my_app/
├── lib/
│   ├── main.dart
│   ├── app.dart            # App widget and routing
│   ├── screens/            # Page-level widgets
│   │   └── home_screen.dart
│   ├── widgets/            # Reusable widgets
│   │   └── custom_button.dart
│   ├── models/             # Data models
│   ├── services/           # API calls, storage
│   ├── providers/          # State management
│   ├── utils/              # Helpers, constants
│   └── theme/              # Colors, typography
├── assets/                 # Images, fonts, JSON
├── android/
├── ios/
├── test/
├── pubspec.yaml
└── README.md
```

### Checklist

- [ ] Project created with `flutter create`
- [ ] `pubspec.yaml` with all dependencies (http, provider/bloc, etc.)
- [ ] State management setup (Provider, Riverpod, or Bloc)
- [ ] `screens/` folder with at least a home screen
- [ ] `widgets/` folder with reusable components
- [ ] `models/` folder with data classes
- [ ] `services/` folder with API client
- [ ] Theme defined in `theme/` (colors, text styles)
- [ ] Assets folder configured in `pubspec.yaml`
- [ ] Android and iOS builds tested

---

## React Native / Expo Stack

### Minimum Viable Boilerplate

```bash
npx create-expo-app my-app --template blank-typescript
```

### Checklist

- [ ] Expo project with TypeScript
- [ ] Navigation setup (React Navigation)
- [ ] `src/screens/` with at least home and detail screens
- [ ] `src/components/` with reusable UI elements
- [ ] `src/services/` with API client
- [ ] `src/context/` or state management (Zustand, Redux)
- [ ] `app.json` configured (name, icon, splash screen)
- [ ] Tested on both iOS simulator and Android emulator

---

## Environment Variable Checklist

Every project needs these documented. Add to your `.env.example`:

### Universal Variables
```
# App
APP_ENV=development
APP_PORT=3000
APP_URL=http://localhost:3000

# Database
DATABASE_URL=your_database_url_here

# Auth
JWT_SECRET=your_jwt_secret_here
NEXTAUTH_SECRET=your_nextauth_secret_here

# External APIs
OPENAI_API_KEY=your_openai_key_here
```

### Platform-Specific Additions

| Platform | Additional Variables |
|----------|---------------------|
| **Vercel** | `VERCEL_URL`, `VERCEL_ENV` |
| **AWS** | `AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY`, `AWS_REGION` |
| **Firebase** | `FIREBASE_API_KEY`, `FIREBASE_AUTH_DOMAIN`, `FIREBASE_PROJECT_ID` |
| **Stripe** | `STRIPE_SECRET_KEY`, `STRIPE_PUBLISHABLE_KEY`, `STRIPE_WEBHOOK_SECRET` |
| **Supabase** | `SUPABASE_URL`, `SUPABASE_ANON_KEY`, `SUPABASE_SERVICE_ROLE_KEY` |

---

## Deployment Readiness Check

Run this before submitting. Every box must be checked.

- [ ] All environment variables are set in production
- [ ] No secrets in client-side code (check with `grep -r "sk_" src/` and similar)
- [ ] Database is accessible from production server
- [ ] CORS is configured for production domain only
- [ ] HTTPS is enabled
- [ ] Error pages return proper status codes (not blank 500s)
- [ ] Static assets are served from CDN or optimized
- [ ] API rate limiting is in place (even basic)
- [ ] App loads in under 3 seconds on 3G
- [ ] No console.log statements with sensitive data
- [ ] Health check endpoint returns 200 OK
- [ ] Database migrations are applied
- [ ] Favicon and title are set (not default)
- [ ] README has live demo link
