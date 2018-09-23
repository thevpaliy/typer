from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask_migrate import Migrate

db = SQLAlchemy()
bootstrap = Bootstrap()
migrate = Migrate()

def create_app(config):
  app =  Flask(__name__)
  app.config.from_object(config)

  db.init_app(app)
  migrate.init_app(app, db)
  bootstrap.init_app(app)

  from app.auth import auth
  app.register_blueprint(auth)

  from app.main import main
  app.register_blueprint(main)

  return app
