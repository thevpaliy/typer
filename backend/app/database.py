from sqlalchemy.orm import relationship
from app.extensions import db
import datetime as dt
from abc import abstractmethod
from flask_sqlalchemy import BaseQuery


Column = db.Column
relationship = relationship

class SurrogatePK(object):
  __table_args__ = {'extend_existing': True}

  id = db.Column(db.Integer, primary_key=True)

  @classmethod
  def get_by_id(cls, record_id):
    if any((
      isinstance(record_id, str) and record_id.isdigit(),
      isinstance(record_id, (int, float))),
    ):
      return cls.query.get(int(record_id))


class Model(db.Model):
  __abstract__ = True

  @classmethod
  def create(cls, **kwargs):
    instance = cls(**kwargs)
    return instance.save()

  def save(self, commit=True):
    db.session.add(self)
    if commit:
      db.session.commit()
    return self

  def delete(self, commit=True):
    db.session.delete(self)
    return commit and db.session.commit()

  def update(self, commit=True, **kwargs):
    for attr, value in kwargs.items():
      setattr(self, attr, value)
    return commit and self.save()


class TimeQuery(BaseQuery):
  def _within_interval(self, user_id, is_valid):
    now, result = dt.datetime.now(), []
    for item in self.filter_by(user_id=user_id).all():
      delta = now - item.created_at
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


class TimeModelMixin(Model):
  __abstract__ = True
  query_class = TimeQuery

  @property
  @abstractmethod
  def created_at(self):
    """Returns the creation date."""
