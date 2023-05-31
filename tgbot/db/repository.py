import datetime

from sqlalchemy import insert, select, update
from sqlalchemy import text

from tgbot.db.manager import DatabaseManager
from tgbot.db.models import User, Base, Pair


class Repository:
    def __init__(self, db_manager: DatabaseManager):
        self.db_manager = db_manager
        self.user_repository = UserRepository(db_manager=db_manager)
        self.pair_repository = PairRepository(db_manager=db_manager)

    async def create_all_models(self):
        async with self.db_manager.engine.begin() as conn:
            await conn.run_sync(Base.metadata.create_all)


class UserRepository:
    def __init__(self, db_manager: DatabaseManager):
        self.db_manager = db_manager

    async def create_user(self, user: User):
        async with self.db_manager.async_session() as session:
            query = (
                insert(User).values(user_id=user.user_id, last_connect=user.last_connect)
            )
            await session.execute(query)
            await session.commit()

    async def get_user_by_id(self, user_id: int) -> User | None:
        async with self.db_manager.async_session() as session:
            query = (
                select(User).where(User.user_id == user_id)
            )
            result = await session.execute(query)
            data = result.fetchone()
            if data:
                return data[0]

    async def update_last_connect(self, user_id: int):
        async with self.db_manager.async_session() as session:
            current_time = datetime.datetime.now()
            query = (update(User).where(User.user_id == user_id).values(last_connect=current_time))
            await session.execute(query)
            await session.commit()

    async def get_free_users(self, time_diff: datetime.timedelta):
        async with self.db_manager.async_session() as session:
            ten_sec_ago = datetime.datetime.now() - time_diff
            query = (
                select(User.user_id).where(User.last_connect < ten_sec_ago)
            )
            result = await session.execute(query)
            return result.fetchall()


class PairRepository:
    def __init__(self, db_manager: DatabaseManager):
        self.db_manager = db_manager

    async def create_pair(self, pair: Pair):
        async with self.db_manager.async_session() as session:
            query = (insert(Pair).values(user_id_1=pair.user_id_1, user_id_2=pair.user_id_2))
            await session.execute(query)
            await session.commit()

    async def get_free_friends_ids_for_user(self, user_id: int):
        async with self.db_manager.async_session() as session:
            query = f"SELECT user_id FROM users WHERE user_id != {user_id} " \
                    f"AND user_id NOT IN (SELECT user_id_2 FROM pairs WHERE user_id_1 = {user_id}) " \
                    f"AND user_id NOT IN (SELECT user_id_1 FROM pairs WHERE user_id_2 = {user_id})"""
            result = await session.execute(text(query))
            data = result.fetchall()
            return data
