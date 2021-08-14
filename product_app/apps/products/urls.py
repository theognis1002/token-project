from django.urls import include, path
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter(trailing_slash=False)
router.register(r"products/?", views.ProductModelViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
