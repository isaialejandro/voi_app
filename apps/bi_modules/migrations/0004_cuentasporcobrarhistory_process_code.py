# Generated by Django 2.1.7 on 2019-07-26 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bi_modules', '0003_auto_20190726_1416'),
    ]

    operations = [
        migrations.AddField(
            model_name='cuentasporcobrarhistory',
            name='process_code',
            field=models.CharField(default='', max_length=6),
        ),
    ]
