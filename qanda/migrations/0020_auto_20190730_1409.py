# Generated by Django 2.2 on 2019-07-30 08:39

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('qanda', '0019_auto_20190730_1407'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='myprofile',
            name='slug',
        ),
        migrations.AlterField(
            model_name='answer',
            name='ans_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 7, 30, 8, 39, 44, 1211, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='question',
            name='asked_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 7, 30, 8, 39, 44, 213, tzinfo=utc)),
        ),
    ]
