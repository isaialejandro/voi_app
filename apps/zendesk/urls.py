from django.urls import path, include

from apps.zendesk.views import Zendesk

urlpatterns = [
    path('active_users', Zendesk.as_view(), name='active_users'),
    
]