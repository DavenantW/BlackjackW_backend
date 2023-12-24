# function on the orm
from DataBase.factory_engine import session_factory, engine, Base
from DataBase.models import Users, Statistics
from sqlalchemy.sql import *


def create_tables():
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)

'''

def select_Users_ORM():
  with session_factory() as session:
        query = select(Users)
        result = session.execute(query)
        all_users = result.all()
        print(f"{all_users}")


def new_userORM(email: str, password: str, name: str = 'anonim', **id: int):
    """Add new user in tables (Users, Statistics)"""
    with session_factory() as session:
        user_create = Users(email=email, password=password, **id)
        
        # create user in Users table
        user_create2 = Statistics(**id ,name=name)
        session.add_all([user_create2,user_create])
        # create user in Statistics table
        session.commit()


def select_via_email(search_email):
  with session_factory() as session:
    query_email = (select(Users.email).filter_by(email = search_email))
    res = session.execute(query_email)
    res_all = res.all()
    print(f"{query_email.compile(compile_kwargs={"literal_binds":True})}")
    print(res_all)


def update_User(**kwargs):
  id_user = Users.id
  id_stat = Statistics.id
  with session_factory() as session:
    updates = session.get(Users, id_user)
    updates.email = new_email
    updates.password = new_password
    updates2 = session.get(Statistics, id_stat)
    updates2.name = new_name
    
create_tables()
# select_Users_ORM()
# new_userORM('asasasa','sasa','sasa' , id = 2)
select_via_email('dimahubulwqsq')
'''


def select_user(id_user: int = None):
    """ Find all user data in tables(Users, Statistics)
    if necessary, select a specific user and enter an id
    """
    with session_factory() as session:
        if not(id_user is None):
            query_user = select(Users).filter_by(id=id_user)
            query_stat = select(Statistics).filter_by(id=id_user)
            response_user = session.execute(query_user)
            response_stat = session.execute(select(query_stat))
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


def select_user_email(email: str):
    """
    Find all personal data

    if necessary, select a specific user and enter an id
    """
    with session_factory() as session:
        query = select(Users).filter_by(email=email)
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


def update_user(id_user: int, id: int = False, email: str = False, password: str = False, name: str = False, games: str = False, wins: int = False, money: int = False):
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
            user_statistics.games = games
        if wins:
            user_statistics.wins = wins
        if money:
            user_statistics.money = money
        session.commit()