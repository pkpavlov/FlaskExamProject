from flask_restful import Resource
from flask import request

from managers.employee import EmployeeManager
from managers.store import StoreManager
from managers.store_user import StoreUserManager
from managers.task import TaskManager
from schemas.requests.auth import RegisterEmployeeSchemaRequest, RegisterShopUserSchemaRequest, \
    RegisterItemSchemaRequest, RegisterTaskSchemaRequest, LoginSchemaRequest
from utils.decorators import validate_schema, permission_required
from managers.auth import auth
from models import UserRole


class RegisterEmployeeResource(Resource):
    @auth.login_required
    @permission_required(UserRole.admin)
    @validate_schema(RegisterEmployeeSchemaRequest)
    def post(self):
        data = request.get_json()
        token = EmployeeManager.register(data)

        return {"token": token}, 201


class RegisterStoreUserResource(Resource):

    @validate_schema(RegisterShopUserSchemaRequest)
    def post(self):
        data = request.get_json()
        token = StoreUserManager.register(data)

        return {"token": token}, 201


class RegisterTaskResource(Resource):
    @auth.login_required
    @permission_required(UserRole.admin)
    @validate_schema(RegisterTaskSchemaRequest)
    def post(self):
        data = request.get_json()
        task = TaskManager.register(data)
        return f"Task {task.task_name} number {task.id} assigned to {task.employee.first_name} {task.employee.last_name}"


class RegisterItemResource(Resource):
    @auth.login_required
    @permission_required(UserRole.warehouseman, UserRole.admin)
    @validate_schema(RegisterItemSchemaRequest)
    def post(self):
        data = request.get_json()
        item = StoreManager.register(data)
        return f"added item {item.item_name} with quantity {item.quantity}"

class LoginEmployeeResource(Resource):

    def post(self):
        data = request.get_json()
        token = EmployeeManager.login(data)

        return {"token": token}, 200


class LoginStoreUserResource(Resource):

    def post(self):
        data = request.get_json()
        token = StoreUserManager.login(data)

        return {"token": token}, 200
