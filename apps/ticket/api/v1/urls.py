from django.urls import path, include

from apps.ticket.api.v1.views import CloseCurrentTicket


urlpatterns = [
    path('close/', CloseCurrentTicket.as_view(), name='close_ticket'),
]
