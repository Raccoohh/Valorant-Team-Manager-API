import pytest
import pytest_asyncio
from app.core.database import engine, Base

# autouse=True означає, що функція спрацює автоматично для всіх тестів
@pytest_asyncio.fixture(scope="session", autouse=True)
async def setup_test_database():
    # 1. Створюємо всі таблиці перед тестами
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    
    yield # Тут pytest виконує самі тести
    
    # 2. Видаляємо таблиці після тестів (щоб очистити пам'ять)
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)