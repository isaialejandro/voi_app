# Generated by Django 2.1.7 on 2019-09-28 03:17

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('extra_incidents', '0020_auto_20190927_2203'),
    ]

    operations = [
        migrations.AlterField(
            model_name='extraincident',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2019, 9, 27, 22, 17, 25, 652059)),
        ),
        migrations.AlterField(
            model_name='extraincident',
            name='inc_number',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
