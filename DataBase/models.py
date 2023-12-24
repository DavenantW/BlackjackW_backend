import datetime

from sqlalchemy import Table, Column, Integer, String, MetaData, VARCHAR, VARBINARY
from sqlalchemy.orm import Mapped, mapped_column
from DataBase.factory_engine import Base
from bcrypt import hashpw, gensalt, checkpw


class Users(Base):
    __tablename__ = 'Users'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(32))
    email: Mapped[str] = mapped_column(String(256), unique=True)
    password_hash: Mapped[str] = mapped_column(String(128))

    @property
    def password(self):
        """ If somebody uses a password the value of password_hash is returned"""
        return self.password_hash

    @password.setter
    def password(self, password):
        """ When creating new user, this function creates a hash for the password"""
        self.password_hash = str(hashpw(password.encode(), gensalt()))[2:-1]

    def ps_check(self, password):
        """ This function checks, that password == is the password in the DataBase"""
        return checkpw(password.encode(), self.password_hash.encode())


class Statistics(Base):
    __tablename__ = 'Statistics'

    id: Mapped[int] = mapped_column(primary_key=True)
    games: Mapped[int] = mapped_column(default=0)
    wins: Mapped[int] = mapped_column(default=0)
    money: Mapped[int] = mapped_column(default=0)