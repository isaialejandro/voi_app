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
        verbose_name = 'Cuentas por cobrar History'

        permissions = (
            ('view_cuentas_por_cobrar', 'Can visualize cuentas por cobrar dashboard'),
            ('process_cuentas_por_cobrar', 'Can process cuentas por cobrar'),
        )


class Account(models.Model):

    account_period = models.CharField(max_length=25, blank=True, null=True)
    proper_account_period = models.CharField(max_length=25, blank=True, null=True)
    company_code = models.CharField(max_length=25, blank=True, null=True)
    journal_entry = models.CharField(max_length=25, blank=True, null=True)
    debit_account_number = models.CharField(max_length=25, blank=True, null=True)
    debit_center_number = models.CharField(max_length=25, blank=True, null=True)
    credit_account_number = models.CharField(max_length=25, blank=True, null=True)
    credit_center_number = models.CharField(max_length=25, blank=True, null=True)
    account_event = models.CharField(max_length=25, blank=True, null=True)
    account_type = models.CharField(max_length=25, blank=True, null=True)
    mapping_number = models.CharField(max_length=25, blank=True, null=True)
    local_amount = models.CharField(max_length=25, blank=True, null=True)
    local_currency = models.CharField(max_length=25, blank=True, null=True)
    host_amount = models.CharField(max_length=25, blank=True, null=True)
    host_currency = models.CharField(max_length=25, blank=True, null=True)
    reference_code = models.CharField(max_length=25, blank=True, null=True)
    transaction_key = models.CharField(max_length=25, blank=True, null=True)
    reference_date = models.CharField(max_length=25, blank=True, null=True)
    revenue_and_nonrevenue = models.CharField(max_length=25, blank=True, null=True)
    suspense_type = models.CharField(max_length=25, blank=True, null=True)
    reg_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{}'.format(self.account_period) + ' ' + '{}'.format(self.reg_date)
