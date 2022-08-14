import uuid

from werkzeug.exceptions import BadRequest
from werkzeug.security import generate_password_hash, check_password_hash

from models import TransactionModel
from models.user import EmployeesModel
from db import db
from managers.auth import AuthManager
from services.wise import WiseService

wise = WiseService()




class EmployeeManager:

    @staticmethod
    def get_employee_info(employee_id):
        employee = EmployeesModel.query.filter_by(id=employee_id).first()
        employee_id = employee.id
        salary = employee.salary
        iban = employee.iban
        full_name = f"{employee.first_name} {employee.last_name}"

        return salary, full_name, iban, employee_id

    @staticmethod
    def register(employee_data):
        employee_data["password"] = generate_password_hash(employee_data["password"])
        user = EmployeesModel(**employee_data)
        db.session.add(user)
        db.session.commit()
        return AuthManager.encode_token(user)

    @staticmethod
    def login(login_data):
        employee = EmployeesModel.query.filter_by(email=login_data["email"]).first()
        if not employee:
            raise BadRequest("No such user with this E-mail!")
        if check_password_hash(employee.password, login_data["password"]):
            return AuthManager.encode_token(employee)
        raise BadRequest("Wrong password!")

    @staticmethod
    def issue_transaction(amount,full_name, iban, employee_id):
        quote_id = wise.create_quotes("EUR", "EUR", amount)
        recipient_id = wise.create_recipient(full_name, iban)
        customer_transaction_id = str(uuid.uuid4())
        transfer_id = wise.create_transfer(recipient_id, quote_id, customer_transaction_id)
        data = {
                    "quote_id": quote_id,
            "recipient_id": recipient_id,
            "transfer_di": transfer_id,
            "target_account_id": customer_transaction_id,
            "amount": amount,
            "employee_id": employee_id,
        }
        transaction = TransactionModel(**data)
        db.session.add(transaction)
        db.session.commit()

    @staticmethod
    def salary_update(employee_data):
        EmployeesModel.query.filter_by(id=employee_data["id"]).update({"salary": employee_data["salary"]})
        db.session.commit()
