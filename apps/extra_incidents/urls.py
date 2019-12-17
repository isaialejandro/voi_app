from django.urls import path

from apps.extra_incidents.views import ListView, CreateIncident, IncidentDetail, \
    UpdateExtraIncident


urlpatterns = [
    path('list/', ListView.as_view(), name='list'),
    path('create/', CreateIncident.as_view(), name='create'),
    path('update/<int:pk>/', UpdateExtraIncident.as_view(), name='update'),
    path('detail/<int:pk>/', IncidentDetail.as_view(), name='detail'),
]
