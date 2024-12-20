from rest_framework import serializers
from .models import LibraryModel, FavoriteBookModel, BookRatingModel


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
            'rating'
        ]


class LibraryRatingModelSerializer(serializers.ModelSerializer):
    book = serializers.PrimaryKeyRelatedField(
        queryset=LibraryModel.objects.all())

    class Meta:
        model = BookRatingModel
        fields = [
            'id',
            'user',
            'book',
            'rating',
        ]

    def validate(self, data):
        user = data['user']
        book = data['book']

        if BookRatingModel.objects.filter(user=user, book=book).exists():
            raise serializers.ValidationError('You already set rating')
        return data


class FavoriteModelSerializer(serializers.ModelSerializer):
    book = serializers.PrimaryKeyRelatedField(
        queryset=LibraryModel.objects.all())

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
            raise serializers.ValidationError('Book already in your favorite')
        return data
