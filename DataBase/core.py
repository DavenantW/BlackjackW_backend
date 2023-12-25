# function on the core
from bcrypt import checkpw, gensalt, hashpw
from DataBase.factory_engine import engine
from DataBase.models import *
from sqlalchemy.sql import *


def create_tables():
    Base.metadata.create_all(engine)


def drop_tables():
    Base.metadata.drop_all(engine)


def ps_check(password: str, email: str = None, id: int = None):
    password = password.encode()
    if id:
        password_db = select_user(id)['password_hash']
        return checkpw(password, password_db.encode())
    elif email:
        password_db = select_user(select_user_id(email))['password_hash']
        return checkpw(password, password_db.encode())
    else:
        raise TypeError("Were not found need data: email or id")


def select_user_id(email: str = None):
    """ Find all users

    if necessary, select a specific user and enter an email address
    """
    with engine.connect() as conn:
        stmt = select(Users.id) if email is None else select(Users).where(Users.email == email)
        response = conn.execute(stmt)
        row = response.fetchone()
        res = row[0]
        return res


def select_user(id_user: str = None):
    """Find all personal data

    if necessary, select a specific user and enter an id
    """
    with engine.connect() as conn:
        if id_user:

            stmt = select(Users).where(Users.id == id_user)
            response = conn.execute(stmt)
            row = response.fetchone()
            res = {response.keys()._keys[i]: row[i] for i in range(len(row))}
            return res
        stmt = select(Users)
        response = conn.execute(stmt)
        res = []
        for row in response.fetchall():
            res.append({response.keys()._keys[i]: row[i] for i in range(len(row))})
        return res


def new_user(email: str, password: str, name: str = 'anonim', **id: int):
    """Add new user in tables (Users, Statistics)"""
    with engine.connect() as conn:
        stmt = insert(Users).values(email=email, password_hash=str(hashpw(password.encode(), gensalt()))[2:-1], name=name, **id)
        res = conn.execute(stmt)
        # conn.commit()
        # create user in Users table
        stmt1 = insert(Statistics).values(id=res.inserted_primary_key[0])
        res1 = conn.execute(stmt1)
        conn.commit()


def update_data_user(id_user: int, **kwargs):
    ''' Update information about user personal data '''
    with engine.connect() as conn:
        if kwargs.get('password'):
            k = kwargs.pop('password')
            stmt = update(Users).where(Users.id == id_user).values(**kwargs, password_hash=str(hashpw(k.encode(), gensalt()))[2:-1])
        else:
            stmt = update(Users).where(Users.id == id_user).values(**kwargs)
        conn.execute(stmt)
        conn.commit()
        if kwargs.get('id'):
            # change id column in Statistics table
            stmt = update(Statistics).where(Statistics.id == id_user).values(id=kwargs.get('id'))
            conn.execute(stmt)
            conn.commit()


def select_statistics(id_user: int = None):
    """Find all users statistics

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