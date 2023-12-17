# function on the orm
from engine import session_factory, engine, Base
import models


def create_tables():
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)


create_tables()