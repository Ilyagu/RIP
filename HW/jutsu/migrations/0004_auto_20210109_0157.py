# Generated by Django 3.1.5 on 2021-01-08 22:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jutsu', '0003_auto_20210108_1912'),
    ]

    operations = [
        migrations.AlterField(
            model_name='anime',
            name='head_img',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='anime',
            name='img',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='сharacter',
            name='img',
            field=models.CharField(max_length=200),
        ),
    ]
