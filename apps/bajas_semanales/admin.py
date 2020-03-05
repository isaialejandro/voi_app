from django.contrib import admin

from apps.bajas_semanales.models import TipoBaja, BajaSemanal

# Register your models here.
@admin.register(TipoBaja)
class TipoBajaAdmin(admin.ModelAdmin):

    list_display = ('type', 'created_date', 'is_active')

admin.site.register(BajaSemanal)
