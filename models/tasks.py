from sqlalchemy import func

from db import db
from models.enums import TaskState


class TaskModel(db.Model):
    __tablename__ = "task"

    id = db.Column(db.Integer, primary_key=True)
    task_name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(255), nullable=False)
    created_on = db.Column(db.DateTime, server_default=func.now(), nullable=False)
    finished_on = db.Column(db.DateTime, onupdate=func.now(), nullable=False)
    used_parts = db.Column(db.String(255), default="Not used", nullable=False)
    employee_comments = db.Column(db.String(255), default="Add comment:", nullable=False)
    state = db.Column(db.Enum(TaskState), default=TaskState.in_progress, nullable=False)
    employee_id = db.Column(db.Integer, db.ForeignKey("employees.id"), nullable=False)
    employee = db.relationship("EmployeesModel")
