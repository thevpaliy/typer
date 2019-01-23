from marshmallow import Schema, fields, post_dump


class SessionResult(Schema):
  words = fields.Int()
  chars = fields.Int()
  accuracy = fields.Float()


class SessionSchema(Schema):
  id = fields.Str()
  userId = fields.Str(attribute='user_id')
  scores = fields.Nested(ScoreSchema)
  createdAt = fields.DateTime(attribute='created_date')
