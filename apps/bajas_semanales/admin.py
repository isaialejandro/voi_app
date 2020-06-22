from django.contrib import admin

from import_export.admin import ImportExportModelAdmin

from apps.bajas_semanales.models import TipoBaja, BajaSemanal
from apps.bajas_semanales.resources import BajaSemanalResource


@admin.register(TipoBaja)
#class TipoBajaAdmin(admin.ModelAdmin):
class TipoBajaAdmin(ImportExportModelAdmin):

    list_display = ('type', 'created_date', 'is_active')


@admin.register(BajaSemanal)
#class BajaSemanalAdmin(admin.ModelAdmin):
class BajaSemanalAdmin(ImportExportModelAdmin):

    list_display = (
        'type',
        'subject',
        'user_code',
        'user_name',
        'request_date',
        'user',
        'already_checked',
        'last_user_update'
    )
