from django.urls import path
from .views import (
    LibraryListCreateAPIView,
    LibraryRetrieveUpdateDestroyAPIView,
    CreateFavoriteAPIView,
    ListFavoriteAPIView,
    RemoveFavoriteAPIView
)

urlpatterns = [
    path('libraries/', LibraryListCreateAPIView.as_view(), name='get_post_library'),
    path('libraries/<int:pk>/', LibraryRetrieveUpdateDestroyAPIView.as_view(), name='update_delete_library'),
    path('favourites/', ListFavoriteAPIView.as_view(), name='get_favorite'),
    path('favourites/add/', CreateFavoriteAPIView.as_view(), name='add_favorite'),
    path('favourites/remove/<int:pk>/', RemoveFavoriteAPIView.as_view(), name='remove_favorite'),

]
