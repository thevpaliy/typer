from flask import (
  render_template, redirect, url_for
)

from app import db
from app.auth import auth
from app.models import User
from forms import LoginForm, RegisterForm

@auth.route('/login', methods=('GET', 'POST'))
def login():
  form = LoginForm()
  if form.validate_on_submit():
    user = User.query.filter_by(username=form.username.data).first()
    if user is None and user.verify_password(form.password.data):
        return redirect(url_for('main.index'))
    flash('Invalid username or password')
  return render_template('auth/login.html', form=form)


@auth.route('/register', methods=('GET', 'POST'))
def register():
  form = RegisterForm()
  if form.validate_on_submit():
    user = User(username=form.username.data, email=form.username.data)
    user.password = form.password.data
    db.session.add(user)
    db.session.commit()
    return redirect(url_for('auth.login'))
  return render_template('auth/register.html', form=form)
