from celery import shared_task
from .models import LibraryModel, User


@shared_task
def book_creation(book_id, creator_id):

    book = LibraryModel.objects.get(id=book_id)
    user = User.objects.get(id=creator_id)

    print(f'Book {book.title}, added by user: {user.username}')

    return f"Уведомление для книги '{book.title}' успешно отправлено."
