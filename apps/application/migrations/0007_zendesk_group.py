# Generated by Django 2.1.7 on 2019-11-15 23:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0006_zendeskgroup'),
    ]

    operations = [
        migrations.AddField(
            model_name='zendesk',
            name='group',
            field=models.ManyToManyField(to='application.ZendeskGroup'),
        ),
    ]
