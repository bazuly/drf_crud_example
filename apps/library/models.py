from django.db import models
from django.contrib.auth.models import User


class LibraryModel(models.Model):
    title = models.CharField(max_length=255)
    genre = models.CharField(max_length=255)
    year = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.FloatField(default=0.0, blank=True, null=True)

    def __str__(self):
        return f"{self.title} {self.genre} {self.year} {self.creator}"

    class Meta:
        ordering = ["-created_at"]


class BookRatingModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(LibraryModel, on_delete=models.CASCADE, related_name="ratings")
    rating = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.user} {self.book} {self.rating}"

    # class Meta:
    #     unique_together = ("user", "book")


class FavoriteBookModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(LibraryModel, on_delete=models.CASCADE, related_name="favorites")

    def __str__(self):
        return f"{self.user} {self.book}"
