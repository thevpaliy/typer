from flask import render_template, redirect, url_for, flash
from flask_login import login_user, \
  current_user, logout_user, login_required

from app import db
from app import login
from app.auth import auth
from app.models import User
from forms import LoginForm, RegisterForm

@auth.route('/login', methods=('GET', 'POST'))
def login():
  if current_user.is_authenticated:
    return redirect(url_for('main.practice'))
  form = LoginForm()
  if form.validate_on_submit():
    user = User.query.filter_by(username=form.username.data).first()
    if user is None:
      user = User.query.filter_by(email=form.username.data).first()
    if user is not None and user.verify_password(form.password.data):
        login_user(user, remember=form.remember_me.data)
        return redirect(url_for('main.practice'))
    flash('Invalid username or password')
  return render_template('auth/login.html', form=form)


@auth.route('/register', methods=('GET', 'POST'))
def register():
  if current_user.is_authenticated:
    return redirect(url_for('main.index'))
  form = RegisterForm()
  if form.validate_on_submit():
    user = User(username=form.username.data, email=form.username.data)
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
