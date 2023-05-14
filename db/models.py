from datetime import datetime

from sqlalchemy import Column, BigInteger, insert, String, DateTime, update
from sqlalchemy import select
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


class User(Base):
    __tablename__ = "users"

    telegram_id = Column(BigInteger, primary_key=True)
    first_name = Column(String(length=100))
    last_name = Column(String(length=100), nullable=True)
    username = Column(String(length=100), nullable=True)
    lang_code = Column(String(length=4), default='ru_RU')
    role = Column(String(length=100), default='user')
    created_at = Column(DateTime(timezone=False))

    @classmethod
    async def get_user(cls, session_maker: sessionmaker, telegram_id: int) -> 'User':
        async with session_maker() as db_session:
            sql = select(cls).where(cls.telegram_id == telegram_id)
            request = await db_session.execute(sql)
            user: cls = request.scalar()
        return user

    @classmethod
    async def add_user(cls,
                       session_maker: sessionmaker,
                       telegram_id: int,
                       first_name: str,
                       created_at: datetime,
                       last_name: str = None,
                       username: str = None,
                       lang_code: str = None,
                       role: str = None,
                       ) -> 'User':
        async with session_maker() as db_session:
            sql = insert(cls).values(telegram_id=telegram_id,
                                     first_name=first_name,
                                     created_at=created_at,
                                     last_name=last_name,
                                     username=username,
                                     lang_code=lang_code,
                                     role=role).returning('*')
            result = await db_session.execute(sql)
            await db_session.commit()
            return result.first()

    async def update_user(self, session_maker: sessionmaker, updated_fields: dict) -> 'User':
        async with session_maker() as db_session:
            sql = update(User).where(User.telegram_id == self.telegram_id).values(**updated_fields)
            result = await db_session.execute(sql)
            await db_session.commit()
            return result


async def test_db(session_maker):
    # await Email.add_email(session_maker, user_id=364294246, email='asddfdsfds', password='sssssswwwwww')
    # print(await User.delete_user(session_maker, telegram_id=364294246))
    # print(await Email.delete_email(session_maker, user_id=364294246, email='asddfdsfds'))
    # print(await Email.get_emails(session_maker, user_id=364294246))
    pass
