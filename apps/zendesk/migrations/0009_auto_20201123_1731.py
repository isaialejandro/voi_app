# Generated by Django 2.1.7 on 2020-11-23 23:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zendesk', '0008_auto_20201123_1729'),
    ]

    operations = [
        migrations.AlterField(
            model_name='zendeskuser',
            name='user_id',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
