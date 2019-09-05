from django.db import models

from django.contrib.auth.models import User


class CuentasPorCobrarHistory(models.Model):

    process_code = models.CharField(max_length=6, null=False, default='')
    process_date = models.DateTimeField(auto_now_add=True)
    processed_by_year= models.BooleanField(default=False)
    processed_by_month= models.BooleanField(default=False)

    processed_years = models.CharField(max_length=100, null=True, blank=True)
    processed_months = models.CharField(max_length=100, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)

    def __str__(self):
        return '{}'.format(self.process_date)

    class Meta:
        verbose_name = 'Cuentas por cobrar History'
        verbose_name = 'Cuentas por cobrar Historie'

        permissions = (
            ('view_cuentas_por_cobrar', 'Can visualize cuentas por cobrar dashboard'),
            ('process_cuentas_por_cobrar', 'Can process cuentas por cobrar'),
        )
