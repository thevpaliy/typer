from app.users import users
from app.users.models import User, TokenizedUser
from flask_apispec import use_kwargs, marshal_with
from flask_jwt_extended import jwt_required, jwt_optional, current_user
from app.exceptions import InvalidUsage
from sqlalchemy.exc import IntegrityError
from app.auth.models import AuthModel
from app.users.serializers import user_schema, tokenized_user_schema


@users.route('/api/users/login', methods=('POST', ))
@use_kwargs(user_schema)
@marshal_with(tokenized_user_schema)
@jwt_optional
def login(username, password, **kwargsa):
  user = User.query.filter_by(username=username).first()
  if user is None:
    user = User.query.filter_by(email=username).first()
  if user is not None and user.verify_password(password):
    auth = AuthModel.create(identity=user)
    return TokenizedUser(auth, user)
  raise InvalidUsage.user_not_found()


@users.route('/api/users/register', methods=('POST', ))
@use_kwargs(user_schema)
@marshal_with(tokenized_user_schema)
def register(email, username, password, **kwargs):
  try:
    user = User.create(
      email=email,
      username=username,
      password=password,
      **kwargs
    )
  except IntegrityError:
    db.session.rollback()
    raise InvalidUsage.user_already_registered()
  auth = AuthModel.create(identity=user)
  return TokenizedUser(auth, user)


@users.route('/api/users/recover', methods=('POST', ))
@use_kwargs(user_schema)
def recover_password(username):
  pass


@users.route('/api/users/me', methods=('GET', ))
@use_kwargs(user_schema)
@jwt_required
def get_me():
  pass
