from pydantic import BaseModel, ConfigDict, Field

class TeamBase(BaseModel):
    name: str = Field(..., json_schema_extra={"example": "no talent"})
    captain_id: int = Field(..., json_schema_extra={"example": 1})

class TeamCreate(TeamBase):
    pass

class TeamResponse(TeamBase):
    id: int

    model_config = ConfigDict(from_attributes=True)