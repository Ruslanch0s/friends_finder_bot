from sqlalchemy import BigInteger, DateTime, String
from sqlalchemy import Column
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class User(Base):
    __tablename__ = "users"
    user_id = Column(BigInteger, primary_key=True, unique=True, autoincrement=False)
    full_name = Column(String)
    last_connect = Column(DateTime)


class Pair(Base):
    __tablename__ = "pairs"
    id = Column(BigInteger, primary_key=True, unique=True, autoincrement=True)
    user_id_1 = Column(BigInteger)
    user_id_2 = Column(BigInteger)
