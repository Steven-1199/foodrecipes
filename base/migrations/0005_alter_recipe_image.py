# Generated by Django 4.1.7 on 2023-03-14 22:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_recipe'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='image',
            field=models.ImageField(null=True, upload_to='images/'),
        ),
    ]
