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
  password = fields.Str(load_only=True)
  seenAt = fields.DateTime(attribute='last_seen')
  totalSessions = fields.Int(attribute='sessions_taken')
  scores = fields.Nested(ScoreSchema)


class UserSessionSchema(Schema):
  sessions = fields.Nested(SessionSchema)
  prev = fields.Url()
  next = fields.Url()
  count = fields.Int()
