from django.urls import path, include

from apps.bi_modules.api.v1.views import MatchAcountFiles, AccountList


urlpatterns = [
    path('agg_local_amounts/', MatchAcountFiles.as_view(), name='agg_local_amounts'),
    path('account_list/', AccountList.as_view(), name='account_list'),
]
