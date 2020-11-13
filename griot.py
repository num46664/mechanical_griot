from mastodon import Mastodon
from time import sleep
import utils
CONFIG = utils.conf()

mastodon = Mastodon(
    access_token = CONFIG['usercred'],
    api_base_url= CONFIG['url'],
    ratelimit_method='wait'
)

# mastodon.status_post('@root test...', visibility='direct')

def get_users():
    with open('users','r') as f:
        return {line.strip() for line in set(f.readlines())}

def fresh_users():
    followers = mastodon.account_followers(mastodon.me())
    users = [f for f in followers if ('@' not in f['acct'])]
    return [user for user in users if str(user['id']) not in get_users()]

def save_users(users):
    with open('users','a') as f:
        for user in users:
            f.write(f"{user['id']}\n") 

def messages_for(user):
    with open('messages','r') as messages:
        mess = [
            f"@{user['username']}\n"+message.strip() for message in messages.read().split('---')
        ]
        mess[0] = f"Welcome to okapi.website "+mess[0]
        return mess

def welcome():
    fresh = fresh_users()
    for user in fresh:
        for message in messages_for(user):
            # print(message)
            mastodon.status_post(message,visibility='direct')
            sleep(1)
    save_users(fresh)

