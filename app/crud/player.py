from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.models.models import Player
from app.schemas.player import PlayerCreate

# Додаємо аргумент puuid: str
async def create_player(db: AsyncSession, player: PlayerCreate, puuid: str) -> Player:
    # **player.model_dump() розпакує nickname, riot_id, game_role та discord_tag
    # А puuid ми додаємо вручну поруч
    db_player = Player(**player.model_dump(), puuid=puuid)
    db.add(db_player)
    await db.commit()
    await db.refresh(db_player)
    return db_player

async def get_player(db: AsyncSession, player_id: int) -> Player | None:
    result = await db.execute(select(Player).where(Player.id == player_id))
    return result.scalar_one_or_none()