from flask import (request, redirect, url_for, flash, current_app)

import app.email
from app.extensions import db
from app.auth import auth
from app.models import User, AuthModel
from app.auth.serializers import auth_schema
from app.auth.oauth import OAuthFactory
from flask_apispec import use_kwargs, marshal_with
from app.users.serializers import user_schema, tokenized_user_schema
from flask_jwt_extended import jwt_refresh_token_required


@auth.route('/authorize/<path:provider>')
def oauth_authorize(provider):
  oauth_config = current_app.config['OAUTH'][provider]
  provider = OAuthFactory.get_provider(provider, oauth_config)
  return provider.authorize()


@auth.route('/callback/<path:provider>')
def oauth_callback(provider):
  provider = OAuthFactory.get_provider(provider)
  social_id, username, email = provider.callback()
  if not social_id:
    return redirect(url_for('auth.login'))
  user = User.query.filter_by(email=email).first()
  if not user:
    user = User(username=username, email=email, social_id=social_id)
    db.session.add(user)
    db.session.commit()
  # TODO: replace it
  return redirect(get_next_page('main.practice'))


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
