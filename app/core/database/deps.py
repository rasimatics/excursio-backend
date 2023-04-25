from sqlalchemy.ext.asyncio import AsyncSession
from .db import SessionLocal


async def get_db():
    session: AsyncSession = SessionLocal()
    try:
        yield session
    except:
        await session.rollback()
    finally:
        await session.close()
