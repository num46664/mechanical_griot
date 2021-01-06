from griotlib import db

USERS = [1,2,70,71,69,77,62,155,222,282]
MSG_LVL = 5

for user in USERS:
    db.new_user(user,MSG_LVL)