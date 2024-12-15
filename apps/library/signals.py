from .models import BookRatingModel, LibraryModel
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver


@receiver(post_save, sender=BookRatingModel)
@receiver(post_delete, sender=LibraryModel)
def update_book_rating(sender, instance, **kwargs):
    book = instance.book
    ratings = instance.rating

    if ratings.exists():
        book.rating = sum(ratings.rating for rating in ratings) / ratings.count()
    else:
        book.rating = 0.0

    book.save()
