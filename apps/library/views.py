from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
    CreateAPIView,
    ListAPIView,
    DestroyAPIView,
    RetrieveAPIView

)
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from django_filters import rest_framework as filters

from .serializers import LibraryModelSerializer, FavoriteModelSerializer, LibraryRatingModelSerializer
from .models import LibraryModel, FavoriteBookModel, BookRatingModel
from .library_pagination import CustomLibraryPagination
from .filters import LibraryFilter
from .permissions import IsOwnerOrReadOnly
from .tasks import book_creation


class LibraryListCreateAPIView(ListCreateAPIView):
    """
    API view for listing and creating library records.

    This view provides the following functionalities:
    - **List library records**: Retrieve a paginated list of books with optional filtering.
    - **Create a library record**: Allow authenticated users to add new books to the library.

    Key configurations:
    - **Queryset**: Fetches all objects from the `LibraryModel`.
    - **Serializer**: Uses `LibraryModelSerializer` for serialization/deserialization.
    - **Permissions**: Only authenticated users can access this view (`IsAuthenticated` permission).
    - **Pagination**: Uses custom pagination defined in `CustomLibraryPagination`.
    - **Filtering**: Supports filtering based on the fields defined in `LibraryFilter` via `DjangoFilterBackend`.

    Overridden methods:
    - `perform_create`: Sets the `creator` field of the newly created record to the current authenticated user.

    """
    queryset = LibraryModel.objects.all()
    serializer_class = LibraryModelSerializer
    permission_classes = [IsAuthenticated, ]
    pagination_class = CustomLibraryPagination
    filter_backends = [filters.DjangoFilterBackend]
    filterset_class = LibraryFilter

    def perform_create(self, serializer):
        book = serializer.save(creator=self.request.user)
        book_creation.delay(book.id, self.request.user.id)


class LibraryRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    """
    API view for retrieving, updating, and deleting a library record.

    This view provides the following functionalities:
    - **Retrieve**: Fetch detailed information about a specific library record.
    - **Update**: Modify an existing library record (allowed for owners or admins).
    - **Delete**: Remove a library record (allowed for owners or admins).

    Key configurations:
    - **Queryset**: Fetches all objects from the `LibraryModel`.
    - **Serializer**: Uses `LibraryModelSerializer` for serialization/deserialization.
    - **Permissions**:
        - Authenticated users can access this view.
        - Ownership-based permissions are enforced (`IsOwnerOrReadOnly`).
        - Admin users have full access.

    """
    queryset = LibraryModel.objects.all()
    serializer_class = LibraryModelSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly, IsAdminUser]


class BookRatingCreateAPIView(CreateAPIView):
    """
    API view for creating a book rating.

    This view allows authenticated users to add a rating for a specific book.

    Key configurations:
    - **Queryset**: Fetches all objects from the `BookRatingModel`.
    - **Serializer**: Uses `LibraryRatingModelSerializer` for validation and serialization.
    - **Permissions**: Only authenticated users can access this view.

    """
    queryset = BookRatingModel.objects.all()
    serializer_class = LibraryRatingModelSerializer
    permission_classes = [IsAuthenticated, ]


class BookRatingRetrieveAPIView(RetrieveAPIView):
    """
    API view for retrieving a book rating.

    This view allows authenticated users to fetch detailed information
    about a specific rating they have created or other ratings (if allowed).

    Key configurations:
    - **Queryset**: Fetches all objects from the `BookRatingModel`.
    - **Serializer**: Uses `LibraryRatingModelSerializer` for serialization/deserialization.
    - **Permissions**: Only authenticated users can access this view.

    """
    queryset = BookRatingModel.objects.all()
    serializer_class = LibraryRatingModelSerializer
    permission_classes = [IsAuthenticated, ]


class BookRatingRemoveAPIView(DestroyAPIView):
    """
    API view for removing a book rating.

    This view allows authenticated users to delete their own book rating.

    Key configurations:
    - **Queryset**: Fetches all objects from the `BookRatingModel`.
    - **Serializer**: Uses `LibraryRatingModelSerializer` for serialization/deserialization.
    - **Permissions**: Only authenticated users can delete their ratings.
    - **Custom behavior**:
        - Ensures that only the current user's rating is deleted via `perform_destroy`.

    """
    queryset = BookRatingModel.objects.all()
    serializer_class = LibraryRatingModelSerializer
    permission_classes = [IsAuthenticated,]

    def perform_destroy(self, instance):
        return BookRatingModel.objects.filter(user=self.request.user, id=instance.id).delete()


class CreateFavoriteAPIView(CreateAPIView):
    """
    API view for adding a book to favorites.

    This view allows authenticated users to mark a book as their favorite.

    Key configurations:
    - **Queryset**: Fetches all objects from the `FavoriteBookModel`.
    - **Serializer**: Uses `FavoriteModelSerializer` for validation and serialization.
    - **Permissions**: Only authenticated users can access this view.
    - **Custom behavior**:
        - Automatically associates the favorite book with the current user.

    """
    queryset = FavoriteBookModel.objects.all()
    serializer_class = FavoriteModelSerializer
    permission_classes = [IsAuthenticated, ]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class ListFavoriteAPIView(ListAPIView):
    """
    API view for listing favorite books.

    This view allows authenticated users to retrieve a list of their favorite books.

    Key configurations:
    - **Queryset**: Fetches all objects from the `FavoriteBookModel`.
    - **Serializer**: Uses `FavoriteModelSerializer` for serialization/deserialization.
    - **Permissions**: Only authenticated users can access this view.
    - **Custom behavior**:
        - Filters the queryset to include only the favorite books of the current user.

    """
    queryset = FavoriteBookModel.objects.all()
    serializer_class = FavoriteModelSerializer
    permission_classes = [IsAuthenticated, ]

    def get_queryset(self):
        return FavoriteBookModel.objects.filter(user=self.request.user)


class RemoveFavoriteAPIView(DestroyAPIView):
    """
    API view for removing a favorite book.

    This view allows authenticated users to delete a book from their favorites.

    Key configurations:
    - **Queryset**: Fetches all objects from the `FavoriteBookModel`.
    - **Serializer**: Uses `FavoriteModelSerializer` for serialization/deserialization.
    - **Permissions**: Only authenticated users can delete their favorite books.
    - **Custom behavior**:
        - Ensures that only the current user's favorite record is deleted via `perform_destroy`.

    """
    queryset = FavoriteBookModel.objects.all()
    serializer_class = FavoriteModelSerializer
    permission_classes = [IsAuthenticated, ]

    def perform_destroy(self, instance):
        return FavoriteBookModel.objects.filter(user=self.request.user, id=instance.id).delete()
