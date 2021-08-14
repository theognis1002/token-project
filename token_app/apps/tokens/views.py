from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from tokens.mixins import CreateTokenMixin


class ReadOnlyTokenView(CreateTokenMixin, APIView):
    permission_classes = (AllowAny,)
    obj_permissions = ("read_product",)


class WriteOnlyTokenView(CreateTokenMixin, APIView):
    permission_classes = (AllowAny,)
    obj_permissions = ("manage_product",)


class ReadWriteTokenView(CreateTokenMixin, APIView):
    permission_classes = (AllowAny,)
    obj_permissions = ("read_product", "manage_product")


class AdminTokenView(CreateTokenMixin, APIView):
    permission_classes = (AllowAny,)
    obj_permissions = ("admin",)


class TestView(APIView):
    def get(self, request, format=None):
        return Response({"data": []})
