from django.urls import path

from apps.bajas_semanales.views import BajasSemanalesList, CreateBajaSemanal


urlpatterns = [
   path('list/', BajasSemanalesList.as_view(), name='list'),
   path('new/', CreateBajaSemanal.as_view(), name='new'),
   #path('update/<int:pk>/', UpdateBaja.as_view(), name='update'),
]
