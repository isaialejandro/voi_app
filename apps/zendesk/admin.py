from django.contrib import admin

from apps.zendesk.models import ZendeskUser, ZendeskUserHistory

admin.site.register(ZendeskUser)
admin.site.register(ZendeskUserHistory)