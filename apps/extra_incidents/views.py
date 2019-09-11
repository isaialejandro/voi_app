import datetime

from django.contrib import messages
from django.contrib.auth.models import User

from django.urls import reverse_lazy

from django.shortcuts import render

from django.http import HttpResponseRedirect

from django.views.generic import ListView
from django.views.generic.edit import CreateView, View

from braces.views import LoginRequiredMixin

from apps.tools.decorators import NeverCacheMixin, CSRFExemptMixin, PermissionRequiredMixin

from apps.extra_incidents.models import ExtraIncident
from apps.extra_incidents.forms import ExtraIncidentForm

from apps.application.models import Application

now = datetime.datetime.now()


class ListView(NeverCacheMixin, CSRFExemptMixin, LoginRequiredMixin, ListView):

    model = ExtraIncident
    context_object_name='extra_incidents'
    queryset=ExtraIncident.objects.filter(is_active=True)
    template_name='extra_incident_list.html'


class CreateIncident(NeverCacheMixin, CSRFExemptMixin, LoginRequiredMixin, CreateView):

    model = ExtraIncident
    form_class = ExtraIncidentForm
    #template_name = 'extra_incident_form.html'

    def get(self, request):
        context = {
            'new_incident': True,
            'form': ExtraIncidentForm(),
            'application_list': Application.objects.filter(is_active=True)
        }
        return render(request, 'extra_incident_form.html', context)

    """
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context = {
            'new_incident': True,
            'form': ExtraIncidentForm(),
            'application_list': Application.objects.filter(is_active=True)
        }
        return context
    """

    def post(self, request, *args):

        #form = ExtraIncidentForm(request.POST)

        app = request.POST.get('application')
        inc_no = request.POST.get('inc_number').upper()
        type = request.POST.get('type')
        exec_date = request.POST.get('date_1')
        end_date = request.POST.get('date_2')
        summary = request.POST.get('summary')
        extra_commnt = request.POST.get('extra_comments')
        inc_source = request.POST.get('inc_source')
        user =  request.user.id

        if not ExtraIncident.objects.filter(inc_number=inc_no):
            new = ExtraIncident(
                application=Application.objects.get(id=app),
                inc_number=inc_no,
                type=type,
                exec_date=exec_date,
                end_date=end_date,
                summary=summary,
                inc_source=inc_source,
                extra_comments=extra_commnt,
                user=User.objects.get(id=user)
            )
            new.save()

            msg = 'Incident ' + inc_no + ' saved successfully'
            messages.success(request, msg)
            return HttpResponseRedirect(reverse_lazy('extra_incidents:list'))
        else:
            msg = 'Incident ' + inc_no + ' already has been registered, try with another one'
            messages.success(request, msg)

            form = ExtraIncidentForm(
                initial = {
                    'application': app,
                    'inc_number': inc_no,
                    'type': type,
                    'exec_date': exec_date,
                    'end_date': end_date,
                    'summary': summary,
                    'extra_comments': extra_commnt,
                    'inc_source': inc_source
                }
            )
            context = {}
            context['form'] = form
            return render(request, 'extra_incident_form.html', context)

        """
        if form.is_valid():

            form.save(commit=False)

            msg = 'Incident ', form.cleaned_data['inc_number'], ' saved successfully.'
            messages.success(request, msg)
            return HttpResponseRedirect(reverse_lazy('extra_incidents:list'))
        else:
            f = form.cleaned_data
            print('ELSE: ', form.errors)


            form = ExtraIncidentForm(
                initial = {
                    'application': f['application'],
                    'inc_number': f['inc_number'],
                    'type': f['type'],
                    'exec_date': exec_date,
                    'end_date': end_date,
                    'summary': f['summary'],
                    'extra_comments': f['extra_comments'],
                    'inc_source': f['inc_source']
                }
            )
            context = {}
            context['form'] = form

            msg = str(form.errors)
            messages.error(request, msg)
            return render(request, 'extra_incident_form.html', context)
            """
