# Generated by Django 4.1.7 on 2023-03-21 14:55

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0019_recipe_recipe_favorite_ingrediets_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='CollectionName',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('collection_name', models.TextField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='collection_name_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterField(
            model_name='recipe',
            name='create_at',
            field=models.DateField(default=datetime.datetime(2023, 3, 21, 14, 55, 49, 794877, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='review_rating',
            name='create_at',
            field=models.DateField(default=datetime.datetime(2023, 3, 21, 14, 55, 49, 810878, tzinfo=datetime.timezone.utc)),
        ),
        migrations.CreateModel(
            name='Collections',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('collection_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.collectionname')),
                ('recipe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.recipe')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='collections_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
