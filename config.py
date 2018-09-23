import os

basedir = os.path.abspath(os.path.dirname(__name__))

class Config(object):
  SECRET_KEY = os.getenv('secret-key') or 'default'
  SQLALCHEMY_TRACK_MODIFICATIONS = False

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
