from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_mail import Mail
from flask_jwt_extended import JWTManager


db = SQLAlchemy()
migrate = Migrate()
mail = Mail()
jwt = JWTManager()

from app.utils import jwt_load, jwt_identity # noqa

jwt.user_identity_loader(jwt_load)
jwt.user_loader_callback_loader(jwt_identity)
