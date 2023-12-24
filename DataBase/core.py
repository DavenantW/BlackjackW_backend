# function on the core
from bcrypt import checkpw, gensalt, hashpw
from DataBase.factory_engine import engine
from DataBase.models import *
from sqlalchemy.sql import *


def create_tables():
    Base.metadata.create_all(engine)


def drop_tables():
    Base.metadata.drop_all(engine)


def ps_hash(password: str):
    password = password.encode()
    return hashpw(password, gensalt())


def ps_check(password: str, email: str = None, id: int = None):
    password = password.encode()
    if not(id is None):
        password_db = select_user(id)[0]['password'].encode()
        print(password_db)
        return checkpw(password, password_db)
    elif not(email is None):
        password_db = select_user_email(email)[0]['password'].encode()
        return checkpw(password, password_db)
    else:
        raise Exception('что-то пошло не так')


def new_user(email: str, password: str, name: str = 'anonim', **id: int):
    """Add new user in tables (Users, Statistics)"""
    with engine.connect() as conn:
        stmt = insert(Users).values(email=email, password_hash=str(ps_hash(password))[2:-1], name=name, **id)
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
        if kwargs.get('password'):
            k = kwargs.pop('password')
            stmt = update(Users).where(Users.id == id_user).values(**kwargs, password_hash=str(ps_hash(k))[2:-1])
        else:
            stmt = update(Users).where(Users.id == id_user).values(**kwargs)
        conn.commit()
        if kwargs.get('id'):
            # change id column in Statistics table
            stmt = update(Statistics).where(Statistics.id == id_user).values(id=kwargs.get('id'))
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