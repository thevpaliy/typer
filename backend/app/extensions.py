from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_mail import Mail
from flask_jwt_extended import JWTManager


db = SQLAlchemy()
bootstrap = Bootstrap()
migrate = Migrate()
login = LoginManager()
mail = Mail()
jwt = JWTManager()

from app.utils import jwt_load, jwt_identity # noqa

login.login_view = 'auth.login'
jwt.user_identity_loader(jwt_load)
jwt.user_loader_callback_loader(jwt_identity)
