from marshmallow import Schema, fields, pre_load


class ScoresSchema(Schema):
  words = fields.Int(required=True, allow_none=False)
  chars = fields.Int(required=True, allow_none=False)
  accuracy = fields.Float(required=True, allow_none=False)


class SessionSchema(Schema):
  id = fields.String(required=True, allow_none=False)
  userId = fields.String(attribute='user_id')
  scores = fields.Nested(ScoresSchema)
  createdAt = fields.DateTime(attribute='created_date')

  @pre_load
  def parse(self, data):
    if 'id' in data and data['id']:
      data['id'] = str(data['id'])


scores_schema = ScoresSchema()
session_schema = SessionSchema()
