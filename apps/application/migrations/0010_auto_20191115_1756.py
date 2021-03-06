# Generated by Django 2.1.7 on 2019-11-15 23:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0009_auto_20191115_1751'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='zendeskrol',
            name='is_active',
        ),
        migrations.RemoveField(
            model_name='zendeskrol',
            name='user',
        ),
        migrations.AddField(
            model_name='zendesk',
            name='rol',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='application.ZendeskRol'),
        ),
        migrations.AlterField(
            model_name='zendeskgroup',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
        ),
    ]
