# -*- coding: future_fstrings -*-
import collections
import datetime
from hashlib import md5
from abc import abstractmethod, ABCMeta
from six import add_metaclass
from werkzeug.security import generate_password_hash
from werkzeug.security import check_password_hash
from flask_login import UserMixin
from flask_sqlalchemy import BaseQuery
from operator import attrgetter
from app.database import Model, SurrogatePK, db


USER_ONLINE_TIMEOUT = 300


class TimeQuery(BaseQuery):
  def _within_interval(self, user_id, is_valid):
    now, result = datetime.datetime.now(), []
    for item in self.filter_by(user_id=user_id).all():
      delta = now - item.creation_time
      if is_valid(delta):
        result.append(item)
    return result

  def today(self, user_id):
    return self._within_interval(user_id,
        is_valid = lambda d: d.days <= 1)

  def last_month(self, user_id):
    return self._within_interval(user_id,
        is_valid = lambda d: d.days <= 30)

  def last_week(self, user_id):
    return self._within_interval(user_id,
      is_valid = lambda d: d.days <= 7)


class TimeModel(Model):
  __abstract__ = True
  query_class = TimeQuery

  @property
  @abstractmethod
  def creation_time(self):
    """Returns the creation date."""


class ScoresModel(object):
  __slots__ = ('words', 'chars', 'accuracy')

  def __init__(self, words, chars, accuracy):
    self.words = words
    self.chars = chars
    self.accuracy = accuracy


@add_metaclass(ABCMeta)
class Statistics(object):
  def __init__(self, user):
    self.user = user

  @abstractmethod
  def _generate_stat(self, field_getter):
    """Return max statistics for a specified category
     within a specified period of time."""

  @property
  def words(self):
    return self._generate_stat(
      field_getter = lambda s: s.words
    )

  @property
  def accuracy(self):
    return self._generate_stat(
      field_getter = lambda s: s.accuracy
    )

  @property
  def chars(self):
    return self._generate_stat(
      field_getter = lambda s: s.chars
    )

  @property
  def scores(self):
    def _format(data):
      return [dict(zip(('time', 'value'), (t, v)))
          for t, v in data.items()]
    return ScoresModel(
      words=_format(self.words),
      chars=_format(self.chars),
      accuracy=_format(self.accuracy)
    )


class DailyStats(Statistics):
  def _generate_stat(self, field_getter):
    def _format_time(time):
      if time < 10:
        return f'0{time}'
      return time
    sessions, result = Session.query.today(self.user.id), {}
    for session in sessions:
      time = session.created_date
      time = '{hours}:{minutes}'.format(
        hours = _format_time(time.hour),
        minutes = _format_time(time.minute)
      )
      result[time] = max(result.get(time, -1), field_getter(session))
    strptime =datetime.datetime.strptime
    result = sorted(result.items(),
      key = lambda x: strptime(x[0],'%H:%M').time())
    return collections.OrderedDict(result)


class WeeklyStats(Statistics):
  def _generate_stat(self, field_getter):
    sessions, result = Session.query.last_week(self.user.id), {}
    for session in sessions:
      day = session.created_date.day
      result[day] = max(result.get(day, -1), field_getter(session))
    return result


class MonthlyStats(Statistics):
  def _generate_stat(self, field_getter):
    sessions, result = Session.query.last_month(self.user.id), {}
    for session in sessions:
      day = session.created_date.day
      result[day] = max(result.get(day, -1), field_getter(session))
    return result


class Session(TimeModel, SurrogatePK):
  __tablename__ = 'sessions'

  words = db.Column(db.Integer, default=0)
  chars = db.Column(db.Integer, default=0)
  accuracy = db.Column(db.Float, default=0.0)
  created_date = db.Column(db.DateTime, default=datetime.datetime.utcnow)
  user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

  @property
  def creation_time(self):
    return self.created_date

  @property
  def scores(self):
    return ScoresModel(
      words = self.words,
      chars = self.chars,
      accuracy = self.accuracy
    )

  def __repr__(self):
    return f'<Session {self.words}>'


class User(Model, SurrogatePK, UserMixin):
  __tablename__ = 'users'

  social_id = db.Column(db.String(128), unique=True)
  email = db.Column(db.String(64), unique=True, index=True)
  username = db.Column(db.String(64), unique=True, index=True)
  password_hash = db.Column(db.String(128))
  last_seen = db.Column(db.DateTime, default=datetime.datetime.utcnow)
  sessions = db.relationship('Session', backref='user', lazy='dynamic')

  @property
  def password(self):
    raise AttributeError('password is not readable')

  @property
  def is_online(self):
    if self.last_seen:
      now = datetime.datetime.now()
      delta = datetime.timedelta(seconds=USER_ONLINE_TIMEOUT)
      return (now - self.last_seen) < delta
    return False

  @password.setter
  def password(self, password):
    self.password_hash = generate_password_hash(password)

  def _get_average(self, field_getter):
    if self.sessions.count() != 0:
      return sum(field_getter(s) for s in self.sessions) / self.sessions.count()
    return 0

  @property
  def sessions_taken(self):
    return self.sessions.count()

  @property
  def words_score(self):
    return self._get_average(
      field_getter = lambda x: x.words
    )

  @property
  def accuracy_score(self):
    score = round(self._get_average(
      field_getter = lambda x: x.accuracy
    ))
    return int(score)

  @property
  def chars_score(self):
    return self._get_average(
      field_getter = lambda x: x.chars
    )

  @property
  def daily_stats(self):
    if not hasattr(self, '_daily_stats'):
      self._daily_stats = DailyStats(self)
    return self._daily_stats

  @property
  def weekly_stats(self):
    if not hasattr(self, '_weekly_stats'):
      self._weekly_stats = WeeklyStats(self)
    return self._weekly_stats

  @property
  def monthly_stats(self):
    if not hasattr(self, '_monthly_stats'):
      self._monthly_stats = MonthlyStats(self)
    return self._monthly_stats

  def avatar(self, size):
    digest = md5(self.email.lower().encode('utf-8')).hexdigest()
    return f'https://www.gravatar.com/avatar/{digest}?d=identicon&s={size}'

  def verify_password(self, password):
    # if the user signed up with a provider, deny
    if not self.password_hash:
      return False
    return check_password_hash(self.password_hash, password)

  def __repr__(self):
    return f'<User {self.username}>'
