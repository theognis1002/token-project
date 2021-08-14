from django.contrib.auth.models import User
from django.test import TestCase
from products import views
from products.models import Product
from products.serializers import AdminProductSerializer, ProductSerializer
from rest_framework import status
from rest_framework.test import APIRequestFactory, force_authenticate


class ProductTestCase(TestCase):
    def setUp(self):
        Product.objects.create(
            name="Blue Shirt", description="Made of cotton", qty=22, price=55.0
        )

    def test_product_str(self):
        product = Product.objects.get(name="Blue Shirt")
        self.assertEqual(str(product), "Blue Shirt")

    def test_product_fields(self):
        product = Product.objects.get(name="Blue Shirt")
        self.assertEqual(product.name, "Blue Shirt")
        self.assertEqual(product.qty, 22)
        self.assertEqual(product.description, "Made of cotton")
        self.assertEqual(product.price, 55.0)


class ProductSerializersTestCase(TestCase):
    def setUp(self):
        self.product_attrs = {"name": "Nike sneakers", "qty": 5, "price": 125.0}

        self.serializer_data = {"name": "Puma sneakers", "qty": 2, "price": 65.0}

        self.product = Product.objects.create(**self.product_attrs)
        self.serializer = ProductSerializer(instance=self.product)
        self.admin_serializer = AdminProductSerializer(instance=self.product)

    def test_pub_serializer_contains_expected_fields(self):
        data = self.serializer.data

        self.assertEqual(
            set(data.keys()),
            set(
                [
                    "id",
                    "qty",
                    "date_added",
                    "description",
                    "price",
                    "name",
                ]
            ),
        )

    def test_admin_serializer_contains_expected_fields(self):
        data = self.admin_serializer.data

        self.assertEqual(
            set(data.keys()),
            set(
                [
                    "id",
                    "soft_delete",
                    "qty",
                    "date_added",
                    "description",
                    "price",
                    "name",
                ]
            ),
        )


class ProductEndpointsTestCase(TestCase):
    factory = APIRequestFactory()

    def setUp(self):
        self.factory = APIRequestFactory()
        self.admin = User.objects.create(username="admin")
        Product.objects.create(
            name="Blue Shirt", description="Made of cotton", qty=22, price=55.0
        )
        Product.objects.create(
            name="Red Shirt", description="Made of polyester", qty=1, price=25.0
        )

    def test_get_all_products(self):
        view = views.ProductList.as_view()
        request = self.factory.get("/products/")
        force_authenticate(request, user=self.admin)
        response = view(request)

        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_product(self):
        view = views.ProductList.as_view()
        request = self.factory.get("/products/1/")
        force_authenticate(request, user=self.admin)
        response = view(request)

        products = Product.objects.get(pk=1)
        serializer = ProductSerializer(products, many=False)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
