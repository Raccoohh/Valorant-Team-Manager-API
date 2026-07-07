from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.models.models import Tournament
from app.schemas.tournament import TournamentCreate

async def create_tournament(db: AsyncSession, tournament: TournamentCreate) -> Tournament:
    db_tournament = Tournament(**tournament.model_dump())
    db.add(db_tournament)
    await db.commit()
    await db.refresh(db_tournament)
    return db_tournament

async def get_tournaments(db: AsyncSession) -> list[Tournament]:
    result = await db.execute(select(Tournament))
    return list(result.scalars().all())