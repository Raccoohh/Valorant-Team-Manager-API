from sqlalchemy.ext.asyncio import AsyncSession
from app.models.models import Payment
from app.schemas.payment import PaymentCreate

async def create_payment(db: AsyncSession, payment: PaymentCreate) -> Payment:
    db_payment = Payment(**payment.model_dump())
    db.add(db_payment)
    await db.commit()
    await db.refresh(db_payment)
    return db_payment