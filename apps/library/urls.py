from django.urls import path

from .views import (
    LibraryListCreateAPIView,
    LibraryRetrieveUpdateDestroyAPIView,
    CreateFavoriteAPIView,
    ListFavoriteAPIView,
    RemoveFavoriteAPIView,
    BookRatingCreateAPIView,
    # BookRatingUpdateAPIView,
    BookRatingRetrieveAPIView,
    BookRatingRemoveAPIView

)

urlpatterns = [
    path('libraries/', LibraryListCreateAPIView.as_view(), name='get_post_library'),
    path('libraries/<int:pk>/', LibraryRetrieveUpdateDestroyAPIView.as_view(), name='update_delete_library'),
    path('favourites/', ListFavoriteAPIView.as_view(), name='get_favorite'),
    path('favourites/add/', CreateFavoriteAPIView.as_view(), name='add_favorite'),
    path('favourites/remove/<int:pk>/', RemoveFavoriteAPIView.as_view(), name='remove_favorite'),
    path('libraries/set_rating/<int:pk>/', BookRatingCreateAPIView.as_view(), name='set_rating'),
    # path('libraries/update_rating/<int:pk>/', BookRatingUpdateAPIView.as_view(), name='update_rating'),
    path('libraries/retrieve_rating/<int:pk>/', BookRatingRetrieveAPIView.as_view(), name='retrieve_rating'),
    path('libraries/remove_rating/<int:pk>', BookRatingRemoveAPIView.as_view(), name='remove_rating'),
]
