# Generated by Django 2.1.7 on 2020-01-04 06:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('extra_incidents', '0037_auto_20191207_1252'),
    ]

    operations = [
        migrations.RenameField(
            model_name='extraincident',
            old_name='created',
            new_name='created_date',
        ),
    ]