# Generated by Django 5.1.4 on 2024-12-11 13:10

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0007_favoritemodel'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameModel(
            old_name='FavoriteModel',
            new_name='FavoriteBookModel',
        ),
    ]