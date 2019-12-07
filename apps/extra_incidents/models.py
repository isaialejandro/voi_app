import datetime
#from django.utils import timezone
from django.utils import timezone

from django.db import models

from django.contrib.auth.models import User

from apps.application.models import Application, Zendesk, OpCenter, NetTracer, \
SmartKargo

from apps.extra_incidents.choices import TYPE, REGISTRY, INC_SOURCE, PAPERLESS, \
AMBASSADOR_TYPE, AEROPUERTOS

now = timezone.now


class ExtraIncident(models.Model):

    application = models.ForeignKey(Application, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=100, null=True, blank=True) #for default apps.
    type = models.CharField(max_length=20,choices=TYPE, default=REGISTRY)
    end_date = models.DateTimeField(blank=True, null=True)
    inc_source = models.CharField(max_length=25, choices=INC_SOURCE, default=PAPERLESS, blank=False)
    is_active = models.BooleanField(default=True)
    finalized = models.BooleanField(default=False)
    created = models.DateTimeField(default=now)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING) #user created incident.
    final_user = models.ForeignKey(User, related_name='final_user', on_delete=models.DO_NOTHING, default=1) #user closed/finalized incident.
    #Custom Extra incidents
    summary = models.TextField(max_length=1000, null=False)

    zendesk = models.ForeignKey(Zendesk, blank=True, null=True, on_delete=models.DO_NOTHING)
    opcenter = models.ForeignKey(OpCenter, blank=True, null=True, on_delete=models.DO_NOTHING)
    nettracer = models.ForeignKey(NetTracer, blank=True, null=True, on_delete=models.DO_NOTHING)
    smartkargo = models.ForeignKey(SmartKargo, blank=True, null=True, on_delete=models.DO_NOTHING)

    def __str__(self):
        if self.end_date:
            end_date = '{}'.format(self.end_date)
        else:
            end_date = ''
        return '{}'.format(self.application) + ' | ' + '{}'.format(self.title) + ' | ' + end_date

    class Meta:

        permissions = (
            ('view_extra_incident_list', 'Visualize Extra Incident List'),
            ('create_extra_incident', 'Create extra incident'),
            ('update_extra_incident', 'Update extra incident'),
            ('disable_extra_incident', 'Disable extra incident'),
            ('view_extra_incident_detail', 'Visualize Extra Incident Detail'),
            ('finalize_extra_incident', 'Finalize Extra Incident'),
        )
