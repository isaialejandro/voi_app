from django.contrib import admin

from apps.extra_incidents.models import ExtraIncident

from apps.tools.mixins.admin_mixins import ExportCSVMixin


@admin.register(ExtraIncident)
#class ExtraIncidentAdmin(admin.ModelAdmin, ExportCSVMixin):
class ExtraIncidentAdmin(admin.ModelAdmin):

    list_display = ('title', 'type', 'application', 'finalized')
    list_filter = ('type', 'application', 'finalized', 'user', 'final_user')
    #actions = ['export_as_csv']


#admin.site.register(ExtraIncident)
