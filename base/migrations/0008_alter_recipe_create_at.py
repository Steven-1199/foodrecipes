# Generated by Django 4.1.7 on 2023-03-17 01:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0007_alter_recipe_create_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='create_at',
            field=models.DateField(default=datetime.datetime(2023, 3, 17, 1, 9, 10, 504272, tzinfo=datetime.timezone.utc)),
        ),
    ]
