from marshmallow import Schema, fields, post_dump


class ScoreSchema(Schema):
  words = fields.Int()
  chars = fields.Int()
  accuracy = fields.Float()


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
  seenAt = fields.DateTime(attribute='last_seen')
  totalSessions = fields.Int(attribute='sessions_taken')
  scores = fields.Nested(ScoreSchema)


class SessionSchema(Schema):
  id = fields.Str()
  userId = fields.Str(attribute='user_id')
  scores = fields.Nested(ScoreSchema)
  createdAt = fields.DateTime(attribute='created_date')


class UserSessionSchema(Schema):
  sessions = fields.Nested(SessionSchema)
  prev = fields.Url()
  next = fields.Url()
  count = fields.Int()
