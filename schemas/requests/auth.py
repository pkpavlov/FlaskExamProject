from marshmallow import Schema, fields, validate
from marshmallow_enum import EnumField
from sqlalchemy import func

from models import TaskState
from schemas.requests.base import BaseRequestUserSchema, BaseRequestSchema




class RegisterEmployeeSchemaRequest(BaseRequestUserSchema):

    iban = fields.String(required=False, validate=validate.Length(min=15, max=32))
    salary = fields.Integer(required=False)
    vacation = fields.Integer(required=False)


class RegisterShopUserSchemaRequest(BaseRequestUserSchema):

    nickname = fields.String(required=True, validate=validate.Length(min=2, max=20))
    address = fields.String(required=True, validate=validate.Length(min=8, max=20))


class RegisterItemSchemaRequest(Schema):
    item_name = fields.String(required=True, validate=validate.Length(min=1, max=20))
    serial_number = fields.String(
        required=True, validate=validate.Length(min=5, max=20)
    )
    quantity = fields.Integer(required=False)
    delivery_price = fields.Float(required=True)
    sell_price = fields.Float(required=False)
    dealer_price = fields.Float(required=False)


class DeleteItemSchemaRequest(Schema):
    id = fields.Integer(required=True)


class RegisterTaskSchemaRequest(Schema):
    task_name = fields.String(required=True, validate=validate.Length(min=5, max=20))
    description = fields.String(required=True, validate=validate.Length(min=5, max=255))
    used_parts = fields.String(required=False)
    employee_comments = fields.String(
        required=False, validate=validate.Length(min=5, max=255)
    )
    state = fields.String(required=False)
    employee_id = fields.Integer(required=True)
    create_on = fields.DateTime()
    updated_on = fields.DateTime()


class UpdateTaskSchemaRequest(Schema):
    id = fields.Integer(required=True)
    used_parts = fields.String(required=True)
    employee_comments = fields.String(
        required=True, validate=validate.Length(min=5, max=255)
    )
    state = EnumField(TaskState)

class DeleteTaskSchemaRequest(Schema):
    id = fields.Integer(required=True)


class LoginSchemaRequest(BaseRequestSchema):
    email = fields.Email(required=True)
    password = fields.String(required=True, validate=validate.Length(min=8, max=20))



