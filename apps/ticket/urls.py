from django.urls import path

from apps.ticket.views import NewTicket, TicketDetail, UpdateTicket

urlpatterns = [
   path('new/', NewTicket.as_view(), name='new'),
   path('detail/<int:pk>/', TicketDetail.as_view(), name='detail'),
   path('update/<int:pk>/', UpdateTicket.as_view(), name='update'),
]
