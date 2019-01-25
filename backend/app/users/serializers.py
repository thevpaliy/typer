from marshmallow import Schema, fields, post_dump
from app.auth.serializers import AuthSchema
from app.practice.serializers import SessionSchema, ScoresSchema


class StatisticSchema(Schema):
  class TimeValue(Schema):
    time = fields.String()
    value = fields.String()

  words = fields.List(fields.Nested(TimeValue))
  chars = fields.List(fields.Nested(TimeValue))
  accuracy = fields.List(fields.Nested(TimeValue))


class UserSchema(Schema):
  id = fields.String()
  username = fields.String()
  email = fields.String()
  password = fields.String(load_only=True)
  seenAt = fields.DateTime(attribute='last_seen')
  totalSessions = fields.Int(attribute='sessions_taken')
  scores = fields.Nested(ScoresSchema)


class TokenizedUserSchema(Schema):
  user = fields.Nested(UserSchema)
  auth = fields.Nested(AuthSchema)


def create_pagination_schema(DataSchema):
  class PaginationSchema(Schema):
    data = fields.Nested(DataSchema)
    prev = fields.Url()
    next = fields.Url()
    count = fields.Int()
  return PaginationSchema()


user_schema = UserSchema()
statistics_schema = StatisticSchema()
users_session_schema = create_pagination_schema(SessionSchema)
tokenized_user_schema = TokenizedUserSchema()
