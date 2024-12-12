from django.contrib import admin
from .models import LibraryModel, BookRatingModel, FavoriteBookModel

admin.site.register(LibraryModel)
admin.site.register(BookRatingModel)
admin.site.register(FavoriteBookModel)



