from django.contrib import admin

from apps.wiki_module.models import AppDocument, Article


admin.site.register(AppDocument)
admin.site.register(Article)
