from fastapi import FastAPI
from app.core.database import engine, Base
from contextlib import asynccontextmanager
from app.api import players, teams, tournaments, matches, payments

# Ця функція автоматично створює таблиці в БД при запуску
@asynccontextmanager
async def lifespan(app: FastAPI):
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield

app = FastAPI(
    title="Valorant Team Management API",
    lifespan=lifespan
)

app.include_router(players.router)
app.include_router(teams.router)
app.include_router(tournaments.router)
app.include_router(matches.router)
app.include_router(payments.router)

@app.get("/")
async def root():
    return {"message": "Welcome to the Esports Team Management API"}