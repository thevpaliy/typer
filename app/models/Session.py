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
