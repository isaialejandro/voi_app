from django.urls import path

from apps.extra_incidents.views import ListView, CreateIncident

urlpatterns = [
    path('list/', ListView.as_view(), name='list'),
    path('create/', CreateIncident.as_view(), name='create')
]
