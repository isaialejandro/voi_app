# Generated by Django 2.1.7 on 2020-06-23 20:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wiki_module', '0008_auto_20200623_1516'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogdoc',
            name='related_tags',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='wiki_module.Tag'),
        ),
    ]
