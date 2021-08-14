from django.urls import include, path
from rest_framework.routers import DefaultRouter

from . import views

# router = DefaultRouter(trailing_slash=False)
# router.register(r"products/?", views.TokenModelViewSet)

urlpatterns = [
    # path("", views.TokenView.as_view(), name="get_token"),
    path("test/", views.TestView.as_view(), name="test_view"),
    path("read/", views.ReadOnlyTokenView.as_view(), name="read_token"),
    path("manage/", views.WriteOnlyTokenView.as_view(), name="manage_token"),
    path("both/", views.ReadWriteTokenView.as_view(), name="rw_token"),
    path("admin/", views.AdminTokenView.as_view(), name="admin_token"),
]
