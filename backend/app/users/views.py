from flask import jsonify, request, url_for
from app.users import users
from app.extensions import db
from app.users.models import User, TokenizedUser, PaginationModel
from flask_apispec import use_kwargs, marshal_with
from flask_jwt_extended import jwt_required, jwt_optional, current_user
from app.exceptions import InvalidUsage
from sqlalchemy.exc import IntegrityError
from app.auth.models import AuthModel
from app.users.serializers import (user_schema, statistics_schema,
      tokenized_user_schema, users_session_schema)
from flask import jsonify


@users.route('/api/users/login', methods=('POST', ))
@use_kwargs(user_schema)
@marshal_with(tokenized_user_schema)
@jwt_optional
def login(username, password, **kwargsa):
  user = User.first(username=username, email=username)
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
  return TokenizedUser(user, auth)


@users.route('/api/users/recover', methods=('POST', ))
@use_kwargs(user_schema)
def recover_password(username):
  user = User.first(username=username, email=username)
  if user is not None:
    return jsonify({'message': 'Please check your email to restore your password'})
  raise InvalidUsage.user_not_found()


@users.route('/api/users/me', methods=('GET', ))
@use_kwargs(user_schema)
@jwt_required
def get_me():
  return current_user


@users.route('/api/users/<path:username>', methods=('GET', ))
@jwt_optional
@marshal_with(user_schema)
def get_user_profile(username):
  user = User.first(username=username, email=username)
  if user is None:
    raise InvalidUsage.user_not_found()
  return user


@users.route('/api/users/<int:id>/sessions')
@marshal_with(users_session_schema)
def get_user_sessions(id):
  user = User.first(id=id)
  if user is None:
    raise InvalidUsage.user_not_found()
  page = request.args.get('page', 1, type=int)
  pagination = user.sessions.paginate(
    page, per_page=25, error_out=False
  )
  sessions = pagination.items
  return PaginationModel(
    page=page,
    data=sessions,
    total_pages=max(pagination.total // 25, 1),
    total_results=pagination.total
  )


@users.route('/api/users/<int:id>/statistics')
@marshal_with(statistics_schema)
def get_users_statistics(id):
  user = User.first(id=id)
  if user is None:
    raise InvalidUsage.user_not_found()
  return user.statistics
