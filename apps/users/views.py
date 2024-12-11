from rest_framework import generics, permissions
from rest_framework.viewsets import ReadOnlyModelViewSet
from .serializers import UserSerializer
from django.contrib.auth.models import User


class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    model = User
    serializer_class = UserSerializer
    permission_classes = (permissions.AllowAny,)


class UserViewSet(ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAdminUser, )
