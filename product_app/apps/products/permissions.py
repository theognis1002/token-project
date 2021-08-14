import jwt
from django.conf import settings
from rest_framework import permissions


class CustomPermission(permissions.BasePermission):

    cud_operations = ("POST", "PUT", "PATCH", "DELETE")

    def has_object_permission(self, request, view, obj):
        auth_header = request.META.get("HTTP_AUTHORIZATION")
        access_token = auth_header.split(" ")[-1] if auth_header else None
        decoded_jwt = jwt.decode(
            str(access_token), settings.SECRET_KEY, algorithms=["HS256"]
        )
        user_permissions = decoded_jwt.get("permissions", [])

        if "admin" in user_permissions:
            return True

        if request.method == "GET" and "read_product" in user_permissions:
            return True

        if (
            request.method in self.cud_operations
            and "manage_product" in user_permissions
        ):
            return True

        return False
