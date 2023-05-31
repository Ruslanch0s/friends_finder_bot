from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker


class DatabaseManager:
    def __init__(self, db_url: str, echo: bool):
        self.engine = create_async_engine(url=db_url)
        self.async_session = async_sessionmaker(bind=self.engine, expire_on_commit=False)
