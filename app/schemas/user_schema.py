from marshmallow import Schema, fields


class UserSchema(Schema):

    id = fields.Integer()

    username = fields.String()

    email = fields.Email()

    created_at = fields.DateTime()