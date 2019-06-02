from django.urls import path

from apps.import_export.views import Dashboard


urlpatterns = [
	path('dashboard/', Dashboard.as_view(), name='import_export_dashboard'),

]