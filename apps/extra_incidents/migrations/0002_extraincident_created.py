# Generated by Django 2.1.7 on 2019-09-05 01:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('extra_incidents', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='extraincident',
            name='created',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
