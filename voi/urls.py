"""voi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth import authenticate
from django.contrib.auth.models import Permission, User

from django.urls import path, include

from django.apps import apps

from django.shortcuts import render

from django.views.generic import View, TemplateView

from braces.views import LoginRequiredMixin

from apps.ticket.models import Ticket


ticket = apps.get_app_config('ticket').verbose_name
application = apps.get_app_config('application').verbose_name
applicant = apps.get_app_config('applicant').verbose_name
sox = apps.get_app_config('sox').verbose_name
user = apps.get_app_config('user').verbose_name
import_export = apps.get_app_config('import_export').verbose_name
bi_modules = apps.get_app_config('bi_modules').verbose_name


class Dashboard(View):

    def get(self, request):

        usr = request.POST.get('username')
        pwd = request.POST.get('password')

        user = authenticate(request, user=usr, password=pwd)

        if not request.user.is_authenticated:
            return render(request, '404.html')

        else:
            context = {}
            context['dashboard'] = True
            context['pending_tickets'] = Ticket.objects.filter(is_active=True)

            permissions = Permission.objects.filter(user=request.user.id)
            print('Current user permssions from Dashboard View: ', permissions,', ', request.user.id)

            return render(request, 'index.html', context)


urlpatterns = [
    path('c4r0nt3/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),

    path('', Dashboard.as_view(), name='dashboard'),
    path('tickets/', include(('apps.ticket.urls', ticket), namespace='ticket')),
    path('application/', include(('apps.application.urls', application), namespace='application')),
    path('applicant/', include(('apps.applicant.urls', applicant), namespace='applicant')),
    path('sox/', include(('apps.sox.urls', sox), namespace='sox')),
    path('bi_modules/', include(('apps.bi_modules.urls', bi_modules), namespace='bi_modules')),

    path('api-auth/', include('rest_framework.urls')),
    path('tickets-api-v1/', include(('apps.ticket.api.v1.urls', ticket), namespace='ticket-api-v1')),
]
