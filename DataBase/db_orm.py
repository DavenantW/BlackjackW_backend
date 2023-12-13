from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker, DeclarativeBase
import config

engine = create_engine(
    url=config.pg(),
    echo=False
)

session_factory = sessionmaker(engine)


class Base(DeclarativeBase):
    pass