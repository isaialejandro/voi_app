# Generated by Django 2.1.7 on 2019-09-08 22:45

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('extra_incidents', '0006_auto_20190908_1739'),
    ]

    operations = [
        migrations.AlterField(
            model_name='extraincident',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2019, 9, 8, 22, 45, 35, 608165, tzinfo=utc)),
        ),
    ]
