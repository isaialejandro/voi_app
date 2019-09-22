from django.utils import timezone

from django.db import models

from django.contrib.auth.models import User

from apps.application.models import Application

from apps.extra_incidents.choices import TYPE, REGISTRY, INC_SOURCE, PAPERLESS


class ExtraIncident(models.Model):

    application = models.ForeignKey(Application, on_delete=models.DO_NOTHING)
    inc_number = models.CharField(max_length=12, null=True, blank=True) #for default apps.
    type = models.CharField(max_length=20,choices=TYPE, default=REGISTRY)
    exec_date = models.DateField()
    end_date = models.DateField(null=True)
    summary = models.TextField(max_length=1000, null=False)
    extra_comments = models.TextField(max_length=1000, null=True, blank=True)
    inc_source = models.CharField(max_length=25, choices=INC_SOURCE, default=PAPERLESS, blank=False)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    created = models.DateTimeField(default=timezone.now())
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return '{}'.format(self.application) + ' | ' + '{}'.format(self.inc_number) + ' | ' + '{}'.format(self.end_date)

    class Meta:

        permissions = (
            ('view_extra_incident_list', 'Visualize Extra Incident List'),
            ('create_extra_incident', 'Create extra incident'),
            ('disable_extra_incident', 'Disable extra incident'),
        )
