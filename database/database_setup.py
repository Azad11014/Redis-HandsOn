"""
Database setup and initialization script
Run this file once to create all tables in your Neon database
"""

import asyncio
import logging

from sqlalchemy.ext.asyncio import create_async_engine
from app.models.models import Base
from config.config import DATABASE_URL

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


async def create_tables():
    """Create all tables in the database (async-safe)"""
    try:
        engine = create_async_engine(
            DATABASE_URL,
            echo=True,
        )

        logger.info("Creating database tables...")

        async with engine.begin() as conn:
            await conn.run_sync(Base.metadata.create_all)

        logger.info("All tables created successfully!")

        await engine.dispose()

    except Exception as e:
        logger.error(f"Error creating tables: {e}")
        raise


if __name__ == "__main__":
    asyncio.run(create_tables())
