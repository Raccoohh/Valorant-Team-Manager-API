from pydantic import BaseModel, ConfigDict, Field
from typing import Optional

class PlayerBase(BaseModel):
    nickname: str = Field(..., json_schema_extra={"example": "m1zz1x"})
    riot_id: str = Field(..., json_schema_extra={"example": "M1zz1x#TAG"})
    game_role: str = Field(..., json_schema_extra={"example": "Duelist"})
    discord_tag: Optional[str] = Field(default=None, json_schema_extra={"example": None})

class PlayerCreate(PlayerBase):
    pass

class PlayerResponse(PlayerBase):
    id: int

    model_config = ConfigDict(from_attributes=True)