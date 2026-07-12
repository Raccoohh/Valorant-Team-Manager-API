from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api import players, teams, tournaments, matches, payments

app = FastAPI(
    title="Valorant Team Management API",
    description="RESTful API for managing esports rosters, tracking performance, and AI coaching.",
    version="1.0.0"
)

# === НАЛАШТУВАННЯ CORS ===
# Це обов'язковий стандарт для публічних/комерційних API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # У продакшені тут вказуються конкретні домени (наприклад, https://mydomain.com)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# === ПІДКЛЮЧЕННЯ РОУТЕРІВ ===
app.include_router(players.router)
app.include_router(teams.router)
app.include_router(tournaments.router)
app.include_router(matches.router)
app.include_router(payments.router)

# === КОРЕНЕВИЙ ЕНДПОІНТ (Health Check) ===
@app.get("/", tags=["Health Check"])
async def root():
    return {
        "status": "ok",
        "message": "Welcome to the no talent | Esports Team Management API",
        "docs_url": "/docs"
    }