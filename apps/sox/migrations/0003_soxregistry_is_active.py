# Generated by Django 2.1.7 on 2019-03-14 20:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sox', '0002_auto_20190314_1420'),
    ]

    operations = [
        migrations.AddField(
            model_name='soxregistry',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
