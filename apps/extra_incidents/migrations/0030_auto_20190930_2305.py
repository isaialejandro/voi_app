# Generated by Django 2.1.7 on 2019-10-01 04:05

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('extra_incidents', '0029_auto_20190930_2255'),
    ]

    operations = [
        migrations.AlterField(
            model_name='extraincident',
            name='created',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
