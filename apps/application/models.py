from django.db import models
from django.contrib.auth.models import User

from apps.tools.choices import TYPE, REGISTRY, INC_SOURCE, PAPERLESS, \
AMBASSADOR_TYPE, AEROPUERTOS, SK_ROLES, GSA


class Application(models.Model):
    """
    This model manage the normal and sox apps, each one with different parameters & rules
    """
    NORMAL = 'Normal'
    SOX = 'Sox'

    APP_TYPE = (
        ('NORMAL', NORMAL),
        ('SOX', SOX),
    )

    name = models.CharField(max_length=50, blank=False)
    registry_date = models.DateTimeField(auto_now_add=True)
    app_type = models.CharField(max_length=6, choices=APP_TYPE, default=NORMAL, blank=False)
    is_for_bajas_semanales = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, default='')

    def __str__(self):
        return self.name.capitalize()

    class Meta:
        permissions = (
            ('view_application_list', 'Can visualize the applications list'),
            ('create_application', 'Can create application'),
            ('update_application', 'Can update application'),
            ('disable_application', 'Can disable Application'),
        )
