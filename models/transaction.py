from sqlalchemy import func

from db import db


class TransactionModel(db.Model):

    __tablename__ = "transactions"
    id = db.Column(db.Integer, primary_key=True)
    quote_id = db.Column(db.String(255), nullable=False)
    recipient_id = db.Column(db.String(255), nullable=False)
    transfer_di = db.Column(db.String(255), nullable=False)
    target_account_id = db.Column(db.String(100), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    employee_id = db.Column(db.ForeignKey("employees.id"), nullable=False)
    employee = db.relationship("EmployeesModel")
    created_on = db.Column(db.DateTime, server_default=func.now())
