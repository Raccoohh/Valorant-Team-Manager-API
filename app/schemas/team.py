from pydantic import BaseModel, ConfigDict, Field

class TeamBase(BaseModel):
    name: str = Field(..., example="NAVI")
    captain_id: int = Field(..., example=1)

class TeamCreate(TeamBase):
    pass

class TeamResponse(TeamBase):
    id: int

    model_config = ConfigDict(from_attributes=True)