import datetime

from sqlalchemy import Table, Column, Integer, String, MetaData
from sqlalchemy.orm import Mapped, mapped_column
from engine import Base


class Users(Base):
    __tablename__ = 'Users'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(32))
    email: Mapped[str] = mapped_column(String(256), unique=True)
    password: Mapped[str] = mapped_column(String(256))


class Statistics(Base):
    __tablename__ = 'Statistics'

    id: Mapped[int] = mapped_column(primary_key=True)
    games: Mapped[int] = mapped_column(default=0)
    wins: Mapped[int] = mapped_column(default=0)
    money: Mapped[int] = mapped_column(default=0)