from flask import (request, redirect, url_for, flash, current_app)

import app.email as email
from app import db
from app import login
from app.auth import auth
from app.models import User
from app.auth.oauth import OAuthFactory
from app.auth.utils import generate_password_token, get_user_from_token


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


@auth.route('/password-reset-request', methods=('POST',))
def request_password_reset():
  # TODO: implement
  pass


@auth.route('/password-reset/<path:token>', methods=('GET', 'POST'))
def reset_password(token):
  user = get_user_from_token(token)
  if not user:
    # TODO: explain why this happened to the user
    flash('Invalid token')
  user.password = form.password.data
  db.session.commit()
  return None


def get_next_page(default):
  next_page = request.args.get('next')
  if not next_page:
    next_page = url_for(default)
  return next_page
