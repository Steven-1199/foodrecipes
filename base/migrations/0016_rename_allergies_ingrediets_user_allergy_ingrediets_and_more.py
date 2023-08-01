# Generated by Django 4.1.7 on 2023-03-20 02:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0015_user_allergies_ingrediets_user_favorite_ingrediets_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='allergies_ingrediets',
            new_name='allergy_ingrediets',
        ),
        migrations.AlterField(
            model_name='recipe',
            name='create_at',
            field=models.DateField(default=datetime.datetime(2023, 3, 20, 2, 48, 48, 236692, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='review_rating',
            name='create_at',
            field=models.DateField(default=datetime.datetime(2023, 3, 20, 2, 48, 48, 236692, tzinfo=datetime.timezone.utc)),
        ),
    ]
