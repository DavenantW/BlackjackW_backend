from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker, DeclarativeBase
import DataBase.config

engine = create_engine(
    url=DataBase.config.pg(),
    echo=False
)

session_factory = sessionmaker(engine)


class Base(DeclarativeBase):
    pass
