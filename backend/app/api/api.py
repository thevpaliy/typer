import datetime
from app.api import api
from app.models import User, Session
from app.serializers import SessionResult, SessionSchema, UserSchema
from app.api.errors import InvalidUsage
from app.database import db
from flask_apispec import use_kwargs, marshal_with
from flask_jwt_extended import (jwt_required, jwt_optional, jwt_refresh_token_required,
      create_access_token, create_refresh_token, current_user)


@api.route('/session', methods=('POST',))
@use_kwargs(SessionResult())
@marshal_with(SessionSchema())
@jwt_required
def save_session(words, char, accuracy):
  session = Session.create(
      user_id=current_user.id,
      created_date = datetime.datetime.now(),
      words=words,
      chars=chars,
      accuracy=accuracy
    )
  return session


@api.route('/authenticate', methods=('POST', ))
@use_kwargs(UserSchema())
@jwt_optional
def get_tokens(username, password, **kwargs):
  user = User.query.filter_by(username=username)
  if user is None:
    user = User.query.filter_by(email=username)
  if user is None or user.verify_password(password):
    raise InvalidUsage.user_not_found()
  return None
