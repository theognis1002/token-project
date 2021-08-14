from django.contrib.auth.models import User
from django.test import TestCase
from products import views
from rest_framework import status
from rest_framework.test import APIRequestFactory, force_authenticate


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
        self.assertEqual(1, 1)

    # def test_get_product(self):
    #     view = views.ProductList.as_view()
    #     request = self.factory.get("/products/1/")
    #     force_authenticate(request, user=self.admin)
    #     response = view(request)

    #     products = Product.objects.get(pk=1)
    #     serializer = ProductSerializer(products, many=False)
    #     self.assertEqual(response.data, serializer.data)
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
