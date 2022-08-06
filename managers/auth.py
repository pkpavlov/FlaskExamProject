from datetime import datetime, timedelta

import jwt
from jwt.exceptions import ExpiredSignatureError, InvalidTokenError
from decouple import config

from werkzeug.exceptions import BadRequest
from flask_httpauth import HTTPTokenAuth
from models import EmployeesModel


class AuthManager:
    @staticmethod
    def encode_token(user):
        payload = {"sub": user.id, "exp": datetime.utcnow() + timedelta(days=1)}
        return jwt.encode(payload, key=config("JWT_SECRET"), algorithm="HS256")

    @staticmethod
    def decode_token(token):
        try:
            payload = jwt.decode(token, key=config("JWT_SECRET"), algorithms=["HS256"])
            return payload["sub"]
        except ExpiredSignatureError:
            raise BadRequest("Token expired")
        except InvalidTokenError:
            raise BadRequest("Invalid token")


auth = HTTPTokenAuth()


@auth.verify_token
def verify(token):
    user_id = AuthManager.decode_token(token)
    return EmployeesModel.query.filter_by(id=user_id).first()
