from django.contrib import admin

from apps.bajas_semanales.models import TipoBaja, BajaSemanal

# Register your models here.
admin.site.register(TipoBaja)
admin.site.register(BajaSemanal)
