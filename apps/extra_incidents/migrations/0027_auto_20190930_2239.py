# Generated by Django 2.1.7 on 2019-10-01 03:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('extra_incidents', '0026_auto_20190930_2225'),
    ]

    operations = [
        migrations.AlterField(
            model_name='extraincident',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2019, 9, 30, 22, 39, 18, 640028)),
        ),
        migrations.AlterField(
            model_name='extraincident',
            name='end_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
