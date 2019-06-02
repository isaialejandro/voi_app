from django.shortcuts import render

from django.views.generic import View


class Dashboard(View):

	def get(self, request):
		context = {}
		context['import_export'] = True
		return render(request, 'import_export_dashboard.html', context)