# Generated by Django 2.1.7 on 2019-09-22 21:08

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('extra_incidents', '0016_auto_20190921_1753'),
    ]

    operations = [
        migrations.AddField(
            model_name='extraincident',
            name='finalized',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='extraincident',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2019, 9, 22, 21, 8, 38, 755119, tzinfo=utc)),
        ),
    ]
