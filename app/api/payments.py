from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.database import get_db
from app.schemas.payment import PaymentCreate, PaymentResponse
from app.crud import payment as crud_payment

router = APIRouter(prefix="/payments", tags=["Finance"])

@router.post("/", response_model=PaymentResponse)
async def process_payment(payment: PaymentCreate, db: AsyncSession = Depends(get_db)):
    return await crud_payment.create_payment(db, payment)