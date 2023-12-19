# function on the orm
from engine import session_factory, engine, Base
from models import *
from sqlalchemy.sql import *


def create_tables():
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)


def select_Users_ORM():
  with session_factory() as session:
			query = select(Users)
			result = session.execute(query)
			all_users = result.all()
   
def new_userORM(email: str, password: str, name: str = 'anonim', **id: int):
    """Add new user in tables (Users, Statistics)"""
    with session_factory() as session:
        user_create = insert(Users).values(email=email, password=password, **id)
        res = session.execute(user_create)
        # create user in Users table
        user_create2 = insert(Statistics).values(id=res.inserted_primary_key[0], name=name)
        session.execute(user_create2)
        # create user in Statistics table
        session.commit()
   
def select_via_email():
  with session_factory() as session:
    users_email = Users.email
    select_user_email = session.get(Users, users_email)
   
def update_User(new_email, new_password, new_name, id_user,id_stat):
  id_user = Users.id
  id_stat = Statistics.id
  with session_factory() as session:
    updates = session.get(Users, id_user)
    updates.email = new_email
    updates.password = new_password
    updates2 = session.get(Statistics, id_stat)
    updates2.name = new_name
    
create_tables()