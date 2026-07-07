from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.database import get_db
from app.schemas.tournament import TournamentCreate, TournamentResponse
from app.crud import tournament as crud_tournament

router = APIRouter(prefix="/tournaments", tags=["Tournaments"])

@router.post("/", response_model=TournamentResponse)
async def create_new_tournament(tournament: TournamentCreate, db: AsyncSession = Depends(get_db)):
    return await crud_tournament.create_tournament(db, tournament)

@router.get("/", response_model=list[TournamentResponse])
async def read_all_tournaments(db: AsyncSession = Depends(get_db)):
    return await crud_tournament.get_tournaments(db)