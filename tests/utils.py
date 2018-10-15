import datetime
import random
from app import db
from app.models import User, Session


def generate_user(**kwargs):
  user = User(
    username = kwargs.get('username','username-example'),
    email = kwargs.get('email', 'example@email.com'),
    password = kwargs.get('password', 'example-password'),
    last_seen = kwargs.get('last_seen', datetime.datetime.now())
  )
  db.session.add(user)
  db.session.commit()
  return user


def generate_session(user_id, **kwargs):
  random_int = lambda :random.randint(10,300)
  session = Session(
      user_id = user_id,
      words = kwargs.get('words', random_int()),
      chars = kwargs.get('chars', random_int()),
      accuracy = kwargs.get('accuracy', random_int()),
      created_date = kwargs.get('created_date', datetime.datetime.now())
  )
  db.session.add(session)
  db.session.commit()
  return session


def generate_sessions_within(user_id, delta_generator, count=10):
  sessions = []
  for index in range(count):
    delta = delta_generator()
    sessions.append(generate_session(
      user_id = user_id,
      created_date = datetime.datetime.now() - delta
    ))
  return sessions
