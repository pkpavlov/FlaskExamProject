from flask_testing import TestCase

from config import create_app
from db import db
from tests.factories import EmployeeFactory
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
