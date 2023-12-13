from dotenv import load_dotenv
import os
load_dotenv()


def pg():
    return f"{os.getenv('config_pg')}://{os.getenv('user')}:{os.getenv('password')}@localhost:5432/"