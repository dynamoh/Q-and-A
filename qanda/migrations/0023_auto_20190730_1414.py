# Generated by Django 2.2 on 2019-07-30 08:44

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('qanda', '0022_auto_20190730_1413'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='ans_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 7, 30, 8, 44, 50, 897919, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='answer',
            name='slug',
            field=models.SlugField(unique=True),
        ),
        migrations.AlterField(
            model_name='question',
            name='asked_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 7, 30, 8, 44, 50, 897919, tzinfo=utc)),
        ),
    ]
