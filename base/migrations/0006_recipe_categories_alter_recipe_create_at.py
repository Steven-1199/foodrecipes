# Generated by Django 4.1.7 on 2023-03-15 00:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_alter_recipe_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='categories',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='create_at',
            field=models.DateField(default=datetime.datetime(2023, 3, 15, 0, 9, 14, 676587, tzinfo=datetime.timezone.utc)),
        ),
    ]
