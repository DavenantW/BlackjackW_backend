from orm import engine
from sqlalchemy import Table, Column, Integer, String, MetaData
from models import *
from sqlalchemy.sql import *


def select_all():
    with engine.connect() as conn:
        stmt = select(Users)
        res = conn.execute(stmt)
        res = res.all()
        print(res)


def iserts(name, email, password, **kwargs):
    with engine.connect() as conn:
        stmt = insert(Users).values(name=name, email=email, password=password)
        conn.execute(stmt)
        conn.commit()


iserts(name='qwe', email='qwer', password='1234')