# FastAPI starter (Supabase-ready)

Minimal API for Python hackathon demos. In-memory store by default so the
golden path works with zero setup; point at Supabase/Neon Postgres next.

## Run

```bash
pip install -r requirements.txt
uvicorn main:app --reload
# health: GET http://127.0.0.1:8000/healthz
# fixture mode: GET /items?demo=1
```

## Env

```bash
FRONTEND_URL=http://localhost:3000  # set to your Vercel URL in production
```

## Deploy

- Railway or Render → Web Service, start command:
  `uvicorn main:app --host 0.0.0.0 --port $PORT`
- Set `FRONTEND_URL` to the deployed frontend domain (CORS).
- Add `/healthz` as the platform health check.
- See `10-deployment-mastery/` for the full backup-plan checklist.
