from django.contrib import admin

# Register your models here.
from apps.applicant.models import Applicant

admin.site.register(Applicant)