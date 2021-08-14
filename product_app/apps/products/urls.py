from django.urls import include, path
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register(r"products/?", views.ProductModelViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path(
        "products-admin/", views.AdminProductList.as_view(), name="admin_product_list"
    ),
]
