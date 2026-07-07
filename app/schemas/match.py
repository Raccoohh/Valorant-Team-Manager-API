from pydantic import BaseModel, ConfigDict, Field
from typing import Optional

class MatchBase(BaseModel):
    team_id: int = Field(..., example=1)
    tournament_id: int = Field(..., example=1)
    opponent_name: str = Field(..., example="Sentinels")
    team_score: int = Field(default=0, example=13)
    opponent_score: int = Field(default=0, example=11)
    match_result: Optional[str] = Field(default=None, example="WIN") # WIN або LOSS

class MatchCreate(MatchBase):
    pass

class MatchResponse(MatchBase):
    id: int

    model_config = ConfigDict(from_attributes=True)