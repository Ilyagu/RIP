# Generated by Django 3.1.4 on 2020-12-16 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_anime_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='description',
            name='description',
            field=models.CharField(max_length=400),
        ),
    ]
