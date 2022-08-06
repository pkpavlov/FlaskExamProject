from marshmallow import Schema, fields, validate, validates, ValidationError
from password_strength import PasswordPolicy


policy = PasswordPolicy.from_names(
    uppercase=1,
    numbers=1,
    special=1,
    nonletters=1,
)


class BaseRequestSchema(Schema):
    email = fields.Email(required=True)
    password = fields.String(required=True, validate=validate.Length(min=8, max=20))

    @validates("password")
    def validate_password(self, password):
        errors = policy.test(password)
        if errors:
            raise ValidationError("Password does not meet requirements")


class BaseRequestUserSchema(BaseRequestSchema):

    first_name = fields.String(required=True, validate=validate.Length(min=2, max=20))
    last_name = fields.String(required=True, validate=validate.Length(min=2, max=20))
    phone = fields.String(required=True, validate=validate.Length(min=10, max=20))
    role = fields.String(required=False)
