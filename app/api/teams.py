from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.database import get_db
from app.schemas.team import TeamCreate, TeamResponse
from app.crud import team as crud_team

router = APIRouter(prefix="/teams", tags=["Teams"])

@router.post("/", response_model=TeamResponse)
async def create_new_team(team: TeamCreate, db: AsyncSession = Depends(get_db)):
    return await crud_team.create_team(db, team)

@router.get("/{team_id}", response_model=TeamResponse)
async def read_team(team_id: int, db: AsyncSession = Depends(get_db)):
    db_team = await crud_team.get_team(db, team_id)
    if db_team is None:
        raise HTTPException(status_code=404, detail="Team not found")
    return db_team

@router.post("/{team_id}/players/{player_id}")
async def add_player_to_roster(team_id: int, player_id: int, db: AsyncSession = Depends(get_db)):
    try:
        return await crud_team.add_player_to_team(db, team_id, player_id)
    except Exception as e:
        # Відловлюємо помилку, якщо гравця чи команди не існує, 
        # або якщо цей гравець ВЖЕ є у цій команді
        raise HTTPException(
            status_code=400, 
            detail="Не вдалося додати гравця. Перевірте, чи існують такі ID, або можливо гравець вже у складі."
        )