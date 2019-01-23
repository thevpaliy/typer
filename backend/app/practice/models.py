# -*- coding: future_fstrings -*-
import datetime
from app.database import (TimeModelMixin, Column, db, SurrogatePK)


class Session(TimeModelMixin, SurrogatePK):
  __tablename__ = 'sessions'

  words = Column(db.Integer, default=0)
  chars = Column(db.Integer, default=0)
  accuracy = Column(db.Float, default=0.0)
  created_date = Column(db.DateTime, default=datetime.datetime.utcnow)
  user_id = Column(db.Integer, db.ForeignKey('users.id'))

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
