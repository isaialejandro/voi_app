from django.contrib import admin

# Register your models here.
from apps.application.models import Application, TresSesentaEnUnClick, Zendesk, \
OpCenter, NetTracer, SmartKargo, ZendeskGroup, ZendeskRol

admin.site.register(Application)
admin.site.register(TresSesentaEnUnClick)
admin.site.register(Zendesk)
admin.site.register(OpCenter)
admin.site.register(NetTracer)
admin.site.register(ZendeskGroup)
admin.site.register(ZendeskRol)
admin.site.register(SmartKargo)
