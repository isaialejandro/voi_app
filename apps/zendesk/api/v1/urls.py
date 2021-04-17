from django.urls import path, include

from apps.zendesk.api.v1.views import GetActiveUsersAPI, ExportUserAPI, GetTickets, \
    StructureTicket


urlpatterns = [
    path('user/users', GetActiveUsersAPI.as_view(), name='get_users'),
    path('user/export', ExportUserAPI.as_view(), name='export_users'),
    path('ticket/tickets', GetTickets.as_view(), name='tickets'),
    path('ticket/structure', StructureTicket.as_view(), name='structure'),
]