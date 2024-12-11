from django_filters import rest_framework as filters
from .models import LibraryModel


class LibraryFilter(filters.FilterSet):
    title = filters.CharFilter(lookup_expr='icontains')
    genre = filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = LibraryModel
        fields = ('title', 'genre')