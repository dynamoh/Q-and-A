# Generated by Django 2.2 on 2019-07-29 15:57

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('qanda', '0007_auto_20190716_1504'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='ans_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 7, 29, 15, 57, 17, 188701, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='question',
            name='asked_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 7, 29, 15, 57, 17, 187982, tzinfo=utc)),
        ),
    ]
