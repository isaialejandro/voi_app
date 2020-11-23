from django.urls import path, include

from apps.zendesk.api.v1.views import GetActiveUsersAPI


urlpatterns = [
    path('get_active_users', GetActiveUsersAPI.as_view(), name='get_active_users'),
]