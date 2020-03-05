from django.contrib import admin

# Register your models here.
from apps.application.models import Application, TresSesentaEnUnClick, Zendesk, \
OpCenter, NetTracer, SmartKargo, ZendeskGroup, ZendeskRol


@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):

    list_display = ('name', 'app_type', 'is_active', 'is_for_bajas_semanales')

admin.site.register(TresSesentaEnUnClick)
admin.site.register(Zendesk)
admin.site.register(OpCenter)
admin.site.register(NetTracer)
admin.site.register(ZendeskGroup)
admin.site.register(ZendeskRol)
admin.site.register(SmartKargo)
