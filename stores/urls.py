from rest_framework.routers import DefaultRouter
from django.urls import path, include
from . import views
from .views import StoresViewSet, UsersViewSet

app_name = "stores"

router = DefaultRouter()
router.register(r"owners", views.UsersViewSet, basename="users")
router.register(r"stores", views.StoresViewSet, basename="stores")

urlpatterns = [
    path("", include(router.urls)),
]