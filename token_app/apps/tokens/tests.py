import jwt
from django.conf import settings
from django.contrib.auth.models import User
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIRequestFactory, force_authenticate
from tokens import views


class TokenEndpointsTestCase(TestCase):
    factory = APIRequestFactory()

    def setUp(self):
        self.factory = APIRequestFactory()
        test_user = User.objects.create(username="admin", password="")
        test_user.set_password("admin")
        test_user.save()
        self.admin = test_user

    def test_read_only_token_gen(self):
        view = views.ReadOnlyTokenView.as_view()
        request = self.factory.post(
            "/tokens/read/", {"username": "admin", "password": "admin"}
        )
        response = view(request)
        print(response.data)
        self.assertEqual(list(response.data.keys()), ["token"])

    def test_write_only_token_gen(self):
        view = views.WriteOnlyTokenView.as_view()
        request = self.factory.post(
            "/tokens/manage/", {"username": "admin", "password": "admin"}
        )
        response = view(request)
        self.assertEqual(list(response.data.keys()), ["token"])

    def test_read_write_token_gen(self):
        view = views.ReadWriteTokenView.as_view()
        request = self.factory.post(
            "/tokens/both/", {"username": "admin", "password": "admin"}
        )
        response = view(request)
        self.assertEqual(list(response.data.keys()), ["token"])

    def test_admin_token_gen(self):
        view = views.AdminTokenView.as_view()
        request = self.factory.post(
            "/tokens/admin/", {"username": "admin", "password": "admin"}
        )
        response = view(request)
        self.assertEqual(list(response.data.keys()), ["token"])


class TokenPermissionTestCase(TestCase):
    factory = APIRequestFactory()

    def setUp(self):
        self.factory = APIRequestFactory()
        test_user = User.objects.create(username="admin", password="")
        test_user.set_password("admin")
        test_user.save()
        self.admin = test_user

    def test_read_only_permissions(self):
        view = views.ReadOnlyTokenView.as_view()
        request = self.factory.post(
            "/tokens/read/", {"username": "admin", "password": "admin"}
        )
        response = view(request)
        token = response.data["token"]
        decoded_jwt = jwt.decode(str(token), settings.SECRET_KEY, algorithms=["HS256"])
        user_permissions = decoded_jwt["permissions"]
        self.assertEqual(user_permissions, ["read_product"])

    def test_write_only_permissions(self):
        view = views.WriteOnlyTokenView.as_view()
        request = self.factory.post(
            "/tokens/manage/", {"username": "admin", "password": "admin"}
        )
        response = view(request)
        token = response.data["token"]
        decoded_jwt = jwt.decode(str(token), settings.SECRET_KEY, algorithms=["HS256"])
        user_permissions = decoded_jwt["permissions"]
        self.assertEqual(user_permissions, ["manage_product"])

    def test_read_write_permissions(self):
        view = views.ReadWriteTokenView.as_view()
        request = self.factory.post(
            "/tokens/both/", {"username": "admin", "password": "admin"}
        )
        response = view(request)
        token = response.data["token"]
        decoded_jwt = jwt.decode(str(token), settings.SECRET_KEY, algorithms=["HS256"])
        user_permissions = decoded_jwt["permissions"]
        self.assertEqual(user_permissions, ["read_product", "manage_product"])

    def test_admin_permissions(self):
        view = views.AdminTokenView.as_view()
        request = self.factory.post(
            "/tokens/admin/", {"username": "admin", "password": "admin"}
        )
        response = view(request)
        token = response.data["token"]
        decoded_jwt = jwt.decode(str(token), settings.SECRET_KEY, algorithms=["HS256"])
        user_permissions = decoded_jwt["permissions"]
        self.assertEqual(user_permissions, ["admin"])
