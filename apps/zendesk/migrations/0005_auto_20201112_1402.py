# Generated by Django 2.1.7 on 2020-11-12 20:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zendesk', '0004_auto_20201112_1353'),
    ]

    operations = [
        migrations.AlterField(
            model_name='zendeskuserhistory',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
