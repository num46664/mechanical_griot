from mastodon import Mastodon
import config

# returns config object
# this object is needed to authenticate
def conf():
    return config.CONFIG

# this should never be called at normal runtime
# the credential it produces is good forever
# only call if we need new creds for some reason
def init(config):
    Mastodon.create_app(
        config['app_name'],
        api_base_url = config['url'],
        to_file = config['clientcred']
    )

# this can be called once per runtime, 
# but the creds can be saved and reused
# so there really is no need to call it unless
# you don't have valid creds
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
