from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

from apps.application.models import Application


now = timezone.now


class TipoBaja(models.Model):

    type = models.CharField(max_length=100, blank=False, null=False)
    created_date = models.DateTimeField(default=now)
    is_active = models.BooleanField(default=True)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, default=1)

    def __str__(self):
        return self.type

    class Meta:
        permissions = (
            ('view_tipo_bajas_list', 'Visualize Tipo de Bajas List'),
            ('create_tipo_baja', 'Create Tipo Baja'),
            ('update_tipo_baja', 'Update Tipo de Baja'),
            ('deactivate_tipo_baja', 'Deactivate Tipo de Baja'),
        )


class BajaSemanal(models.Model):

    uid = models.CharField(max_length=100, null=True, blank=True)
    type = models.ForeignKey('TipoBaja', on_delete=models.DO_NOTHING)
    subject = models.CharField(max_length=200, blank=False, null=False)
    user_code = models.CharField(max_length=20, blank=False, null=False)
    user_name = models.CharField(max_length=50, blank=False, null=False)
    request_date = models.DateField(max_length=10)
    application = models.ManyToManyField(Application)
    created_date = models.DateTimeField(default=now)
    already_checked = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True)
    last_user_update = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='last_updated_user')

    def __str__(self):
        return '{}'.format(self.subject + ' | ' + '{}'.format(self.created_date))

    class Meta:
        permissions = (
            ('view_bajas_semanales_list', 'Visualize Bajas Semanales list'),
            ('create_baja_semanal', 'Create Baja Semanale'),
            ('update_baja_semanal', 'Update Bajas Semanales'),
        )
