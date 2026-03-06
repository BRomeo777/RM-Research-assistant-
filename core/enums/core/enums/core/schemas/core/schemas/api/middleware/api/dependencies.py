from typing import AsyncGenerator
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import Request
from slowapi import Limiter
from slowapi.util import get_remote_address
from config.database import SessionLocal

# Re-export limiter so routes can use it easily
limiter = Limiter(key_func=get_remote_address)

async def get_db() -> AsyncGenerator[AsyncSession, None]:
    """
    Creates a fresh database session for each request and closes it when done.
    Essential for preventing memory leaks in Phase 1 and beyond.
    """
    async with SessionLocal() as session:
        try:
            yield session
        finally:
            await session.close()
