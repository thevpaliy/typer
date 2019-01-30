import jwt
import time
import random
from flask import current_app

from app.models import User


def generate_password_token(user, expires=360):
  payload = dict(user_id=user.id, exp=time.time() + expires)
  return jwt.encode(payload,
    current_app.config['SECRET_KEY'], algorithm='HS256')


def get_user_from_token(token):
  try:
    payload = jwt.decode(token,
      current_app.config['SECRET_KEY'], algorithms='HS256')
  except:
    return None
  else:
    return User.query.get(int(payload['user_id']))


def generate_pin_code():
  return random.randint(100000, 999999)


def jwt_load(user):
  return user.id


def jwt_identity(payload):
  return User.query.filter_by(id=payload).first()
