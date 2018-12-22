from flask import Flask
from app.extensions import db, bootstrap, migrate, login, mail


def register_blueprints(app):
  from app.auth import auth
  from app.auth.utils import load_user
  from app.main import main
  from app.errors import errors
  from app.api import api

  login.login_view = 'auth.login'

  app.register_blueprint(auth)
  app.register_blueprint(main)
  app.register_blueprint(errors)
  app.register_blueprint(api)


def register_extensions(app):
  db.init_app(app)
  migrate.init_app(app, db)
  bootstrap.init_app(app)
  login.init_app(app)
  mail.init_app(app)


def create_app(config):
  app =  Flask(__name__)
  app.config.from_object(config)

  register_extensions(app)
  register_blueprints(app)

  return app
