from django.shortcuts import render

from django.contrib import messages
from django.contrib.auth.models import User

from django.db import transaction

from django.urls import reverse_lazy

from django.utils import timezone

from django.views import View
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.detail import DetailView


class WikiDashboard(View):

    def get(self, request):
        context = {}
        context['dashboard'] = True
        return render(request, 'wiki_dashboard.html', context)
