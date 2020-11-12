from django.db import models
from django.contrib.auth.models import User


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
