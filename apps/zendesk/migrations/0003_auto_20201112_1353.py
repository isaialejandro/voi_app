# Generated by Django 2.1.7 on 2020-11-12 19:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zendesk', '0002_auto_20201112_1351'),
    ]

    operations = [
        migrations.AlterField(
            model_name='zendeskuserhistory',
            name='current_admins',
            field=models.CharField(blank=True, max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='zendeskuserhistory',
            name='current_agents',
            field=models.CharField(blank=True, max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='zendeskuserhistory',
            name='occupied_licenses',
            field=models.CharField(blank=True, max_length=3, null=True),
        ),
    ]