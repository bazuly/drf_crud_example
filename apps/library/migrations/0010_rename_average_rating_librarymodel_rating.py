# Generated by Django 5.1.4 on 2024-12-13 15:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0009_rename_ratingmodel_bookratingmodel'),
    ]

    operations = [
        migrations.RenameField(
            model_name='librarymodel',
            old_name='average_rating',
            new_name='rating',
        ),
    ]
