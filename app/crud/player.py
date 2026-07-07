from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.models.models import Player
from app.schemas.player import PlayerCreate

async def create_player(db: AsyncSession, player: PlayerCreate) -> Player:
    db_player = Player(**player.model_dump())
    db.add(db_player)
    await db.commit()
    await db.refresh(db_player)
    return db_player

async def get_player(db: AsyncSession, player_id: int) -> Player | None:
    result = await db.execute(select(Player).where(Player.id == player_id))
    return result.scalar_one_or_none()