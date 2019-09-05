# Generated by Django 2.1.7 on 2019-09-05 00:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('application', '__first__'),
        ('applicant', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=50)),
                ('folio_number', models.CharField(blank=True, max_length=20)),
                ('priority', models.CharField(choices=[('low', 'Low'), ('mid', 'Mid'), ('high', 'High')], default='low', max_length=15)),
                ('status', models.CharField(choices=[('open', 'Open'), ('pending', 'Pending'), ('in progress', 'In Progress'), ('assigned', 'Assigned'), ('provider approval proccess', 'Provider Approval Proccess'), ('closed', 'Closed')], default='open', max_length=50)),
                ('registry_date', models.DateTimeField(auto_now_add=True)),
                ('request_type', models.CharField(choices=[('registration', 'Registration'), ('unsubscribe', 'Unsubscribe')], default='registration', max_length=25)),
                ('beneficiary_name', models.CharField(blank=True, max_length=50)),
                ('beneficiary_last_name', models.CharField(blank=True, max_length=50)),
                ('approval_owner', models.CharField(choices=[('approval', 'Approval')], default='approval', max_length=15)),
                ('approval_executor', models.CharField(choices=[('yes', 'Yes'), ('no', 'No')], default='yes', max_length=50)),
                ('approve', models.CharField(choices=[('yes', 'Yes'), ('no', 'No')], default='yes', max_length=3)),
                ('created_by', models.CharField(blank=True, max_length=50)),
                ('item_type', models.CharField(choices=[('item', 'Item')], default='item', max_length=10)),
                ('path', models.CharField(blank=True, max_length=150)),
                ('description', models.CharField(blank=True, max_length=450, null=True)),
                ('solution_date', models.DateTimeField(blank=True, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('close_comment', models.TextField(blank=True, max_length=100, null=True)),
                ('applicant', models.ForeignKey(default='', on_delete=django.db.models.deletion.DO_NOTHING, to='applicant.Applicant')),
                ('application', models.ForeignKey(default='', on_delete=django.db.models.deletion.DO_NOTHING, to='application.Application')),
                ('assigned_to', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='user_assigned', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(default='', on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'permissions': (('view_ticket_list', 'Can view the tickets list'), ('create_ticket', 'Can create new ticket'), ('update_ticket', 'Can update current ticket'), ('close_ticket', 'Can close current ticket'), ('view_ticket_detail', 'Can visualize current ticket detail'), ('disable_ticket', 'Can disable ticket')),
            },
        ),
        migrations.CreateModel(
            name='TicketHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('summary', models.TextField(max_length=450)),
                ('registry_date', models.DateTimeField(auto_now=True)),
                ('update', models.BooleanField(default=True)),
                ('finished', models.BooleanField(default=False)),
                ('ticket', models.ForeignKey(default='', on_delete=django.db.models.deletion.DO_NOTHING, to='ticket.Ticket')),
                ('user', models.ForeignKey(default='', on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
