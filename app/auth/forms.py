from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms import validators, ValidationError

from app.models import User

class LoginForm(FlaskForm):
  username = StringField('Email or username', [
    validators.Required(),
    validators.Length(min=1, max=64)
  ])

  password = PasswordField('Password', [
    validators.Required(),
    validators.Length(min=8, max=20)
  ])

  remember_me = BooleanField('Keep me logged in')
  submit = SubmitField('Log In')

class RegisterForm(FlaskForm):
  email = StringField('Email', [
    validators.Required(),
    validators.Email(),
    validators.Length(min=6, max=64)
  ])

  username = StringField('Username', [
    validators.Required(),
    validators.Length(min=1, max=64),
    validators.Regexp('^[A-Za-z][A-Za-z0-9_.]*$', 0,
      message = 'Usernames must have only letters, '
      'numbers, dots or underscores')
  ])

  password = PasswordField('Password', [
    validators.Required(),
    validators.Length(min=8, max=20),
    validators.EqualTo('repeat_password', message='Passwords must match')
  ])

  repeat_password = PasswordField('Confirm password', [
    validators.Required()
  ])

  submit = SubmitField('Sign Up')

  def validate_email(self, email):
    if User.query.filter_by(email=email.data).first():
      raise ValidationError('Email has already been used by another user')

  def validate_username(self, username):
    if User.query.filter_by(username=username.data).first():
      raise ValidationError('Username has already been used by another user')
