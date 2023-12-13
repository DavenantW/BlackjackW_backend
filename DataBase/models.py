from sqlalchemy import Table, Column, Integer, String, MetaData
from sqlalchemy.orm import Mapped, mapped_column
from DB_func import Base


class Chenge(Base):
    __tablename__ = 'chenge'

    id: Mapped[int] = mapped_column(primary_key=True)
    chenge: Mapped[str]