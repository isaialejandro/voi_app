from django.db import models
from django.contrib.auth.models import User


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
    is_active = models.BooleanField(default=True)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, default='')

    def __str__(self):
        return self.name.capitalize()
