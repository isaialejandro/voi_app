# Generated by Django 2.1.7 on 2019-11-15 23:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0010_auto_20191115_1756'),
    ]

    operations = [
        migrations.AlterField(
            model_name='zendesk',
            name='group',
            field=models.ManyToManyField(blank=True, null=True, to='application.ZendeskGroup'),
        ),
    ]
