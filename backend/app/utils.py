import app.models


def jwt_load(user):
  return user.id


def jwt_identity(payload):
  return User.query.filter_by(id=payload).first()
