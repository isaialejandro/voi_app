from datetime import datetime

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


from apps.tools.choices import TYPE, REGISTRY, INC_SOURCE, PAPERLESS

now = timezone.now


class ZendeskUser(models.Model):
    class Meta:
        verbose_name = 'Zendesk User'
        permissions = (
            ('view_active_zendesk_user_list', 'View active Zendesk userlist'),
            ('get_active_zendesk_user_list', 'Get active Zendesk userlist'),
            ('export_active_zendesk_user_list', 'Export Zendesk userlist'),
        )
    
    user_id = models.CharField(max_length=50, null=False, blank=True)
    name = models.CharField(max_length=50, null=False, blank=True)
    email = models.EmailField()
    role = models.CharField(max_length=350, null=False, blank=True)
    group = models.CharField(max_length=350, null=True, blank=True)
    hist = models.ForeignKey('ZendeskUserHistory', on_delete=models.DO_NOTHING, null=True)

    def __str__(self):
        return self.name + ' - ' + 'Exec Date: ' + \
        (self.hist.date.strftime('%d-%m-%Y %I:%M:%S %p') if self.hist.date else '')

class ZendeskUserHistory(models.Model):
    class Meta:
        verbose_name = 'Request History'
        verbose_name_plural = 'User Request Histories'
        permissions = (
            ('view_zendesk_active_user_hist', 'View Zendesk active User History'),
        )

    total_occupied_licenses = models.CharField(max_length=3, null=True, blank=True)
    current_admins = models.CharField(max_length=3, null=True, blank=True)
    current_agents = models.CharField(max_length=3, null=True, blank=True)
    date = models.DateTimeField(default=now)
    exec_user = models.ForeignKey(User, on_delete=models.DO_NOTHING)

    def __str__(self):
        return '%s Occupied Licenses - ' % self.total_occupied_licenses + '{}'.format(self.date.strftime("%d %b %Y %H:%M:%S"))

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
    
    #----------------------------------------------------------------
    previous_agent_name = models.CharField(max_length=100, blank=False, null=False)
    previous_agent_email = models.CharField(max_length=50, blank=False, null=False)
    current_agent_name = models.CharField(max_length=100, blank=False, null=False)
    current_agent_email = models.CharField(max_length=50, blank=False, null=False)
    rol = models.ForeignKey('ZendeskRol', null=True, blank=True, on_delete=models.DO_NOTHING)
    group = models.ManyToManyField(ZendeskGroup)
    registry_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, blank=True)

    def __str__(self):
        return 'Current agent: ' + self.current_agent_name + ' || ' + '{}'.format(self.registry_date)
    
"""

"""
################################################################################
class ZendeskRol(models.Model):

    rol = models.CharField(max_length=25, null=True, blank=True)
    registry_date = models.DateTimeField(auto_now_add=True)

    def ___str__(self):
        return self.rol + ' || ' + '{}'.format(self.registry_date)


class ZendeskGroup(models.Model):

    group = models.CharField(max_length=40, null=True, blank=True)
    registry_date = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, blank=True, null=True)

    def __str__(self):
        return self.group + ' || ' + '{}'.format(self.registry_date)
        """