from unittest.mock import patch

from flask_testing import TestCase

from config import create_app
from db import db
from managers.employee import EmployeeManager

from tests.factories import EmployeeFactory, TasksFactory, ItemsFactory, AdminFactory, AccountantFactory
from tests.helpers import generate_token


class TestApp(TestCase):
    def create_app(self):
        return create_app("config.TestConfig")

    def setUp(self):
        db.init_app(self.app)
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_login_required(self):

        resp = None
        for method, url in [
            ("POST", "/register-employees/"),
            ("POST", "/tasks/"),
            ("GET", "/tasks/"),
            ("POST", "/tasks/"),
            ("PUT", "/task/1/"),
            ("DELETE", "/task/1/"),
            ("POST", "/items/"),
            ("DELETE", "item/1/"),
            ("POST", "/salary/1/payment/"),
            ("PUT", "/salary/1/update/"),
        ]:

            if method == "POST":
                resp = self.client.post(url)
            elif method == "GET":
                resp = self.client.get(url)
            elif method == "PUT":
                resp = self.client.put(url)
            else:
                resp = self.client.delete(url)

            self.assert_401(resp)
            self.assertEqual(resp.json, {"message": "Missing token"})

    def test_invalid_token(self):
        headers = {"Authorization": "Bearer rp8huedo2ALH_Hp6yDxfK0F6SA6Rr3duf9kpoSyRs"}
        resp = None
        for method, url in [
            ("POST", "/register-employees/"),
            ("POST", "/tasks/"),
            ("GET", "/tasks/"),
            ("POST", "/tasks/"),
            ("PUT", "/task/1/"),
            ("DELETE", "/task/1/"),
            ("POST", "/items/"),
            ("DELETE", "item/1/"),
            ("POST", "/salary/1/payment/"),
            ("PUT", "/salary/1/update/"),
        ]:

            if method == "POST":
                resp = self.client.post(url, headers=headers)
            elif method == "GET":
                resp = self.client.get(url, headers=headers)
            elif method == "PUT":
                resp = self.client.put(url, headers=headers)
            else:
                resp = self.client.delete(url, headers=headers)

            self.assert_401(resp)
            self.assertEqual(resp.json, {"message": "Invalid token"})

    def test_missing_permissions_employees(self):
        user = EmployeeFactory()
        token = generate_token(user)

        headers = {"Authorization": f"Bearer {token}"}
        resp = None
        for method, url in [
            ("POST", "/register-employees/"),
            ("POST", "/tasks/"),
            ("POST", "/tasks/"),
            ("DELETE", "/task/1/"),
            ("POST", "/items/"),
            ("DELETE", "item/1/"),
            ("POST", "/salary/1/payment/"),
            ("PUT", "/salary/1/update/"),
        ]:

            if method == "POST":
                resp = self.client.post(url, headers=headers)
            elif method == "GET":
                resp = self.client.get(url, headers=headers)
            elif method == "PUT":
                resp = self.client.put(url, headers=headers)
            else:
                resp = self.client.delete(url, headers=headers)

            self.assert_403(resp)
            self.assertEqual(resp.json, {"message": "Permission denied!"})


    def test_missing_permissions_account(self):
        user = EmployeeFactory()
        token = generate_token(user)

        headers = {"Authorization": f"Bearer {token}"}
        resp = None
        for method, url in [
            ("POST", "/register-employees/"),
            ("POST", "/tasks/"),
            ("DELETE", "/task/1/"),
            ("POST", "/items/"),
            ("DELETE", "item/1/"),

        ]:

            if method == "POST":
                resp = self.client.post(url, headers=headers)
            elif method == "GET":
                resp = self.client.get(url, headers=headers)
            elif method == "PUT":
                resp = self.client.put(url, headers=headers)
            else:
                resp = self.client.delete(url, headers=headers)

            self.assert_403(resp)
            self.assertEqual(resp.json, {"message": "Permission denied!"})

    def test_missing_permissions_warehouseman(self):
        user = EmployeeFactory()
        token = generate_token(user)

        headers = {"Authorization": f"Bearer {token}"}
        resp = None
        for method, url in [
            ("POST", "/register-employees/"),
            ("POST", "/tasks/"),
            ("POST", "/tasks/"),
            ("DELETE", "/task/1/"),
            ("POST", "/items/"),
            ("DELETE", "item/1/"),
            ("POST", "/salary/1/payment/"),
            ("PUT", "/salary/1/update/"),

        ]:

            if method == "POST":
                resp = self.client.post(url, headers=headers)
            elif method == "GET":
                resp = self.client.get(url, headers=headers)
            elif method == "PUT":
                resp = self.client.put(url, headers=headers)
            else:
                resp = self.client.delete(url, headers=headers)

            self.assert_403(resp)
            self.assertEqual(resp.json, {"message": "Permission denied!"})

    @patch.object(EmployeeManager, "issue_transaction", return_value={
        "quote_id": "12-25",
        "recipient_id": "23",
        "transfer_di": "23",
        "target_account_id": "152",
        "amount": 850,
        "employee_id": "0",
    })
    def test_payment_success(self, moke_wise):
        url = "/salary/1/payment/"
        user = AccountantFactory()
        token = generate_token(user)
        headers = {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}
        data = {"id": f"{user.id}" }
        resp = self.client.post(url, headers=headers, json=data)
        self.assert_200(resp)