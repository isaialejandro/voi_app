from django.urls import path

from apps.bajas_semanales.api.v1.views import GetSelectsData, RecheckBaja


urlpatterns = [
    path('get_apps/', GetSelectsData.as_view(), name='get_apps'),
    path('recheck/', RecheckBaja.as_view(), name='recheck_baja'), #get/post
]
