from typing import AsyncGenerator

from sqlalchemy.ext.asyncio import (
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)
from sqlalchemy.orm import DeclarativeBase

from app.core.config import Settings

settings = Settings()


# Classe base para os modelos do SQLAlchemy
class Base(DeclarativeBase):
    pass


engine = create_async_engine(
    url=settings.DATABASE_URL,
    echo=settings.DEBUG,
)

AsyncSessionLocal = async_sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False,
)


async def get_session() -> AsyncGenerator[AsyncSession, None]:
    """Gerador de sessão assíncrona do SQLAlchemy."""
    async with AsyncSessionLocal() as session:
        yield session
