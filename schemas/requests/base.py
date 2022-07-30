from marshmallow import Schema, fields, validate


class BaseRequestSchema(Schema):
    email = fields.Email(required=True)
    password = fields.String(required=True, validate=validate.Length(min=8, max=20))


class BaseRequestUserSchema(BaseRequestSchema):

    first_name = fields.String(required=True,validate=validate.Length(min=2, max=20))
    last_name = fields.String(required=True, validate=validate.Length(min=2, max=20))
    phone = fields. String(required=True, validate=validate.Length(min=10, max=20))
    role = fields.String(required=False)