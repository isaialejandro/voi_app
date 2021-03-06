# Generated by Django 2.1.7 on 2019-11-08 06:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('extra_incidents', '0034_remove_extraincident_exec_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='extraincident',
            name='extra_comments',
        ),
        migrations.AlterField(
            model_name='extraincident',
            name='nettracer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='application.NetTracer'),
        ),
        migrations.AlterField(
            model_name='extraincident',
            name='opcenter',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='application.OpCenter'),
        ),
        migrations.AlterField(
            model_name='extraincident',
            name='smartkargo',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='application.SmartKargo'),
        ),
        migrations.AlterField(
            model_name='extraincident',
            name='zendesk',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='application.Zendesk'),
        ),
    ]
