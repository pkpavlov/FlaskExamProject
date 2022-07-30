from flask import request
from werkzeug.exceptions import BadRequest, Forbidden
from managers.auth import auth


def validate_schema(schema_name):
    def decorated_function(func):
        def wrapper(*args, **kwargs):
            data = request.get_json()
            schema = schema_name()
            errors = schema.validate(data)
            if not errors:
                return func(*args, **kwargs)
            raise BadRequest(errors)

        return wrapper

    return decorated_function


def permission_required(*role):
    def decorated_function(func):
        def wrapper(*args, **kwargs):
            current_user = auth.current_user()
            for r in role:
                if current_user.role == r:
                    return func(*args, **kwargs)
            raise Forbidden("Permission denied!")

        return wrapper
    return decorated_function
