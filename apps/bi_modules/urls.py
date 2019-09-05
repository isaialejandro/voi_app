from django.urls import path

from apps.bi_modules.views import IngresosYCuentasPorCobrarView

urlpatterns = [
    path('cuentas_por_cobrar/', IngresosYCuentasPorCobrarView.as_view(), name='cuentas_por_cobrar_dashboard'),
    #path(),
    #path(),

]
