# Generated by Django 2.1.7 on 2019-12-06 03:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('applicant', '0002_auto_20191205_1825'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='applicant',
            options={'permissions': (('view_applicant_list', 'Can visualize applicant list'), ('update_applicant_list', 'Update applicant list'), ('create_applicant', 'Can create applicant'), ('can_disable_applicant', 'Can disable Applicant'))},
        ),
    ]
