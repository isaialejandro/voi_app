# Generated by Django 2.1.7 on 2020-12-02 05:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zendesk', '0012_auto_20201124_1833'),
    ]

    operations = [
        migrations.AlterField(
            model_name='zendeskuserhistory',
            name='date',
            field=models.DateTimeField(blank=True),
        ),
    ]