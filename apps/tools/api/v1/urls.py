from django.urls import path

from apps.tools.api.v1.views import FileAPI


urlpatterns = [
    path('tools-api-v1/export', FileAPI.as_view(), name='download_file'),
]