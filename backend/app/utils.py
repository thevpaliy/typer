from app.users.models import User


def jwt_load(user):
  return user.id


def jwt_identity(payload):
  return User.query.filter_by(id=payload).first()
