# Generated by Django 3.1.4 on 2020-12-16 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_auto_20201216_1917'),
    ]

    operations = [
        migrations.AlterField(
            model_name='description',
            name='description',
            field=models.CharField(max_length=600),
        ),
    ]
