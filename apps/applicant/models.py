from django.db import models

from django.contrib.auth.models import User


class Applicant(models.Model):

    first_name = models.CharField(max_length=50, blank=False)
    last_name = models.CharField(max_length=50, blank=False, default='')
    registry_date = models.DateTimeField(auto_now_add=True)
    email = models.EmailField(default='')

    is_active = models.BooleanField(default=True)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, default='')

    def __str__(self):
        return self.first_name.capitalize() + ' ' + self.last_name.title()
