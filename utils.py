from mastodon import Mastodon
import config

def init(config):
    Mastodon.create_app(
        config['app_name'],
        api_base_url = config['url'],
        to_file = config['clientcred']
    )

def log_in(config):
    mastodon = Mastodon(
        client_id= config['clientcred'],
        api_base_url= config['url']
    )
    mastodon.log_in(
        config['email'],
        config['pw'],
        to_file=config['usercred']
    )

def conf():
    return config.CONFIG
