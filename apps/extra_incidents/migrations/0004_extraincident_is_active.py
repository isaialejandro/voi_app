# Generated by Django 2.1.7 on 2019-09-05 02:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('extra_incidents', '0003_auto_20190904_2057'),
    ]

    operations = [
        migrations.AddField(
            model_name='extraincident',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
