# Generated by Django 2.1.7 on 2020-12-02 20:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zendesk', '0019_auto_20201202_1446'),
    ]

    operations = [
        migrations.AlterField(
            model_name='zendeskuserhistory',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
