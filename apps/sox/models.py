import datetime

from django.db import models

from django.contrib.auth.models import User

from apps.application.models import Application

now = datetime.datetime.now()


class SOXRegistry(models.Model):

    YES = 'yes'
    NO = 'no'
    MAIL = (
        (YES, 'Yes'),
        (NO, 'No'),
    )

    REGISTRATION = 'registration'
    UNSUBSCRIBE = 'unsubscribe'
    TYPE_REQUEST = (
        (REGISTRATION, 'Registration'),
        (UNSUBSCRIBE, 'Unsubscribe'),
    )

    EXEC_BUT_NOT_FINISHED = 'executed but not finished'
    WAITING_FOR_EXEC_APPROVAL = 'waiting for executor approval'
    APPROVED_BY_EXEC = 'approved by executor'

    STATUS = (
        (EXEC_BUT_NOT_FINISHED, 'Executed but not Finished'),
        (WAITING_FOR_EXEC_APPROVAL, 'Waiting for Executor Approval'),
        (APPROVED_BY_EXEC, 'Approved by Executor'),
    )

    BAJA_TALENTO='baja talento'
    SHAREPOINT = 'sharepoint'
    APP_SOURCES = (
        (BAJA_TALENTO, 'Baja de Talento'),
        (SHAREPOINT, 'Sharepoint'),
    )

    folio_number = models.CharField(max_length=25, blank=True, null=True)
    application = models.ForeignKey(Application, on_delete=models.DO_NOTHING, default='')
    request_type = models.CharField(max_length=30, choices=TYPE_REQUEST, default=REGISTRATION)
    affected_user = models.CharField(max_length=200, blank=True) #usuario al que se dará de alta o baja
    executor = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name="executor", default='')
    execution_date = models.DateField(blank=True, default='2019-03-20')
    status = models.CharField(max_length=30, choices=STATUS, default='')

    sent_email_to_exec = models.CharField(max_length=3, choices=MAIL, default=YES)
    confirmed_by_exec = models.CharField(max_length=3, choices=MAIL, default=YES)
    exec_confirmed_date = models.DateField(blank=True, null=True)

    first_source = models.CharField(max_length=50, choices=APP_SOURCES, default=SHAREPOINT)
    first_source_date = models.DateField(blank=True, null=True)
    first_source_executor = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name="first_source_exec", default='')

    second_source = models.CharField(max_length=50, choices=APP_SOURCES, default='', blank=True)
    second_source_date = models.DateField(blank=True, null=True)
    second_source_executor = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name="second_source_exec", default='')
    
    registry_date = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, default='')


class SoxHistory(models.Model):

    sox = models.ForeignKey('SOXRegistry', on_delete=models.DO_NOTHING, default='')
    registry_date = models.DateTimeField(auto_now=now)
    update = models.BooleanField(default=True)     #Bandera que indica si el registro se actualizó o no.
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, default='')