import datetime

from django.db import transaction

from django.contrib.auth.models import User

from django.contrib.auth import authenticate
from django.contrib import messages

from django.http import HttpResponseRedirect

from django.shortcuts import render

from django.urls import reverse_lazy

from django.views.generic.edit import CreateView, View
from django.views.generic.list import ListView

from apps.application.models import Application
from apps.application.forms import ApplicationForm

from apps.applicant.models import Applicant

from apps.tools.decorators import NeverCacheMixin, CSRFExemptMixin

from braces.views import LoginRequiredMixin

now = datetime.datetime.now()


"""
class ApplicationList(NeverCacheMixin, CSRFExemptMixin, ListView):

    model = Application
    template_name='list.html'
    paginate_by = 3  # if pagination is desired

    def get_context_data(self, **kwargs):

        usr = self.request.POST.get('username')
        pwd = self.request.POST.get('password')

        user = authenticate(request, user= usr, password=pwd)

        if not request.user.is_authenticated:
            return render(request, '404.html')
        else:
            context = super().get_context_data(**kwargs)
            context['applications'] = Application.objects.filter(is_active=True)
            context['applicants'] = Applicant.objects.filter(is_active=True)
            return context    
"""

class ApplicationList(NeverCacheMixin, CSRFExemptMixin, View):

    model = Application
    template_name='list.html'
    paginate_by = 3  # if pagination is desired, not working for now.

    def get(self, request):

        usr = self.request.POST.get('username')
        pwd = self.request.POST.get('password')

        user = authenticate(request, user= usr, password=pwd)

        if not request.user.is_authenticated:
            return render(request, '404.html')
        else:
            context = {}
            context['applications'] = Application.objects.filter(is_active=True)
            context['applicants'] = Applicant.objects.filter(is_active=True)
            return render(request, 'list.html', context)


class CreateApplication(NeverCacheMixin, CSRFExemptMixin, View):


    def get(self, request):

        usr = request.POST.get('username')
        pwd = request.POST.get('password')

        user = authenticate(request, user=usr, password=pwd)

        if not request.user.is_authenticated:
            return render(request, '404.html')
        else:
            context = {}
            context["new_app"] = True
            context['form'] = ApplicationForm
            return render(request, 'application_form.html', context)

    @transaction.atomic  
    def post(self, request):

        name = request.POST.get('name').upper()
        app_type = request.POST.get('app_type')

        if Application.objects.filter(is_active=True, name=name):

            msg = 'Application name ' + name + ' already exist!'
            messages.error(request, msg)

            return HttpResponseRedirect(reverse_lazy('application:new'))
        else:

            new_app = Application(
                name=name,
                registry_date=now,
                app_type=app_type,
                is_active=True,
                user=User.objects.get(id=request.user.id)
            )
            new_app.save()

            msg = 'Application ' + name + ' saved successfully'
            messages.success(request, msg)

            return HttpResponseRedirect(reverse_lazy('application:list'))