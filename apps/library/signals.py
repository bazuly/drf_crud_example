from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import RatingModel


@receiver([post_save, post_delete], sender=RatingModel)
def update_average_rating(sender, instance, **kwargs):
    book = instance.book
    ratings = book.ratings.all()
    book.average_rating = sum(r.rating for r in ratings) / ratings.count() if ratings else 0
    book.save()

