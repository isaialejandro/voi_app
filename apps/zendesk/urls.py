from django.urls import path, include

from apps.zendesk.views import ActiveUsersHist

urlpatterns = [
    path('active_users', ActiveUsersHist.as_view(), name='active_users'),
]