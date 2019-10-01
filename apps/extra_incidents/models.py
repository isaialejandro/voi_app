import datetime
#from django.utils import timezone
from django.utils import timezone

from django.db import models

from django.contrib.auth.models import User

from apps.application.models import Application

from apps.extra_incidents.choices import TYPE, REGISTRY, INC_SOURCE, PAPERLESS

now = timezone.now

class ExtraIncident(models.Model):

    application = models.ForeignKey(Application, on_delete=models.DO_NOTHING)
    inc_number = models.CharField(max_length=100, null=True, blank=True) #for default apps.
    type = models.CharField(max_length=20,choices=TYPE, default=REGISTRY)
    exec_date = models.DateField()
    end_date = models.DateTimeField(blank=True, null=True)
    summary = models.TextField(max_length=1000, null=False)
    extra_comments = models.TextField(max_length=1000, null=True, blank=True)
    inc_source = models.CharField(max_length=25, choices=INC_SOURCE, default=PAPERLESS, blank=False)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING) #user created incident.
    final_user = models.ForeignKey(User, related_name='final_user', on_delete=models.DO_NOTHING, default=1) #user closed/finalized incident.
    created = models.DateTimeField(default=now)
    close_comment = models.CharField(max_length=250, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    finalized = models.BooleanField(default=False)
    closed = models.BooleanField(default=False)

    def __str__(self):
        if self.end_date:
            end_date = '{}'.format(self.end_date)
        else:
            end_date = ''
        return '{}'.format(self.application) + ' | ' + '{}'.format(self.inc_number) + ' | ' + end_date

    class Meta:

        permissions = (
            ('view_extra_incident_list', 'Visualize Extra Incident List'),
            ('create_extra_incident', 'Create extra incident'),
            ('disable_extra_incident', 'Disable extra incident'),
        )
