from werkzeug.exceptions import BadRequest
from werkzeug.security import generate_password_hash, check_password_hash
from models.user import StoreUsersModel
from db import db
from managers.auth import AuthManager


class StoreUserManager:

    @staticmethod
    def register(store_user_data):
        store_user_data["password"] = generate_password_hash(store_user_data["password"])
        user = StoreUsersModel(**store_user_data)
        db.session.add(user)
        db.session.commit()
        return AuthManager.encode_token(user)

    @staticmethod
    def login(login_data):
        employee = StoreUsersModel.query.filter_by(email=login_data["email"]).first()
        if not employee:
            raise BadRequest("No such user with this E-mail!")
        if check_password_hash(employee.password, login_data["password"]):
            return AuthManager.encode_token(employee)
        raise BadRequest("Wrong password!")