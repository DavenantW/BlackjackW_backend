# the file for database functions
from bcrypt import checkpw, gensalt, hashpw


def ps_hash(password: str):
    password = password.encode('utf-8')
    return hashpw(password, gensalt())


def ps_check(password: str, email: str):
    password_db = user_email(email)
    return checkpw(password, password_db)