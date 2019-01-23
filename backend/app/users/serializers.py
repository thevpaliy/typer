from marshmallow import Schema, fields, post_dump
from app.auth.serializers import AuthSchema
from app.practice.serializers import SessionSchema, ScoreSchema


class StatisticSchema(Schema):
  class TimeValue(Schema):
    time = fields.Str()
    value = fields.Str()

  words = fields.List(fields.Nested(TimeValue))
  chars = fields.List(fields.Nested(TimeValue))
  accuracy = fields.List(fields.Nested(TimeValue))


class UserSchema(Schema):
  id = fields.Str()
  username = fields.Str()
  email = fields.Str()
  password = fields.Str(load_only=True)
  seenAt = fields.DateTime(attribute='last_seen')
  totalSessions = fields.Int(attribute='sessions_taken')
  scores = fields.Nested(ScoreSchema)


class UserSessionSchema(Schema):
  sessions = fields.Nested(SessionSchema)
  prev = fields.Url()
  next = fields.Url()
  count = fields.Int()


class TokenizedUserSchema(Schema):
  user = fields.Nested(UserSchema)
  auth = fields.Nested(AuthSchema)


user_schema = UserSchema()
tokenized_user_schema = TokenizedUserSchema()
