# Generated by Django 2.1.7 on 2020-04-08 03:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('art_version', models.CharField(max_length=200)),
                ('summary', models.CharField(max_length=100)),
                ('content', models.CharField(max_length=200)),
                ('views', models.CharField(blank=True, max_length=10)),
                ('reg_date', models.DateTimeField(auto_now_add=True)),
                ('update_date', models.DateTimeField()),
                ('status', models.BooleanField(default=1)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
                ('update_user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='update_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
