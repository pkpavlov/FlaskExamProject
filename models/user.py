from sqlalchemy import func

from db import db
from models.enums import UserRole


class BaseUserModel(db.Model):
    __abstract__ = True

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(20), nullable=False)
    last_name = db.Column(db.String(20), nullable=False)
    password = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(60), nullable=False, unique=True)
    phone = db.Column(db.String(14), nullable=False)


class EmployeesModel(BaseUserModel):
    __tablename__ = "employees"

    role = db.Column(db.Enum(UserRole), default=UserRole.employee, nullable=False)
    iban = db.Column(db.String(50), default="empty", nullable=False)
    salary = db.Column(db.Float, default=850, nullable=False)
    vacation = db.Column(db.Integer, default=21, nullable=False)
    create_on = db.Column(db.DateTime(), server_default=func.now())
    task = db.relationship("TaskModel", backref="task", lazy="dynamic")


class StoreUsersModel(BaseUserModel):
    __tablename__ = "StoreUser"

    role = db.Column(db.Enum(UserRole), default=UserRole.store_user, nullable=False)
    nickname = db.Column(db.String(20), nullable=False)
    address = db.Column(db.String(100), nullable=False)
