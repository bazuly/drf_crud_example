import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from django.contrib.auth.models import User
from apps.library.models import LibraryModel, FavoriteBookModel


@pytest.fixture
def user(db):
    return User.objects.create_user(
        username='testuser',
        password='password'
    )


@pytest.fixture
def client(user):
    client = APIClient()
    client.force_authenticate(user=user)
    return client


@pytest.fixture
def book(db):
    return LibraryModel.objects.create(
        title='Test Book',
        genre='Test genre',
        year=1998,
        creator=User.objects.create_user(
            username='testuser',
            password='password'
        )
    )


@pytest.mark.django_db
def test_add_to_favorites(client, book):
    url = reverse('add_favorite')
    payload = {'book': book.id}
    response = client.post(url, payload)
    assert response.status_code == status.HTTP_201_CREATED
    assert FavoriteBookModel.objects.filter(user=client.handler._force_user, book=book).exists()


@pytest.mark.django_db
def test_list_favorites(client, book):
    FavoriteBookModel.objects.create(user=client.handler._force_user, book=book)
    url = reverse('list_favorites')
    response = client.get(url)
    assert response.status_code == status.HTTP_200_OK
    assert len(response.data) == 1
    assert response.data[0]['id'] == book.id


@pytest.mark.django_db
def test_remove_favorite(client, book):
    favorite = FavoriteBookModel.objects.create(user=client.handler._force_user, book=book)
    url = reverse('remove_favorite', kwargs={'pk': book.id})
    response = client.delete(url)

    assert response.status_code == status.HTTP_204_NO_CONTENT
    assert not FavoriteBookModel.objects.filter(id=favorite.id).exists()


@pytest.mark.django_db
def test_add_duplicate_favorite(client, book):
    FavoriteBookModel.objects.create(user=client.handler._force_user, book=book)
    url = reverse('add_favorite')
    payload = {'book': book.id}
    response = client.post(url, payload)

    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert response.data['non_field_error'][0] == 'This book already in your favorites.'



















