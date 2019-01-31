from app.practice import practice
from app.models import Session
from flask_apispec import use_kwargs, marshal_with
from flask_jwt_extended import jwt_required, jwt_optional, current_user
from app.exceptions import InvalidUsage
from sqlalchemy.exc import IntegrityError
from app.practice.serializers import scores_schema, session_schema
from flask import jsonify


@practice.route('/api/session', methods=('POST', ))
@use_kwargs(scores_schema)
@marshal_with(session_schema)
@jwt_required
def save_session(words, chars, accuracy):
  user = current_user
  try:
    session = Session.create(
      words=words,
      chars=chars,
      accuracy=accuracy,
      user_id=user.id
    )
  except IntegrityError:
    db.session.rollback()
    raise InvalidUsage.unknown_error()
  return session


@practice.route('/api/session', methods=('DELETE', ))
@use_kwargs(session_schema)
@jwt_required
def delete_session(id):
  session = Session.first(id=id)
  if session is None:
    raise InvalidUsage.session_not_found()
  try:
    session.delete(id)
  except IntegrityError:
    db.session.rollback()
    raise InvalidUsage.unknown_error()
  return jsonify(message='Session has been deleted')
