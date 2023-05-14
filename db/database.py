from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker

from config import Config
from db import models


async def create_db_session(config: Config):
    engine = create_async_engine(
        f"postgresql+asyncpg://{config.db.user}:{config.db.password}@{config.db.host}:{config.db.port_target}/{config.db.database}",
        future=True
    )
    # Лучше создать миграции с помощью Alembic
    # async with engine.begin() as conn:
    #     await conn.run_sync(models.Base.metadata.drop_all)
    #     await conn.run_sync(models.Base.metadata.create_all)

    # expire_on_commit=False will prevent attributes from being expired
    # after commit.
    async_session = sessionmaker(
        engine, expire_on_commit=True, class_=AsyncSession
    )
    return async_session
