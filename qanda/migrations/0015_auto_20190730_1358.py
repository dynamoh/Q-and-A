# Generated by Django 2.2 on 2019-07-30 08:28

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('qanda', '0014_auto_20190730_1356'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='ans_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 7, 30, 8, 28, 34, 733117, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='profile',
            name='slug',
            field=models.SlugField(blank=True),
        ),
        migrations.AlterField(
            model_name='question',
            name='asked_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 7, 30, 8, 28, 34, 730267, tzinfo=utc)),
        ),
    ]