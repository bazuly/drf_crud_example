import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from django.contrib.auth.models import User
from apps.library.models import LibraryModel, FavoriteBookModel, BookRatingModel


@pytest.mark.django_db
class TestFavoritesAPI:
    @pytest.fixture(autouse=True)
    def setup(self, db):
        self.user = User.objects.create_user(
            username='testuser',
            password='password'
        )
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)

        self.book = LibraryModel.objects.create(
            title='Test Book',
            genre='Test genre',
            year=1998,
            creator=User.objects.create_user(
                username='bookcreator',
                password='password'
            )
        )

    def test_list_favorites(self):
        FavoriteBookModel.objects.create(user=self.user, book=self.book)
        url = reverse('get_favorite')
        response = self.client.get(url)

        assert response.status_code == status.HTTP_200_OK
        assert len(response.data) == 1
        assert response.data[0]['book']['id'] == self.book.id

    def test_remove_favorite(self):
        favorite = FavoriteBookModel.objects.create(user=self.user, book=self.book)
        url = reverse('remove_favorite', kwargs={'pk': favorite.id})
        response = self.client.delete(url)

        assert response.status_code == status.HTTP_204_NO_CONTENT
        assert not FavoriteBookModel.objects.filter(id=favorite.id).exists()

    def test_add_duplicate_favorite(self):
        favorite = FavoriteBookModel.objects.create(user=self.user, book=self.book)
        url = reverse('add_favorite')
        payload = {'book': self.book.id}
        response = self.client.post(url, payload)

        assert response.status_code == status.HTTP_400_BAD_REQUEST

        assert FavoriteBookModel.objects.filter(id=favorite.id, book=self.book).exists()
        assert FavoriteBookModel.objects.filter(user=self.user, book=self.book).count() == 1

    #
    # def test_create_rating(self):
    #     rating = BookRatingModel.objects.create(user=self.user, book=self.book)
    #     url = reverse('set_rating')
    #     payload = {'book': self.book.id}
    #     response = self.client.post(url, payload)
    #
    #     assert response.status_code == status.HTTP_201_CREATED
    #     assert BookRatingModel.objects.filter(id=rating.id, book=self.book).exists()


















