from django.urls import path

from apps.application.views import ApplicationList, CreateApplication


urlpatterns = [
    path('list/', ApplicationList.as_view(), name='list'),
    path('new/', CreateApplication.as_view(), name='new'),    
]