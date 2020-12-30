import sqlite3
import utils
CONFIG = utils

def create_tables():
    conn,curs = _connect()
    curs.execute('''CREATE TABLE users
             (id TEXT NOT NULL PRIMARY KEY, msg_count INTEGER)''')
    conn.commit()

def new_user(id,count):
    conn,curs = _connect()
    curs.execute(f"INSERT INTO users VALUES ({id},{count}")
    conn.commit()

def _connect():
    conn = sqlite3.connect(CONFIG.db_name)
    return conn,conn.cursor