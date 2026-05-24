from marshmallow import Schema, fields


class RefreshSchema(Schema):

    refresh_token = fields.String(
        required=True
    )