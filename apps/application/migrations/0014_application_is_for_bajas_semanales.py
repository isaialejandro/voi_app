# Generated by Django 2.1.7 on 2020-02-10 03:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0013_auto_20191116_1254'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='is_for_bajas_semanales',
            field=models.BooleanField(default=False),
        ),
    ]
