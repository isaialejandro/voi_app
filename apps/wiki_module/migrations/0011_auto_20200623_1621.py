# Generated by Django 2.1.7 on 2020-06-23 21:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wiki_module', '0010_remove_blogdoc_blog_tags'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogdoc',
            name='related_tags',
        ),
        migrations.AddField(
            model_name='blogdoc',
            name='related_tags',
            field=models.ManyToManyField(to='wiki_module.Tag'),
        ),
    ]