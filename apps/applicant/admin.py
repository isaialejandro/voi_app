from django.contrib import admin

from import_export.admin import ImportExportModelAdmin

from apps.applicant.models import Applicant

#admin.site.register(Applicant)
@admin.register(Applicant)
class ApplicantAdmin(ImportExportModelAdmin):

    list_display = (
        'first_name',
        'second_name',
        'first_lastname',
        'second_lastname',
        'email',
        'no_ambassador_boss',
        'id_ambassador_status',
        'id_station',
        'genere'
    )
