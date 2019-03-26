from django.urls import path, include

from apps.sox.views import SoxList, CreateSOX

urlpatterns = [
    path('list/', SoxList.as_view(),name='list'),
    path('new/', CreateSOX.as_view(),name='new'),
]