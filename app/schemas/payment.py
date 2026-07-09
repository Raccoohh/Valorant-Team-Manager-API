from pydantic import BaseModel, ConfigDict, Field

class PaymentBase(BaseModel):
    team_id: int = Field(..., json_schema_extra={"example": 1})
    tournament_id: int = Field(..., json_schema_extra={"example": 1})
    amount_paid: float = Field(..., json_schema_extra={"example": 50.00})
    payment_status: str = Field(default="completed", json_schema_extra={"example": "completed"})

class PaymentCreate(PaymentBase):
    pass

class PaymentResponse(PaymentBase):
    id: int

    model_config = ConfigDict(from_attributes=True)