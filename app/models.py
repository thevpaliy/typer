from hashlib import md5
from werkzeug.security import generate_password_hash
from werkzeug.security import check_password_hash
from flask_login import UserMixin

from app import db

class Session(db.Model):
  __tablename__ = 'sessions'

  id = db.Column(db.Integer, primary_key=True)
  words = db.Column(db.Integer)
  chars = db.Column(db.Integer)
  accuracy = db.Column(db.Float)
  date = db.Column(db.Date)
  user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

  def __repr__(self):
    return '<Session {!r}>'.format(self.words)


class User(db.Model, UserMixin):
  __tablename__ = 'users'

  id = db.Column(db.Integer, primary_key=True)
  social_id = db.Column(db.String(128), unique=True)
  email = db.Column(db.String(64), unique=True, index=True)
  username = db.Column(db.String(64), unique=True, index=True)
  password_hash = db.Column(db.String(128))

  @property
  def password(self):
    raise AttributeError('password is not readable')

  @password.setter
  def password(self, password):
    self.password_hash = generate_password_hash(password)

  def avatar(self, size):
    digest = md5(self.email.lower().encode('utf-8')).hexdigest()
    return 'https://www.gravatar.com/avatar/{}?d=identicon&s={}'.format(digest, size)

  def verify_password(self, password):
    return check_password_hash(self.password_hash, password)

  def __repr__(self):
    return '<User {!r}>'.format(self.username)
