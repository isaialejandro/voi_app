# Generated by Django 2.1.7 on 2019-05-01 22:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0012_auto_20190501_1728'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ticket',
            options={'permissions': (('close_ticket', 'Can close current ticket'), ('view_ticket_detail', 'Can visualize current ticket detail'), ('disable_ticket', 'Can disable ticket'))},
        ),
    ]
