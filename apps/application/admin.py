from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

# Register your models here.
from apps.application.models import Application

"""
@admin.register(Application)
class ApplicationAdmin(ImportExportModelAdmin):

    list_display = ('name', 'app_type', 'is_active', 'is_for_bajas_semanales')
"""