# Generated by Django 2.1.7 on 2019-09-08 22:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('extra_incidents', '0004_extraincident_is_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='extraincident',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2019, 9, 8, 17, 36, 32, 33232)),
        ),
    ]
