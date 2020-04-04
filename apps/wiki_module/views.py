from django.shortcuts import render

from django.contrib import messages
from django.contrib.auth.models import User

from django.db import transaction

from django.urls import reverse_lazy

from django.utils import timezone


class WikiDashboard(View):

    def get(request):
        context = {}
        context['dashboard'] = True
    return render(request 'wiki-dashboard.html', context)
