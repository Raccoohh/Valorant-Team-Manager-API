from pydantic import BaseModel, ConfigDict, Field

class TournamentBase(BaseModel):
    name: str = Field(..., json_schema_extra={"example": "VCL East Qualifier"})
    entry_fee: float = Field(..., json_schema_extra={"example": 50.00})
    status: str = Field(default="upcoming", json_schema_extra={"example": "upcoming"})

class TournamentCreate(TournamentBase):
    pass

class TournamentResponse(TournamentBase):
    id: int

    model_config = ConfigDict(from_attributes=True)