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

from django.urls import path, include

from django.apps import apps

from django.shortcuts import render

from django.conf import settings
from django.conf.urls.static import static

from django.views.generic import View

from braces.views import LoginRequiredMixin

from apps.tools.decorators import NeverCacheMixin, CSRFExemptMixin


application = apps.get_app_config('application').verbose_name
user = apps.get_app_config('user').verbose_name
bi_modules = apps.get_app_config('bi_modules').verbose_name
bajas_semanales = apps.get_app_config('bajas_semanales').verbose_name
zendesk = apps.get_app_config('zendesk').verbose_name
tools = apps.get_app_config('tools').verbose_name



class Dashboard(NeverCacheMixin, CSRFExemptMixin, LoginRequiredMixin, View):

    def get(self, request):
        #user = request.user
        context = {}
        context['dashboard'] = True
        return render(request, 'index.html', context)


urlpatterns = [
    path('c4r0nt3/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),

    path('dashboard/', Dashboard.as_view(), name='dashboard'),
    path('application/', include(('apps.application.urls', application), namespace='application')),
    path('bi_modules/', include(('apps.bi_modules.urls', bi_modules), namespace='bi_modules')),
    path('bajas/', include(('apps.bajas_semanales.urls', bajas_semanales), namespace='bajas_semanales')),
    path('zendesk/', include(('apps.zendesk.urls', zendesk), namespace='zendesk')),
    path('tools/', include(('apps.tools.urls', zendesk), namespace='tools')),

    path('api-auth/', include('rest_framework.urls')),
    path('bajas_semanales-api-v1/', include(('apps.bajas_semanales.api.v1.urls', bajas_semanales), namespace='bajas-semanales-api-v1')),
    path('bi_modules-api-v1/', include(('apps.bi_modules.api.v1.urls', bi_modules), namespace='bi_modules-api-v1')),
    path('zendesk-api-v1/', include(('apps.zendesk.api.v1.urls', zendesk), namespace='zendesk-api-v1')),
    path('tools-api-v1/', include(('apps.tools.api.v1.urls', tools), namespace='tools-api-v1')),
] + static(settings.STATIC_URL,
    document_root=settings.STATIC_ROOT) + \
    static(settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT)
