from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.database import get_db
from app.schemas.match import MatchCreate, MatchResponse
from app.crud import match as crud_match

router = APIRouter(prefix="/matches", tags=["Matches"])

@router.post("/", response_model=MatchResponse)
async def record_match_result(match: MatchCreate, db: AsyncSession = Depends(get_db)):
    return await crud_match.create_match(db, match)