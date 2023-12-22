# function on the orm
import email
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
"""    
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
"""
# select_Users_ORM()
# new_userORM('asasasa','sasa','sasa' , id = 2)
select_via_email('dimahubulwqsq')