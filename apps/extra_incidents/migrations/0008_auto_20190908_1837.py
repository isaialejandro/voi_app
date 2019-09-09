# Generated by Django 2.1.7 on 2019-09-08 23:37

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('extra_incidents', '0007_auto_20190908_1745'),
    ]

    operations = [
        migrations.AlterField(
            model_name='extraincident',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2019, 9, 8, 23, 37, 31, 882054, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='extraincident',
            name='extra_comments',
            field=models.CharField(max_length=500, null=True),
        ),
    ]