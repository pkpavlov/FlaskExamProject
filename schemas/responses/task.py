from marshmallow import Schema,fields

from marshmallow_enum import EnumField

from models import TaskState


class TaskSchemaResponse(Schema):
    id = fields.Int(required=True)
    employee_id = fields.Int(required=True)
    task_name = fields.String(required=True)
    description = fields.String(required=True)
    created_on = fields.DateTime(required=True)
    finished_on = fields.DateTime(required=True)
    used_parts = fields.String(required=True)
    employee_comments = fields.String(required=True)
    state = EnumField(TaskState, by_value=True)

