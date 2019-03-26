from django.contrib import admin

# Register your models here.
from apps.application.models import Application

admin.site.register(Application)
