from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from apps.extra_incidents.models import ExtraIncident

from apps.tools.mixins.admin_mixins import ExportCSVMixin


@admin.register(ExtraIncident)
class ExtraIncidentAdmin(ImportExportModelAdmin):

    list_display = ('title', 'type', 'application', 'finalized')
    list_filter = ('type', 'application', 'finalized', 'user', 'final_user')
