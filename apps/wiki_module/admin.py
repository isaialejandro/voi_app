from django.contrib import admin

from apps.wiki_module.models import BlogDoc, ArticleFile


admin.site.register(BlogDoc)
admin.site.register(ArticleFile)
