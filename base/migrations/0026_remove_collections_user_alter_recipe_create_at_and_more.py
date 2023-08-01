# Generated by Django 4.1.7 on 2023-03-22 00:38

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0025_alter_recipe_create_at_alter_review_rating_create_at'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='collections',
            name='user',
        ),
        migrations.AlterField(
            model_name='recipe',
            name='create_at',
            field=models.DateField(default=datetime.datetime(2023, 3, 22, 0, 38, 27, 665859, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='review_rating',
            name='create_at',
            field=models.DateField(default=datetime.datetime(2023, 3, 22, 0, 38, 27, 672436, tzinfo=datetime.timezone.utc)),
        ),
    ]
