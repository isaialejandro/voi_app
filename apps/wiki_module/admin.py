from django.contrib import admin

from apps.wiki_module.models import Tag, BlogDoc, ArticleFile


admin.site.register(Tag)
admin.site.register(BlogDoc)
admin.site.register(ArticleFile)
