from flask import render_template, request, \
        redirect, url_for, flash, current_app
from flask_login import login_user, \
  current_user, logout_user, login_required
from werkzeug.urls import url_parse

import app.email as email
from app import db
from app import login
from app.auth import auth
from app.models import User
from app.auth.oauth import OAuthFactory
from app.auth.utils import *
from forms import *


@auth.route('/login', methods=('GET', 'POST'))
def login():
  if current_user.is_authenticated:
    return redirect(get_next_page('main.practice'))
  form = LoginForm()
  if form.validate_on_submit():
    user = User.query.filter_by(username=form.username.data).first()
    if user is None:
      user = User.query.filter_by(email=form.username.data).first()
    if user is not None and user.verify_password(form.password.data):
        login_user(user, remember=form.remember_me.data)
        return redirect(get_next_page('main.practice'))
    flash('Invalid username or password')
  return render_template('auth/login.html', form=form)


@auth.route('/register', methods=('GET', 'POST'))
def register():
  if current_user.is_authenticated:
    return redirect(url_for('main.index'))
  form = RegisterForm()
  if form.validate_on_submit():
    user = User(username=form.username.data, email=form.email.data)
    user.password = form.password.data
    db.session.add(user)
    db.session.commit()
    return redirect(url_for('auth.login'))
  return render_template('auth/register.html', form=form)


@auth.route('/logout')
@login_required
def logout():
  logout_user()
  return redirect(url_for('main.practice'))


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
    flash('Authentication failed')
    return redirect(url_for('auth.login'))
  user = User.query.filter_by(email=email).first()
  if not user:
    user = User(username=username, email=email, social_id=social_id)
    db.session.add(user)
    db.session.commit()
  login_user(user)
  return redirect(get_next_page('main.practice'))


@auth.route('/reset', methods=('GET', 'POST'))
def request_password_reset():
  if current_user.is_authenticated:
    return redirect(url_for('main.practice'))
  form = RequestResettingPasswordForm()
  if form.validate_on_submit():
    user = User.query.filter_by(email=form.email.data).first()
    if user is not None:
      token = generate_password_token(user)
      email.send_reset_password(user, token)
      flash('Please check your email')
      return redirect(url_for('auth.login'))
  return render_template('auth/reset_request.html', form=form)


@auth.route('/reset/<path:token>', methods=('GET', 'POST'))
def reset_password(token):
  if current_user.is_authenticated:
    return redirect(url_for('main.practice'))
  user = get_user_from_token(token)
  if not user:
    abort(404)
  form = ResetPasswordForm()
  if form.validate_on_submit():
    user.password = form.password.data
    db.session.commit()
    flash('Your password has been reset')
    return redirect(url_for('auth.login'))
  return render_template('auth/reset.html', form=form)


# XXX: should I move this out of this module?
def get_next_page(default):
  next_page = request.args.get('next')
  if not next_page:
    next_page = url_for(default)
  return next_page
