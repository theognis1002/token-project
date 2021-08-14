from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.response import Response
from rest_framework_jwt.settings import api_settings
from rest_framework_jwt.utils import jwt_payload_handler


class CreateTokenMixin:
    def post(self, request, *args, **kwargs):
        body = request.data
        try:
            user = User.objects.get(username=body["username"])
            if not user.check_password(body["password"]):
                return Response({"error": "User not found"})
        except (User.DoesNotExist, KeyError):
            return Response(
                {"error": "User does not exist"}, status=status.HTTP_401_UNAUTHORIZED
            )
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

        payload = jwt_payload_handler(user)
        payload["permissions"] = self.obj_permissions
        token = jwt_encode_handler(payload)
        return Response({"token": token})
