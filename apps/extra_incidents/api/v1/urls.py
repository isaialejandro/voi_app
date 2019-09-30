from django.urls import path

from apps.extra_incidents.api.v1.views import FinalizeIncident

urlpatterns = [
    path('finalize/', FinalizeIncident.as_view(), name='finalize'),
]
