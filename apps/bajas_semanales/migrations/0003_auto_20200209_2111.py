# Generated by Django 2.1.7 on 2020-02-10 03:11

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0013_auto_20191116_1254'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('bajas_semanales', '0002_auto_20200209_2107'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Baja',
            new_name='BajasSemanales',
        ),
    ]
