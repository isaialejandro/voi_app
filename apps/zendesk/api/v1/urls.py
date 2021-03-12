from django.urls import path, include

from apps.zendesk.api.v1.views import GetActiveUsersAPI, ExportUserAPI, GetTickets


urlpatterns = [
    path('get_active_users', GetActiveUsersAPI.as_view(), name='get_active_users'),
    path('export_users', ExportUserAPI.as_view(), name='export_users'),
    
    path('get_range_tickets', GetTickets.as_view(), name='get_range_tickets'),
]