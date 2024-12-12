from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
    CreateAPIView,
    ListAPIView,
    DestroyAPIView,
)
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from django_filters import rest_framework as filters

from .serializers import LibraryModelSerializer, FavoriteModelSerializer, LibraryRatingModelSerializer
from .models import LibraryModel, FavoriteBookModel, BookRatingModel
from .library_pagination import CustomLibraryPagination
from .filters import LibraryFilter
from .permissions import IsOwnerOrReadOnly


class LibraryListCreateAPIView(ListCreateAPIView):
    queryset = LibraryModel.objects.all()
    serializer_class = LibraryModelSerializer
    permission_classes = [IsAuthenticated, ]
    pagination_class = CustomLibraryPagination
    filter_backends = [filters.DjangoFilterBackend]
    filterset_class = LibraryFilter

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)


class LibraryRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = LibraryModel.objects.all()
    serializer_class = LibraryModelSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly, IsAdminUser]


class LibraryRatingCreateListAPIView(ListCreateAPIView):
    queryset = BookRatingModel.objects.all()
    serializer_class = LibraryRatingModelSerializer
    permission_classes = [IsAuthenticated, ]


class CreateFavoriteAPIView(CreateAPIView):
    queryset = FavoriteBookModel.objects.all()
    serializer_class = FavoriteModelSerializer
    permission_classes = [IsAuthenticated, ]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class ListFavoriteAPIView(ListAPIView):
    queryset = FavoriteBookModel.objects.all()
    serializer_class = FavoriteModelSerializer
    permission_classes = [IsAuthenticated, ]

    def get_queryset(self):
        return FavoriteBookModel.objects.filter(user=self.request.user)


class RemoveFavoriteAPIView(DestroyAPIView):
    queryset = FavoriteBookModel.objects.all()
    serializer_class = FavoriteModelSerializer
    permission_classes = [IsAuthenticated, ]

    def perform_destroy(self, instance):
        return FavoriteBookModel.objects.filter(user=self.request.user, id=instance.id).delete()
