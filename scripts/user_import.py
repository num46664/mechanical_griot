from src import db

USERS = []
MSG_LVL = 5

for user in USERS:
    db.new_user(user,MSG_LVL)