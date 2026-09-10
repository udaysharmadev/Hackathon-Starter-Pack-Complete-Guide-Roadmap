"""FastAPI hackathon starter. Run: uvicorn main:app --reload."""
import os

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI(title="Hackathon API", version="0.1.0")

FRONTEND_URL = os.environ.get("FRONTEND_URL", "http://localhost:3000")

app.add_middleware(
    CORSMiddleware,
    allow_origins=[FRONTEND_URL],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class Item(BaseModel):
    title: str
    detail: str = ""


# In-memory store so the demo works with zero DB setup.
# Swap for Supabase/Neon Postgres after the golden path works.
ITEMS: list[Item] = [
    Item(title="Seeded demo item", detail="Pre-loaded so judging never sees an empty state."),
]


@app.get("/healthz")
def healthz():
    return {"ok": True}


@app.get("/items")
def list_items(demo: int = 0):
    if demo == 1:
        return {"items": [i.model_dump() for i in ITEMS], "source": "fixture"}
    return {"items": [i.model_dump() for i in ITEMS], "source": "live"}


@app.post("/items", status_code=201)
def create_item(item: Item):
    ITEMS.append(item)
    return item
