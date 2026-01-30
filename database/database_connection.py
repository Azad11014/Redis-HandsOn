from typing import AsyncGenerator

from sqlalchemy.ext.asyncio import (
    create_async_engine,
    AsyncSession,
    async_sessionmaker,
)

from config.config import DATABASE_URL

# DATABASE_URL example:
# sqlite+aiosqlite:///./app.db

# -------------------------
# Async Engine (SQLite)
# -------------------------
engine = create_async_engine(
    DATABASE_URL,
    echo=False,  # set True for SQL debugging
)

# -------------------------
# Async Session Factory
# -------------------------
AsyncSessionLocal = async_sessionmaker(
    bind=engine,
    expire_on_commit=False,
)

# -------------------------
# Dependency
# -------------------------
async def get_db() -> AsyncGenerator[AsyncSession, None]:
    async with AsyncSessionLocal() as session:
        yield session
