# Generated by Django 4.1.7 on 2023-03-21 15:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0020_collectionname_alter_recipe_create_at_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='collectionname',
            name='collectionImg',
            field=models.ImageField(blank=True, default=None, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='create_at',
            field=models.DateField(default=datetime.datetime(2023, 3, 21, 15, 5, 30, 509822, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='review_rating',
            name='create_at',
            field=models.DateField(default=datetime.datetime(2023, 3, 21, 15, 5, 30, 525452, tzinfo=datetime.timezone.utc)),
        ),
    ]
