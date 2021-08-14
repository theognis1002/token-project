from products.models import Product
from products.serializers import ProductSerializer
from rest_framework import status, viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView


class ProductList(APIView):
    """
    List all Products, or create a new Product.
    """

    def get(self, request, format=None):
        products = Product.objects.active_only()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductModelViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.active_only()
    serializer_class = ProductSerializer
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAdminUser]
