from django.contrib import admin
from django.urls import include, path
from rest_framework_jwt.views import obtain_jwt_token

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("products.urls")),
    path("api-token-auth/", obtain_jwt_token),
]
