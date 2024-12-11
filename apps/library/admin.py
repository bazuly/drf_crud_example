from django.contrib import admin
from .models import LibraryModel, RatingModel, FavoriteBookModel

admin.site.register(LibraryModel)
admin.site.register(RatingModel)
admin.site.register(FavoriteBookModel)



