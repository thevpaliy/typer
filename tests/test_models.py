import unittest
import utils
import datetime
import random
from _base import BaseTestCase
from app.models import User, Session
from app import create_app


class UserModelTestCase(BaseTestCase):
  def test_to_json(self):
    now = datetime.datetime.now()
    session = utils.generate_session(
      words = 100,
      chars = 200,
      accuracy = 100.0,
      created_date = now,
      user_id = 1
    )
    user = utils.generate_user(
      id = 1,
      social_id = 2,
      email = 'example@email.com',
      username = 'example',
      last_seen = now
    )
    self.assertEqual({
      'id': 1,
      'username': 'example',
      'email': 'example@email.com',
      'last_seen': now,
      'sessions': 1,
      'words_score': 100,
      'chars_score': 200,
      'accuracy_score': 100.0
    }, user.to_json())


class SessionModelTestCase(BaseTestCase):
  def test_to_json(self):
    # no need to add this to the database
    now = datetime.datetime.now()
    session = Session(
      id = 1,
      words = 100,
      chars = 200,
      accuracy = 100.0,
      created_date = now,
      user_id = 1
    )
    self.assertEqual({
      'id': 1,
      'words': 100,
      'chars': 200,
      'accuracy': 100.0,
      'created_date': now,
      'user_id': 1
    }, session.to_json())

  def test_creation_date(self):
    session = utils.generate_session(user_id=1)
    self.assertTrue((
      datetime.datetime.now() - session.created_date).total_seconds() < 3)

  def test_repr(self):
    session = utils.generate_session(user_id=10)
    self.assertEqual('<Session {!r}>'.format(session.words), repr(session))

  def test_within_day_interval(self):
    user = utils.generate_user()
    sessions = utils.generate_sessions_within(user.id,
        lambda : datetime.timedelta(minutes=random.randint(0, 360)))
    query_result = Session.query.today(user.id)
    self.assertEqual(sorted(sessions), sorted(query_result))
    self.assertEqual([], Session.query.today(-1))

  def test_within_week_interval(self):
    user = utils.generate_user()
    sessions = utils.generate_sessions_within(user.id,
        lambda : datetime.timedelta(days=random.randint(0, 7)))
    query_result = Session.query.last_week(user.id)
    self.assertEqual(sorted(sessions), sorted(query_result))
    self.assertEqual([], Session.query.last_week(-1))

  def test_within_month_interval(self):
    user = utils.generate_user()
    sessions = utils.generate_sessions_within(user.id,
        lambda : datetime.timedelta(days=random.randint(0, 30)))
    query_result = Session.query.last_month(user.id)
    self.assertEqual(sorted(sessions), sorted(query_result))
    self.assertEqual([], Session.query.last_month(-1))
