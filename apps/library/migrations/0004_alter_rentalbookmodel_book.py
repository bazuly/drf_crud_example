# Generated by Django 5.1.4 on 2024-12-09 16:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0003_alter_rentalbookmodel_rental_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rentalbookmodel',
            name='book',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rentals', to='library.bookmodel'),
        ),
    ]