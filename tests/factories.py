from random import randint
import random
import factory
from sqlalchemy import func

from db import db
from models import EmployeesModel, UserRole, StoreUsersModel, StoreModel, TaskModel, TaskState


class BaseFactory(factory.Factory):
    @classmethod
    def create(cls, **kwargs):
        object = super().create(**kwargs)
        db.session.add(object)
        db.session.flush()
        return object


class EmployeeFactory(BaseFactory):
    class Meta:
        model = EmployeesModel

    id = factory.Sequence(lambda x: x)
    first_name = factory.Faker("first_name")
    last_name = factory.Faker("last_name")
    password = factory.Faker("password")
    email = factory.Faker("email")
    phone = str(randint(100000, 200000))
    role = UserRole.employee
    iban = factory.Faker("iban")
    salary = str(850)
    vacation = str(randint(1, 20))
    create_on = func.now()

class AdminFactory(BaseFactory):
    class Meta:
        model = EmployeesModel

    id = factory.Sequence(lambda x: x)
    first_name = factory.Faker("first_name")
    last_name = factory.Faker("last_name")
    password = factory.Faker("password")
    email = factory.Faker("email")
    phone = str(randint(100000, 200000))
    role = UserRole.admin
    iban = factory.Faker("iban")
    salary = str(850)
    vacation = str(randint(1, 20))
    create_on = func.now()

class AccountantFactory(BaseFactory):
    class Meta:
        model = EmployeesModel

    id = factory.Sequence(lambda x: x)
    first_name = factory.Faker("first_name")
    last_name = factory.Faker("last_name")
    password = factory.Faker("password")
    email = factory.Faker("email")
    phone = str(randint(100000, 200000))
    role = UserRole.accountant
    iban = factory.Faker("iban")
    salary = str(850)
    vacation = str(randint(1, 20))
    create_on = func.now()

class WarehousemanFactory(BaseFactory):
    class Meta:
        model = EmployeesModel

    id = factory.Sequence(lambda x: x)
    first_name = factory.Faker("first_name")
    last_name = factory.Faker("last_name")
    password = factory.Faker("password")
    email = factory.Faker("email")
    phone = str(randint(100000, 200000))
    role = UserRole.warehouseman
    iban = factory.Faker("iban")
    salary = str(850)
    vacation = str(randint(1, 20))
    create_on = func.now()

class StoreUsersFactory(BaseFactory):
    class Meta:
        model = StoreUsersModel

    id = factory.Sequence(lambda x: x)
    first_name = factory.Faker("first_name")
    last_name = factory.Faker("last_name")
    password = factory.Faker("password")
    email = factory.Faker("email")
    phone = str(randint(100000, 200000))
    role = UserRole.store_user
    nickname = factory.Faker("nickname")
    address = factory.Faker("address")

class ItemsFactory(BaseFactory):
    class Meta:
        model = StoreModel

    id = factory.Sequence(lambda x: x)
    item_name = factory.Faker("name")
    serial_number = factory.Faker("name")
    quantity = str(randint(1, 1000))
    delivery_price = str(randint(1, 1000))
    sell_price = str(randint(1, 1000))
    dealer_price = str(randint(1, 1000))

class TasksFactory(BaseFactory):
    class Meta:
        model = TaskModel

    id = factory.Sequence(lambda x: x)
    task_name = factory.Faker("name")
    description = factory.Faker("name")
    create_on = func.now()
    updated_on = func.now()
    used_parts = factory.Faker("name")
    employee_comments = factory.Faker("name")
    state = random.choice(list(TaskState))
    employee_id = factory.Sequence(lambda x: x)
