from pydantic import BaseModel, ConfigDict, Field

class PaymentBase(BaseModel):
    team_id: int = Field(..., example=1)
    tournament_id: int = Field(..., example=1)
    amount_paid: float = Field(..., example=50.00)
    payment_status: str = Field(default="completed", example="completed")

class PaymentCreate(PaymentBase):
    pass

class PaymentResponse(PaymentBase):
    id: int

    model_config = ConfigDict(from_attributes=True)