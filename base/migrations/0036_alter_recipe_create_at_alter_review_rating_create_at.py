# Generated by Django 4.1.7 on 2023-03-22 01:03

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0035_alter_recipe_create_at_alter_review_rating_create_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='create_at',
            field=models.DateField(default=datetime.datetime(2023, 3, 22, 1, 3, 57, 139660, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='review_rating',
            name='create_at',
            field=models.DateField(default=datetime.datetime(2023, 3, 22, 1, 3, 57, 139660, tzinfo=datetime.timezone.utc)),
        ),
    ]
