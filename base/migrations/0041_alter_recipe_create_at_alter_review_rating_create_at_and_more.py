# Generated by Django 4.1.7 on 2023-03-23 00:49

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0040_alter_collectionname_collectionimg_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='create_at',
            field=models.DateField(default=datetime.datetime(2023, 3, 23, 0, 49, 55, 265053, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='review_rating',
            name='create_at',
            field=models.DateField(default=datetime.datetime(2023, 3, 23, 0, 49, 55, 272001, tzinfo=datetime.timezone.utc)),
        ),
        migrations.CreateModel(
            name='Following',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('follow', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='follow_user', to=settings.AUTH_USER_MODEL)),
                ('follow_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='follow_by_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
