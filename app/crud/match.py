from sqlalchemy.ext.asyncio import AsyncSession
from app.models.models import Match
from app.schemas.match import MatchCreate

async def create_match(db: AsyncSession, match: MatchCreate) -> Match:
    # Автоматично визначаємо результат, якщо його не вказали прямо
    result = match.match_result
    if not result and (match.team_score > 0 or match.opponent_score > 0):
        result = "WIN" if match.team_score > match.opponent_score else "LOSS"

    db_match = Match(
        team_id=match.team_id,
        tournament_id=match.tournament_id,
        opponent_name=match.opponent_name,
        team_score=match.team_score,
        opponent_score=match.opponent_score,
        match_result=result
    )
    db.add(db_match)
    await db.commit()
    await db.refresh(db_match)
    return db_match