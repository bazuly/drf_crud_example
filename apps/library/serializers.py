from rest_framework import serializers
from .models import LibraryModel, FavoriteBookModel


class LibraryModelSerializer(serializers.ModelSerializer):
    creator = serializers.ReadOnlyField(source='creator.username')

    class Meta:
        model = LibraryModel
        fields = [
            'id',
            'title',
            'genre',
            'year',
            'creator',
            'average_rating'
        ]


class FavoriteModelSerializer(serializers.ModelSerializer):
    book = LibraryModelSerializer()
    class Meta:
        model = FavoriteBookModel
        fields = [
            'id',
            'user',
            'book',
        ]

    def validate(self, data):
        user = data['user']
        book = data['book']

        if FavoriteBookModel.objects.filter(user=user, book=book).exists():
            raise serializers.ValidationError('Book already in your favourite')
        return data
