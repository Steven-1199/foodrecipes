# Generated by Django 4.1.7 on 2023-03-23 00:55

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0042_alter_recipe_create_at_alter_review_rating_create_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='create_at',
            field=models.DateField(default=datetime.datetime(2023, 3, 23, 0, 55, 21, 426237, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='review_rating',
            name='create_at',
            field=models.DateField(default=datetime.datetime(2023, 3, 23, 0, 55, 21, 426237, tzinfo=datetime.timezone.utc)),
        ),
    ]
