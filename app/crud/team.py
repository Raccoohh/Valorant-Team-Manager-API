from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.models.models import Team, TeamRoster
from app.schemas.team import TeamCreate

async def create_team(db: AsyncSession, team: TeamCreate) -> Team:
    db_team = Team(**team.model_dump())
    db.add(db_team)
    await db.commit()
    await db.refresh(db_team)
    return db_team

async def get_team(db: AsyncSession, team_id: int) -> Team | None:
    result = await db.execute(select(Team).where(Team.id == team_id))
    return result.scalar_one_or_none()

async def add_player_to_team(db: AsyncSession, team_id: int, player_id: int):
    # Створюємо запис у проміжній таблиці
    roster_link = TeamRoster(team_id=team_id, player_id=player_id)
    db.add(roster_link)
    await db.commit()
    return {"message": f"Гравець з ID {player_id} успішно доданий до команди {team_id}"}