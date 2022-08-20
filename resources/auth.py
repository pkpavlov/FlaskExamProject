from flask_restful import Resource
from flask import request

from managers.employee import EmployeeManager
from managers.store import StoreManager
from managers.store_user import StoreUserManager
from managers.task import TaskManager
from schemas.requests.auth import (
    RegisterEmployeeSchemaRequest,
    RegisterShopUserSchemaRequest,
    RegisterItemSchemaRequest,
    RegisterTaskSchemaRequest,
    LoginSchemaRequest,
    UpdateTaskSchemaRequest,
    DeleteItemSchemaRequest,
    DeleteTaskSchemaRequest,
    BuyItemsSchemaRequest,
)
from schemas.responses.task import TaskSchemaResponse, ItemsSchemaResponse
from utils.decorators import validate_schema, permission_required
from managers.auth import auth
from models import UserRole, TaskModel, StoreModel, EmployeesModel


def _validate_id(id, model):
    task = model.query.filter_by(id=id).first()
    if not task:
        return False
    return True


class RegisterEmployeeResource(Resource):
    @auth.login_required
    @permission_required(UserRole.admin)
    @validate_schema(RegisterEmployeeSchemaRequest)
    def post(self):
        data = request.get_json()
        token = EmployeeManager.register(data)
        a = 5
        return {"token": token}, 201


class RegisterStoreUserResource(Resource):
    @validate_schema(RegisterShopUserSchemaRequest)
    def post(self):
        data = request.get_json()
        token = StoreUserManager.register(data)

        return {"token": token}, 201


class TasksResource(Resource):

    @auth.login_required
    def get(self):
        user = auth.current_user()
        tasks = TaskManager.get_task(user)
        return TaskSchemaResponse().dump(tasks, many=True)

    @auth.login_required
    @permission_required(UserRole.admin)
    @validate_schema(RegisterTaskSchemaRequest)
    def post(self):
        data = request.get_json()
        task = TaskManager.register(data)
        return f"Task {task.task_name} number {task.id} assigned to {task.employee.first_name} {task.employee.last_name}"


class TaskStatusEditResource(Resource):
    @auth.login_required
    @permission_required(UserRole.admin, UserRole.employee)
    @validate_schema(UpdateTaskSchemaRequest)
    def put(self, id):
        data = request.get_json()
        if _validate_id(data["id"], TaskModel()):
            task = TaskManager.task_update(data)
            return 204
        return 404


class TaskDeleteResource(Resource):
    @auth.login_required
    @permission_required(UserRole.admin)
    @validate_schema(DeleteTaskSchemaRequest)
    def delete(self, id):
        data = request.get_json()
        if _validate_id(data["id"], TaskModel()):
            task = TaskManager.delete(data)
            return 204
        return 404


class ItemsResource(Resource):
    @auth.login_required
    @permission_required(UserRole.warehouseman, UserRole.admin)
    @validate_schema(RegisterItemSchemaRequest)
    def post(self):
        data = request.get_json()
        item = StoreManager.register(data)
        return f"added item {item.item_name} with quantity {item.quantity}"

    @auth.login_required
    def get(self):

        items = StoreManager.get_items()
        return ItemsSchemaResponse().dump(items, many=True)


class DeleteItemsResource(Resource):
    @auth.login_required
    @permission_required(UserRole.warehouseman, UserRole.admin)
    @validate_schema(DeleteItemSchemaRequest)
    def delete(self, id):
        data = request.get_json()
        if _validate_id(data["id"], StoreModel()):
            task = StoreManager.delete(data)
            return 204
        return 404


class LoginEmployeeResource(Resource):
    @validate_schema(LoginSchemaRequest)
    def post(self):
        data = request.get_json()
        token = EmployeeManager.login(data)

        return {"token": token}, 200


class LoginStoreUserResource(Resource):
    @validate_schema(LoginSchemaRequest)
    def post(self):
        data = request.get_json()
        token = StoreUserManager.login(data)

        return {"token": token}, 200


class BuyStoreItemResource(Resource):
    @validate_schema(BuyItemsSchemaRequest)
    def post(self):
        data = request.get_json()
        item = StoreManager.buy(data["id"], data["quantity"])
        return item


class SalaryPaymentResource(Resource):
    @auth.login_required
    @permission_required(UserRole.accountant)
    def post(self, id):
        data = request.get_json()
        if _validate_id(data["id"], EmployeesModel()):
            data = EmployeeManager.get_employee_info(data["id"])
            EmployeeManager.issue_transaction(data[0], data[1], data[2], data[3])
            return 200
        return 404


class SalaryUpdateResource(Resource):
    @auth.login_required
    @permission_required(UserRole.accountant)
    def put(self, id):
        data = request.get_json()
        if _validate_id(data["id"], EmployeesModel()):
            employee = EmployeeManager.salary_update(data)
            return 200
        return 404
