# Generated by Django 2.1.7 on 2019-09-28 05:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('extra_incidents', '0024_auto_20190927_2302'),
    ]

    operations = [
        migrations.AlterField(
            model_name='extraincident',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2019, 9, 28, 0, 8, 2, 160349)),
        ),
    ]