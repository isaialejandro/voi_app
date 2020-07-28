from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from apps.bi_modules.models import CuentasPorCobrarHistory, Account

# Register your models here.
admin.site.register(CuentasPorCobrarHistory)


@admin.register(Account)
class Account(ImportExportModelAdmin):

    #list_display = [n.name for n in Account._meta.get_all_field_names()]
    pass
