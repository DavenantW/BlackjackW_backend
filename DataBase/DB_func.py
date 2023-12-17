# the file for database functions
from orm import session_factory, engine, Base
from models import *


def create_tables():
    Base.metadata.create_all(engine)


create_tables()