# Generated by Django 2.1.7 on 2020-02-14 02:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bajas_semanales', '0012_tipobaja_is_active'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tipobaja',
            options={'permissions': (('view_tipo_bajas', 'Visualize Tipo de Bajas List'), ('update_tipo_baja', 'Update Tipo de Baja'), ('deactivate_tipo_baja', 'Deactivate Tipo de Baja'))},
        ),
    ]
