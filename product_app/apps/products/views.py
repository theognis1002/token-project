from products.models import Product
from products.serializers import AdminProductSerializer, ProductSerializer
from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from .permissions import CustomPermission


class ProductModelViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.active_only()  # hides soft deleted products
    serializer_class = ProductSerializer
    permission_classes = (CustomPermission,)

    def destroy(self, request, *args, **kwargs):
        """overriding default destroy - soft delete method"""
        instance = self.get_object()
        instance.soft_delete = True
        instance.save()
        return Response(status=status.HTTP_204_NO_CONTENT)


class AdminProductList(APIView):
    permission_classes = (CustomPermission,)

    def get(self, request, format=None):
        products = Product.objects.all()  # shows all products including soft deleted
        serializer = AdminProductSerializer(products, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = AdminProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
