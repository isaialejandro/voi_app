# Generated by Django 2.1.7 on 2020-02-14 17:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bajas_semanales', '0014_auto_20200213_2050'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tipobaja',
            options={'permissions': (('view_tipo_bajas_list', 'Visualize Tipo de Bajas List'), ('create_tipo_baja', 'Create Tipo Baja'), ('update_tipo_baja', 'Update Tipo de Baja'), ('deactivate_tipo_baja', 'Deactivate Tipo de Baja'))},
        ),
    ]
