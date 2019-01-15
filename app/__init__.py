from flask import Flask
from app.api.errors import InvalidUsage
from app.extensions import db, bootstrap, migrate, login, mail, jwt


def register_blueprints(app):
  from app.auth import auth
  from app.auth.utils import load_user
  from app.main import main
  from app.errors import errors
  from app.api import api


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
  jwt.init_app(app)


def register_api_error_handlers(app):
  def error_handler(error):
    response = error.to_json()
    response.status_code = error.status_code
    return response
  app.errorhandler(InvalidUsage)(error_handler)


def create_app(config):
  app =  Flask(__name__)
  app.config.from_object(config)

  register_extensions(app)
  register_blueprints(app)
  register_api_error_handlers(app)

  return app
