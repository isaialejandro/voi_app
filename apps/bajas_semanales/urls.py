from django.urls import path

from apps.bajas_semanales.views import TipoBajaList, CreateTipoBaja, BajasSemanalesList, CreateBajaSemanal


urlpatterns = [
    path('tipo_bajas_list/', TipoBajaList.as_view(), name='tipo_bajas_list'),
    path('create_tipo_baja/', CreateTipoBaja.as_view(), name='create_tipo_baja'),
    path('list/', BajasSemanalesList.as_view(), name='bajas_semanales_list'),
    path('new/', CreateBajaSemanal.as_view(), name='new'),
   #path('update/<int:pk>/', UpdateBaja.as_view(), name='update'),
]
