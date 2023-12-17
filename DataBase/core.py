# function on the core
from engine import engine
from sqlalchemy import Table, Column, Integer, String, MetaData
from models import *
from sqlalchemy.sql import *


def select_all():
    """Find all users"""
    with engine.connect() as conn:
        stmt = select(Users)
        res = conn.execute(stmt)
        res = res.all()
        print(res)


def new_user(email: str, password: str, name: str = 'anonim', **id: int):
    """Add new user in tables (Users, Statistics)"""
    with engine.connect() as conn:
        stmt = insert(Users).values(email=email, password=password, **id)
        res = conn.execute(stmt)
        # create user in Users table
        stmt2 = insert(Statistics).values(id=res.inserted_primary_key[0], name=name)
        conn.execute(stmt2)
        # create user in Statistics table
        conn.commit()