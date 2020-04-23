from django.urls import path

from apps.wiki_module.views import WikiDashboard


urlpatterns = [
    path('dashboard/', WikiDashboard.as_view(), name='wiki_dashaboard'),
    #path('new/', CreateApplication.as_view(), name='new'),
]
