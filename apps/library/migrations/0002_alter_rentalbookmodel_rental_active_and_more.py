# Generated by Django 5.1.4 on 2024-12-05 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rentalbookmodel',
            name='rental_active',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='rentalbookmodel',
            name='return_date',
            field=models.DateTimeField(blank=True, default=None, null=True),
        ),
    ]
