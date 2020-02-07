from django.db import models
from django.contrib.auth.models import User

from apps.extra_incidents.choices import TYPE, REGISTRY, INC_SOURCE, PAPERLESS, \
AMBASSADOR_TYPE, AEROPUERTOS, SK_ROLES, GSA


class Application(models.Model):

    """
    This model manage the normal and sox apps, each one with different parameters & rules
    """

    #Application Type
    NORMAL = 'Normal'
    SOX = 'Sox'

    APP_TYPE = (
        ('NORMAL', NORMAL),
        ('SOX', SOX),
    )

    name = models.CharField(max_length=50, blank=False)
    registry_date = models.DateTimeField(auto_now_add=True)
    app_type = models.CharField(max_length=6, choices=APP_TYPE, default=NORMAL, blank=False)
    is_active = models.BooleanField(default=True)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, default='')

    def __str__(self):
        #return self.name.capitalize() + '  |  ' +  self.app_type.capitalize()
        return self.name.capitalize()

    class Meta:

        permissions = (
            ('view_application_list', 'Can visualize the applications list'),
            ('create_application', 'Can create application'),
            ('update_application', 'Can update application'),
            ('disable_application', 'Can disable Application'),
        )


class TresSesentaEnUnClick(models.Model):

    ambassador_type = models.CharField(max_length=20, choices=AMBASSADOR_TYPE, default=AEROPUERTOS, null=False, blank=False)
    ambassador_id = models.CharField(max_length=6, null=False, blank=False)
    ambassador_email = models.CharField(max_length=50, null=False, blank=False)
    first_boss_id = models.CharField(max_length=6, blank=True, null=True)
    first_boss_name = models.CharField(max_length=50, blank=True, null=True)


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


class Zendesk(models.Model):

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
################################################################################


class OpCenter(models.Model):

    access_id = models.CharField(max_length=6, blank=True, null=True)
    ambassador_full_name = models.CharField(max_length=100, blank=True, null=True)


class NetTracer(models.Model):

    access_id = models.CharField(max_length=6, blank=True, null=True)
    ambassador_full_name = models.CharField(max_length=100, blank=True, null=True)
    #station = models.CharField(max_length=) #Setear choices de estaciones
    #otro campo pendiente

class SmartKargo(models.Model):

    access_id = models.CharField(max_length=6, blank=True, null=True)
    rol = models.CharField(max_length=25, choices=SK_ROLES, default=GSA, blank=False)
    station = models.CharField(max_length=6, blank=True, null=True)
    #PENDIENTE POR REVISAR MAS CAMPOS
