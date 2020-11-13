from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


from apps.tools.choices import TYPE, REGISTRY, INC_SOURCE, PAPERLESS

now = timezone.now()


class ZendeskUser(models.Model):
    class Meta:
        verbose_name = 'Zendesk User'
    
    user_id = models.CharField(max_length=11, null=False, blank=True)
    name = models.CharField(max_length=50, null=False, blank=True)
    email = models.EmailField()
    role = models.CharField(max_length=350, null=False, blank=True)
    group = models.CharField(max_length=350, null=True, blank=True)
    hist = models.OneToOneField('ZendeskUserHistory', on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.name + ' - ' + self.hist.date.strftime('%d-%m-%Y %I:%M:%S %p')

class ZendeskUserHistory(models.Model):
    class Meta:
        verbose_name = 'Request History'
        verbose_name_plural = 'User Request Histories'

    total_occupied_licenses = models.CharField(max_length=3, null=True, blank=True)
    current_admins = models.CharField(max_length=3, null=True, blank=True)
    current_agents = models.CharField(max_length=3, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    excec_user = models.ForeignKey(User, on_delete=models.DO_NOTHING)

    def __str__(self):
        return '%s Occupied Licenses - ' % self.total_occupied_licenses + self.date.strftime('%d-%m-%Y %I:%M:%S %p')

#---
"""
class ABC(models.Model):
    class Meta:
        verbose_name_plural = 'ABC´s'

    title = models.CharField(max_length=100, null=True, blank=True) #for default apps incidents.
    type = models.CharField(max_length=20,choices=TYPE, default=REGISTRY)
    inc_source = models.CharField(max_length=25, choices=INC_SOURCE, default=PAPERLESS, blank=False)
    is_active = models.BooleanField(default=True)
    finalized = models.BooleanField(default=False)
    created_date = models.DateTimeField(default=now)
    end_date = models.DateTimeField(blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING) #user that created incident.
    summary = models.TextField(max_length=1000, null=False)

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
"""