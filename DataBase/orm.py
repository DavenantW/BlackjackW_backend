# function on the orm
from DataBase.factory_engine import session_factory, engine, Base
from DataBase.models import Users, Statistics
from sqlalchemy.sql import *


def create_tables():
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)

def drop_tables():
    Base.metadata.drop_all(engine)


def select_user(id_user: int = None):
    """ Find all user data in tables(Users, Statistics)
    if necessary, select a specific user and enter an id
    """
    with session_factory() as session:
        if not(id_user is None):
            query_user = select(Users).filter_by(id=id_user)
            query_stat = select(Statistics).filter_by(id=id_user)
            response_user = session.execute(query_user)
            response_stat = session.execute(query_stat)
            res = (response_user.fetchone()[0], response_stat.fetchone()[0])
            return res
        query_user = select(Users)
        query_stat = select(Statistics)
        response_user = session.execute(query_user)
        response_stat = session.execute(query_stat)
        response_user = response_user.all()
        response_stat = response_stat.all()
        res = []
        for i in range(len(response_user)):
            res.append((response_user[i][0], response_stat[i][0]))
        return res


def select_user_id(email: str):
    """
    Find all personal data

    if necessary, select a specific user and enter an id
    """
    with session_factory() as session:
        query = select(Users.id).filter_by(email=email)
        response = session.execute(query)
        res = response.fetchone()[0]
        return res


def new_user(email: str = None, password: str = None, name: str = 'anonim', **id):
    """Create a new user in tables(Users and Statistics)

    P.S. **id accepts id=int"""
    with session_factory() as session:
        user = Users(email=email, password=password, name=name) if id is None else Users(email=email, password=password,
                                                                                         name=name, **id)
        user_statistics = Statistics(id=user.id)
        session.add_all([user, user_statistics])
        session.commit()


def update_user(id_user: int, id: int = None, email: str = None, password: str = None, name: str = None, games: str = None, wins: int = None, money: int = None):
    """ Update data in tables(User, Statistics)"""
    with session_factory() as session:
        user = session.get(Users, id_user)
        user_statistics = session.get(Statistics, id_user)
        if id:
            user.id = id
            user_statistics.id = id
        if password:
            user.password = password
        if email:
            user.email = email
        if name:
            user.name = name
        if games:
            user_statistics.games += games
        if wins:
            user_statistics.wins += wins
        if money:
            user_statistics.money += money
        session.commit()