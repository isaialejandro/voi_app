from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

from apps.application.models import Application


now = timezone.now


class BajaSemanal(models.Model):

    type = models.CharField(max_length=50, blank=True, null=False)
    subject = models.CharField(max_length=200, blank=False, null=False)
    user_code = models.CharField(max_length=20, blank=False, null=False)
    user_name = models.CharField(max_length=50, blank=False, null=False)
    request_date = models.DateField(max_length=10)
    application = models.ManyToManyField(Application)
    created_date = models.DateTimeField(default=now)
    already_checked = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)

    def __str__(self):
        return '{}'.format(self.subject + ' | ' + '{}'.format(self.created_date))

    class Meta:

        permissions = (
            ('view_bajas_semanales_list', 'Visualize Bajas Semanales list'),
            ('create_baja_semanal', 'Create Baja Semanale'),
            ('update_baja_semanal', 'Update Bajas Semanales'),
        )
