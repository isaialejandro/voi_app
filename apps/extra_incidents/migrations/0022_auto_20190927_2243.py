# Generated by Django 2.1.7 on 2019-09-28 03:43

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('extra_incidents', '0021_auto_20190927_2217'),
    ]

    operations = [
        migrations.AddField(
            model_name='extraincident',
            name='final_user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, related_name='final_user', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='extraincident',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2019, 9, 27, 22, 43, 10, 958367)),
        ),
    ]
