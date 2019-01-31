from flask import (request, redirect, url_for, flash, current_app)

import app.email
from app.extensions import db
from app.auth import auth
from app.models import User, AuthModel
from app.auth.serializers import auth_schema, auth_provider_schema
from app.auth.oauth import OAuthFactory
from flask_apispec import use_kwargs, marshal_with
from app.users.serializers import user_schema, tokenized_user_schema
from flask_jwt_extended import jwt_refresh_token_required
from app.models import TokenizedUser
from app.users.serializers import AuthSchema


@auth.route('/authorize/<path:provider>')
@use_kwargs(auth_provider_schema)
def oauth_authorize(provider, callback_url):
  oauth_config = dict(current_app.config['OAUTH'][provider])
  oauth_config.callback_url = callback_url
  provider = OAuthFactory.get_provider(provider, oauth_config)
  return provider.authorize()


@auth.route('/callback/<path:provider>')
@marshal_with(tokenized_user_schema)
def oauth_callback(provider):
  provider = OAuthFactory.get_provider(provider)
  social_id, username, email = provider.callback()
  if not social_id:
    raise InvalidUsage.unknown_error()
  user = User.query.filter_by(email=email, username=username).first()
  if not user:
    try:
      user = User(username=username, email=email, social_id=social_id)
      db.session.add(user)
      db.session.commit()
    except IntegrityError:
      db.session.rollback()
      raise InvalidUsage.unknown_error()
    auth = AuthModel.create(user)
    return TokenizedUser(user, auth)
  raise InvalidUsage.user_already_registered()


@auth.route('/api/refresh', methods=('POST', 'GET'))
@marshal_with(auth_schema)
@jwt_refresh_token_required
def refresh_token(**kwargs):
  user = current_user
  return AuthModel.create(user)


def get_next_page(default):
  next_page = request.args.get('next')
  if not next_page:
    next_page = url_for(default)
  return next_page
