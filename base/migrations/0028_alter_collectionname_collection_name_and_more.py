# Generated by Django 4.1.7 on 2023-03-22 00:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0027_alter_collectionname_collection_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='collectionname',
            name='collection_name',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='create_at',
            field=models.DateField(default=datetime.datetime(2023, 3, 22, 0, 56, 13, 420285, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='review_rating',
            name='create_at',
            field=models.DateField(default=datetime.datetime(2023, 3, 22, 0, 56, 13, 435931, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterUniqueTogether(
            name='collectionname',
            unique_together={('user', 'collection_name')},
        ),
    ]
