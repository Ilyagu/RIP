# Generated by Django 3.1.4 on 2020-12-16 15:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_auto_20201216_1721'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='description',
            name='anime_id',
        ),
        migrations.DeleteModel(
            name='Anime',
        ),
        migrations.DeleteModel(
            name='Description',
        ),
    ]