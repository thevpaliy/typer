import os
from collections import namedtuple

from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__name__))

load_dotenv(os.path.join(basedir, '.env'), verbose=True)

OAuthConfig = namedtuple('OAuthConfig', 'client_id, secret_id')

OAUTH_FACEBOOK_CONFIG = OAuthConfig(
  client_id = os.getenv('facebook-client-id'),
  secret_id = os.getenv('facebook-secret-id')
)

OAUTH_TWITTER_CONFIG = OAuthConfig(
  client_id = os.getenv('twitter-client-id'),
  secret_id = os.getenv('twitter-secret-id')
)

class Config(object):
  SECRET_KEY = os.getenv('secret-key')
  SQLALCHEMY_TRACK_MODIFICATIONS = False
  OAUTH = dict(zip(('facebook','twitter'),
    (OAUTH_FACEBOOK_CONFIG, OAUTH_TWITTER_CONFIG)))


class Production(Config):
  SQLALCHEMY_DATABASE_URI = os.environ.get('database-url') or \
        'sqlite:///' + os.path.join(basedir, 'data-dev.sqlite')


class Development(Config):
  DEBUG = True
  SQLALCHEMY_DATABASE_URI = os.environ.get('database-url') or \
        'sqlite:///' + os.path.join(basedir, 'data-dev.sqlite')


config = {
  'development': Development,
  'production': Production
}
