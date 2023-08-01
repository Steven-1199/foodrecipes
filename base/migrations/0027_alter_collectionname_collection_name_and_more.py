# Generated by Django 4.1.7 on 2023-03-22 00:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0026_remove_collections_user_alter_recipe_create_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='collectionname',
            name='collection_name',
            field=models.TextField(unique=True),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='create_at',
            field=models.DateField(default=datetime.datetime(2023, 3, 22, 0, 53, 32, 128983, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='review_rating',
            name='create_at',
            field=models.DateField(default=datetime.datetime(2023, 3, 22, 0, 53, 32, 140943, tzinfo=datetime.timezone.utc)),
        ),
    ]
