from pydantic import BaseModel, ConfigDict, Field
from typing import Optional

class PlayerBase(BaseModel):
    nickname: str = Field(..., example="m1zz1x")
    riot_id: str = Field(..., example="9Raccoon9#TAG")
    game_role: str = Field(..., example="Duelist")
    discord_tag: Optional[str] = None

class PlayerCreate(PlayerBase):
    pass

class PlayerResponse(PlayerBase):
    id: int

    model_config = ConfigDict(from_attributes=True)