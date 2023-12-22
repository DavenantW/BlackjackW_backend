# function on the core
from engine import engine
from sqlalchemy import Table, Column, Integer, String, MetaData
from models import *
from sqlalchemy.sql import *

from DB_func import *


def new_user(email: str, password: str, name: str = 'anonim', **id: int):
    """Add new user in tables (Users, Statistics)"""
    with engine.connect() as conn:
        stmt = insert(Users).values(email=email, password=ps_hash(password), name=name, **id)
        res = conn.execute(stmt)
        # create user in Users table
        stmt2 = insert(Statistics).values(id=res.inserted_primary_key[0])
        conn.execute(stmt2)
        # create user in Statistics table
        conn.commit()


def select_user_email(email: str = None):
    """
    Find all users
    if necessary, select a specific user and enter an email address
    """
    with engine.connect() as conn:
        stmt = select(Users) if email is None else select(Users).where(Users.email == email)
        response = conn.execute(stmt)
        row = response.fetchone()
        res = {response.keys()._keys[i]: row[i] for i in range(len(row))}
        return res


def select_user(id_user: str = None):
    """
    Find all personal data
    if necessary, select a specific user and enter an id
    """
    with engine.connect() as conn:
        stmt = select(Users) if id_user is None else select(Users).where(Users.id == id_user)
        response = conn.execute(stmt)
        res = []
        for row in response.fetchall():
             res.append({response.keys()._keys[i]: row[i] for i in range(len(row))})
        return res


def update_data_user(id_user: int, **kwargs):
    ''' Update information about user personal data '''
    with engine.connect() as conn:
        stmt = update(Users).where(Users.id == id_user).values(**kwargs)
        conn.execute(stmt)
        conn.commit()
        if kwargs.get('id'):
            # change id column in Statistics table
            stmt = update(Statistics).where(Statistics.id == id_user).values(id=kwargs.get('id'))
            conn.execute(stmt)
            conn.commit()
        if kwargs.get('password'):
            # change password column in Statistics table
            id_user = kwargs.get('id') if kwargs.get('id') else id_user
            # but need change id_user, because id change earlier commit
            stmt = update(Users).where(Users.id == kwargs.get('id')).values(password=ps_hash(kwargs.get('password')))
            conn.execute(stmt)
            conn.commit()


def select_statistics(id_user: int = None):
    """
    find all users statistics
    if necessary, select a specific user and enter an id
    """
    with engine.connect() as conn:
        stmt = select(Statistics) if id_user is None else select(Statistics).where(Statistics.id == id_user)
        response = conn.execute(stmt)
        res = []
        for row in response.fetchall():
            res.append({response.keys()._keys[i]: row[i] for i in range(len(row))})
        return res


def update_statistics(id_user: int, wins: int = 0, games: int = 0, money: int = 0):
    ''' Update information about user statistics '''
    with engine.connect() as conn:
        stmt = update(Statistics).where(Statistics.id == id_user).values(wins=wins + Statistics.wins,
                                                                    games=games + Statistics.games,
                                                                    money=money + Statistics.money)
        conn.execute(stmt)
        conn.commit()


update_data_user(8, id=9, password='qfwqfqf', email='qwe')
print(select_user_email('qwe'))
print(select_statistics(9))