# Generated by Django 2.1.7 on 2019-09-05 01:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('extra_incidents', '0002_extraincident_created'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='extraincident',
            options={'permissions': (('view_extra_incident_list', 'Visualize Extra Incident List'), ('create_extra_incident', 'Create extra incident'), ('disable_extra_incident', 'Disable extra incident'))},
        ),
    ]