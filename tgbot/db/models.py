from sqlalchemy import BigInteger, DateTime, String, Integer, Boolean
from sqlalchemy import Column
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class User(Base):
    __tablename__ = "users"
    user_id = Column(BigInteger, primary_key=True, unique=True, autoincrement=False)
    last_connect = Column(DateTime)

    interview = Column(Boolean, default=False)
    cashback_points = Column(Integer, nullable=True)
    clients_count = Column(Integer, nullable=True)
    go_points = Column(Integer, nullable=True)
    membership_status = Column(String, nullable=True)
    activity = Column(String, nullable=True)
    city = Column(String, nullable=True)
    strengths = Column(String, nullable=True)
    shortage = Column(String, nullable=True)


class Pair(Base):
    __tablename__ = "pairs"
    id = Column(BigInteger, primary_key=True, unique=True, autoincrement=True)
    user_id_1 = Column(BigInteger)
    user_id_2 = Column(BigInteger)
