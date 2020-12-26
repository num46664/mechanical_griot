import sqlite3
import utils
CONFIG = utils

def connect():
    conn = sqlite3.connect(CONFIG.db_name)
    return conn,conn.cursor

def create_tables():
    conn,curs = connect()
    curs.execute('''CREATE TABLE users
             (id text, msg_count integer)''')
    conn.commit()

def new_user(id,count):
    conn,curs = connect()
    curs.execute(f"INSERT INTO users VALUES ({id},{count}")