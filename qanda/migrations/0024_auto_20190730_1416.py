# Generated by Django 2.2 on 2019-07-30 08:46

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('qanda', '0023_auto_20190730_1414'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='ans_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 7, 30, 8, 46, 10, 406645, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='question',
            name='asked_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 7, 30, 8, 46, 10, 406645, tzinfo=utc)),
        ),
    ]