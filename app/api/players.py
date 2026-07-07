from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.database import get_db
from app.schemas.player import PlayerCreate, PlayerResponse
from app.crud import player as crud_player

router = APIRouter(prefix="/players", tags=["Players"])

@router.post("/", response_model=PlayerResponse)
async def create_new_player(player: PlayerCreate, db: AsyncSession = Depends(get_db)):
    return await crud_player.create_player(db, player)

@router.get("/{player_id}", response_model=PlayerResponse)
async def read_player(player_id: int, db: AsyncSession = Depends(get_db)):
    db_player = await crud_player.get_player(db, player_id)
    if db_player is None:
        raise HTTPException(status_code=404, detail="Player not found")
    return db_player