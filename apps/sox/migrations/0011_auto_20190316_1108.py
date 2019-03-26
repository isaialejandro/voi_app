# Generated by Django 2.1.7 on 2019-03-16 17:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sox', '0010_auto_20190315_1343'),
    ]

    operations = [
        migrations.AlterField(
            model_name='soxregistry',
            name='first_source_executor',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.DO_NOTHING, related_name='first_source_exec', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='soxregistry',
            name='second_source_executor',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.DO_NOTHING, related_name='second_source_exec', to=settings.AUTH_USER_MODEL),
        ),
    ]
