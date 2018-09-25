from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask_migrate import Migrate
from flask_login import LoginManager

db = SQLAlchemy()
bootstrap = Bootstrap()
migrate = Migrate()
login = LoginManager()

def create_app(config):
  app =  Flask(__name__)
  app.config.from_object(config)

  db.init_app(app)
  migrate.init_app(app, db)
  bootstrap.init_app(app)
  login.init_app(app)

  from app.auth import auth
  from app.auth.utils import load_user
  app.register_blueprint(auth)
  login.login_view = 'auth.login'

  from app.main import main
  app.register_blueprint(main)

  from app.errors import errors
  app.register_blueprint(errors)
  
  return app
