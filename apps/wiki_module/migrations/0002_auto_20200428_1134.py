# Generated by Django 2.1.7 on 2020-04-28 16:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wiki_module', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogdoc',
            name='created_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='created_by', to=settings.AUTH_USER_MODEL),
        ),
    ]
