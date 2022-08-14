from random import randint

import factory
from sqlalchemy import func

from db import db
from models import EmployeesModel, UserRole


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
    salary = str(randint(100000, 200000))
    vacation = str(randint(1, 20))
    create_on = func.now()
