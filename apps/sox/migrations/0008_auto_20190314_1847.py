# Generated by Django 2.1.7 on 2019-03-15 00:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sox', '0007_auto_20190314_1842'),
    ]

    operations = [
        migrations.AlterField(
            model_name='soxregistry',
            name='exec_confirmed_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
