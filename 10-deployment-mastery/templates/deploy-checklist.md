# Deploy Checklist — Ship It Live Without Drama

Your app works locally. Now make it work everywhere. This checklist covers every major platform.

## Universal Pre-Deploy (Do This for ALL Platforms)

- [ ] All API keys are in `.env.local`, NOT hardcoded
- [ ] `.env.example` exists with all required variables (no values, just keys)
- [ ] `.gitignore` includes `.env*` files
- [ ] `package.json` has correct `build` and `start` scripts
- [ ] No `console.log` statements with sensitive data
- [ ] Build succeeds locally: `npm run build` completes without errors
- [ ] `README.md` has setup instructions for the deployer
- [ ] Domain/origin URL decided (you'll need this for callbacks)

## Platform-Specific Checklists

### Vercel (Recommended for Next.js / Frontend)

**Best for:** Next.js, React, Vue, static sites, serverless functions

**Deploy command:**
```bash
npx vercel --prod
```
Or connect your GitHub repo at vercel.com/new.

**Environment variables to set (in Vercel Dashboard → Settings → Environment Variables):**

```
# Required (add all that apply)
NEXT_PUBLIC_SUPABASE_URL=https://your-project.supabase.co
NEXT_PUBLIC_SUPABASE_ANON_KEY=eyJ...
SUPABASE_SERVICE_ROLE_KEY=eyJ...
OPENAI_API_KEY=sk-...
STRIPE_SECRET_KEY=sk_live_...
STRIPE_WEBHOOK_SECRET=whsec_...
NEXT_PUBLIC_APP_URL=https://your-app.vercel.app
RESEND_API_KEY=re_...

# Set these for ALL environments (Production, Preview, Development)
# unless you have different dev/staging values
```

**Checklist:**
- [ ] Framework preset detected correctly (Next.js, etc.)
- [ ] Build command is `npm run build` (or correct for your stack)
- [ ] Output directory is `.next` (Next.js default)
- [ ] Node.js version is 18+ in Settings → General
- [ ] Custom domain added and DNS configured
- [ ] `NEXT_PUBLIC_APP_URL` matches your actual domain
- [ ] Auth callback URLs updated to production domain

**Common Vercel errors:**
- `FUNCTION_INVOCATION_TIMEOUT` → Your serverless function takes > 10s. Optimize or move to a worker.
- `NO_BACKEND_FOUND` → Build output dir is wrong. Check `outputDirectory` setting.
- `ENV_VAR_NOT_FOUND` → Variable exists but isn't set for the correct environment.

### Railway (Best for Full-Stack / Backends)

**Best for:** Node.js backends, Python, databases, Docker, anything that needs a long-running process

**Deploy command:**
```bash
npm i -g @railway/cli
railway login
railway init
railway up
```

**Environment variables:**
```
# Railway auto-sets PORT — don't override it
PORT=3000
NODE_ENV=production
DATABASE_URL=postgresql://...
REDIS_URL=redis://...
API_KEY=your-key-here
JWT_SECRET=generate-a-secure-random-string
```

**Checklist:**
- [ ] `railway.json` or `Procfile` exists with start command
- [ ] Health check endpoint exists (usually `/health` or `/`)
- [ ] PORT uses `$PORT` variable, not hardcoded
- [ ] Database plugin connected (if using Railway Postgres)
- [ ] Custom domain configured (if needed)
- [ ] Volume mounted for persistent storage (if needed)

**Common Railway errors:**
- `Application failed to respond` → Health check failing. Make sure your app binds to `0.0.0.0:$PORT`.
- `Build failed` → Check build logs. Usually a missing dependency.
- `Crash loop` → App starts then immediately exits. Check logs for the real error.

### Firebase Hosting (Best for Static + Functions)

**Best for:** Static sites, JAMstack, apps with Cloud Functions

**Deploy command:**
```bash
npm install -g firebase-tools
firebase login
firebase init hosting
firebase deploy
```

**Firebase config (`firebase.json`):**
```json
{
  "hosting": {
    "public": "out",
    "ignore": ["firebase.json", "**/.*"],
    "rewrites": [
      { "source": "/api/**", "function": "api" },
      { "source": "**", "destination": "/index.html" }
    ]
  }
}
```

**Environment variables (set in Firebase Console → Functions → Settings):**
```
# For Cloud Functions, use secrets:
firebase functions:secrets:set OPENAI_API_KEY
firebase functions:secrets:set STRIPE_SECRET_KEY
```

**Checklist:**
- [ ] `firebase.json` configured with correct public directory
- [ ] SPA rewrites configured (all routes → index.html)
- [ ] API rewrites point to correct Cloud Functions
- [ ] Functions region is close to your users (us-central1 default)
- [ ] Custom domain added in Firebase Console
- [ ] SSL enabled (auto with Firebase)

**Common Firebase errors:**
- `404 on refresh` → Missing SPA rewrite. Add `"rewrites": [{"source": "**", "destination": "/index.html"}]`.
- `Function not found` → Function name doesn't match rewrite rule. Check function export name.
- `Billing account required` → You've exceeded the free tier. Upgrade or reduce usage.

### Render (Best for Docker / Monorepos)

**Best for:** Docker containers, monorepos, full-stack apps that need more than serverless

**Deploy command:** Connect GitHub repo at render.com/dashboard → New → Web Service

**Environment variables:**
```
NODE_ENV=production
PORT=10000
DATABASE_URL=postgresql://...
REDIS_URL=redis://...
SESSION_SECRET=random-32-char-string
```

**Checklist:**
- [ ] Build command is correct (`npm install && npm run build`)
- [ ] Start command is correct (`npm start` or `node server.js`)
- [ ] Health check path is set (default: `/`)
- [ ] Auto-deploy is enabled (or manual deploy configured)
- [ ] Free tier spin-down handled (Render free instances sleep after 15 min)
- [ ] Custom domain configured

**Common Render errors:**
- `Build failed: module not found` → Missing dependency in `package.json`. Check build logs.
- `Application failed to start` → Start command wrong or PORT not configured.
- `Health check failed` → App takes too long to start. Increase startup timeout or optimize.

## Common Errors and Fixes (All Platforms)

| Error | Platform | Fix |
|---|---|---|
| `Module not found` | All | Add missing package to `package.json`, rebuild |
| `CORS error` | All | Add production domain to CORS allowed origins |
| `API key undefined` | All | Env var not set for the deploy environment. Check dashboard. |
| `CANNOT GET /path` | Vercel/Render | SPA routing not configured. Add rewrites/redirects. |
| `Function timeout` | Vercel/Firebase | Optimize function or upgrade plan |
| `ECONNREFUSED` | All | Database/network service unreachable. Check connection string. |
| `SSL certificate error` | Railway/Render | Wait 24h for cert provision or use custom domain |
| `Rate limited` | All | You've exceeded API free tier. Add caching or upgrade. |
| `Build exceeds limit` | Vercel | Reduce bundle size. Check `next.config.js` output tracing. |
| `Permission denied` | All | File permissions wrong. Check Dockerfile or build config. |

## DNS/Domain Checklist

When you're ready to use a custom domain:

- [ ] Domain purchased (Namecheap, Cloudflare Registrar, Google Domains)
- [ ] DNS records added:
  - `A` record → platform IP (or CNAME to platform domain)
  - `CNAME` for `www` → your-app.vercel.app (or equivalent)
- [ ] Wait for propagation (5 min to 48 hours, usually ~30 min)
- [ ] SSL certificate auto-provisioned (all major platforms do this)
- [ ] Old URLs redirect to new domain (if migrating)
- [ ] Auth callback URLs updated in all OAuth providers
- [ ] `NEXT_PUBLIC_APP_URL` or equivalent env var updated

**DNS propagation check:**
```bash
dig yourdomain.com +short
# Should return your platform's IP or CNAME target
```

## Rollback Plan

Things will break. Here's what to do:

### Instant Rollback (Vercel / Render)
1. Go to dashboard → Deployments
2. Find the last working deployment
3. Click "Promote to Production"
4. Done. 30 seconds.

### Git Revert
```bash
git revert HEAD
git push origin main
# Auto-deploys the previous state
```

### Emergency: Database Rollback
```bash
# If you have Supabase
# Go to Dashboard → Database → Backups → Restore

# If you have a SQL backup
psql $DATABASE_URL < backup.sql
```

### Nuclear Option: Kill and Redeploy
```bash
# Vercel
vercel rm your-project --hard

# Railway
railway down
railway up
```

## Post-Deploy Verification (Run After Every Deploy)

- [ ] Open live URL in incognito browser
- [ ] Sign up / log in works
- [ ] Core feature works end-to-end
- [ ] No console errors in browser
- [ ] Mobile layout looks correct
- [ ] API calls return expected data (check Network tab)
- [ ] Email/notifications fire correctly
- [ ] Auth callback URL works (no redirect loop)
- [ ] Page loads in < 3 seconds
- [ ] Share the URL with someone. Can they use it?
