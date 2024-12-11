from rest_framework.routers import DefaultRouter
from .views import UserViewSet, CreateUserView
from django.urls import path, include

router = DefaultRouter()

router.register(r'users_list', UserViewSet, basename='users')

urlpatterns = [
    path('', include(router.urls)),
    path('users/register/', CreateUserView.as_view(), name='register'),
]

