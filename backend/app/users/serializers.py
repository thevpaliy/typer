# -*- coding: future_fstrings -*-

from marshmallow import Schema, fields, pre_dump
from app.auth.serializers import AuthSchema
from app.practice.serializers import SessionSchema, ScoresSchema


class StatisticsSchema(Schema):
  class TimeValue(Schema):
    time = fields.Int()
    value = fields.Int()

    @pre_dump
    def convert_to_objects(self, data):
      if len(data) != 2:
        raise ValueError(
          f'A tuple should have 2 elements, found {len(data)}'
        )
      time, value = data
      return dict(time=time, value=value)

  words = fields.List(fields.Nested(TimeValue))
  chars = fields.List(fields.Nested(TimeValue))
  accuracy = fields.List(fields.Nested(TimeValue))


class SummarySchema(Schema):
  monthly = fields.Nested(StatisticsSchema)
  weekly = fields.Nested(StatisticsSchema)
  daily = fields.Nested(StatisticsSchema)


class UserSchema(Schema):
  id = fields.String()
  username = fields.String()
  email = fields.String()
  password = fields.String(load_only=True)
  seenAt = fields.DateTime(attribute='last_seen')
  totalSessions = fields.Int(attribute='sessions_taken')
  scores = fields.Nested(ScoresSchema)
  callback_url = fields.String(load_only=True)


class TokenizedUserSchema(Schema):
  user = fields.Nested(UserSchema)
  auth = fields.Nested(AuthSchema)


def create_pagination_schema(DataSchema):
  class PaginationSchema(Schema):
    data = fields.List(fields.Nested(DataSchema))
    page = fields.Int()
    total_pages = fields.Int()
    total_results = fields.Int()
  return PaginationSchema()


user_schema = UserSchema()
statistics_schema = SummarySchema()
users_session_schema = create_pagination_schema(SessionSchema)
tokenized_user_schema = TokenizedUserSchema()
