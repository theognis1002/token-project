from django.urls import include, path
from rest_framework.routers import DefaultRouter

from . import views

urlpatterns = [
    path("read/", views.ReadOnlyTokenView.as_view(), name="read_token"),
    path("manage/", views.WriteOnlyTokenView.as_view(), name="manage_token"),
    path("both/", views.ReadWriteTokenView.as_view(), name="rw_token"),
    path("admin/", views.AdminTokenView.as_view(), name="admin_token"),
]
