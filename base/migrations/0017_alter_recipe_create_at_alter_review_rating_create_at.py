# Generated by Django 4.1.7 on 2023-03-20 04:06

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0016_rename_allergies_ingrediets_user_allergy_ingrediets_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='create_at',
            field=models.DateField(default=datetime.datetime(2023, 3, 20, 4, 6, 40, 983868, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='review_rating',
            name='create_at',
            field=models.DateField(default=datetime.datetime(2023, 3, 20, 4, 6, 40, 991843, tzinfo=datetime.timezone.utc)),
        ),
    ]
