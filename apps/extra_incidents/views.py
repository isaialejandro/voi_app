import datetime
from datetime import timedelta
from datetime import time

from dateutil.relativedelta import relativedelta

from django.db import transaction
from django.urls import reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from django.contrib import messages
from django.contrib.auth.models import User

#from django.contrib.auth.mixins import PermissionRequiredMixin
from apps.tools.decorators import PermissionRequiredMixin

from django.urls import reverse_lazy

from django.shortcuts import render

from django.http import HttpResponseRedirect

from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, View
from django.views.generic.detail import DetailView

from braces.views import LoginRequiredMixin

from apps.tools.decorators import NeverCacheMixin, CSRFExemptMixin, PermissionRequiredMixin

from apps.extra_incidents.models import ExtraIncident
from apps.extra_incidents.forms import ExtraIncidentForm
from apps.extra_incidents.snippets import ExtraIncidentFilter
from apps.extra_incidents.choices import TYPE, REGISTRY, INC_SOURCE, PAPERLESS

from apps.application.models import Application
now = datetime.datetime.now()


class ListView(NeverCacheMixin, CSRFExemptMixin, LoginRequiredMixin, View):

    def get(self, request):

        user = request.user
        context = {}

        if user.has_perm('extra_incidents.view_extra_incident_list'):

            #---Pagination begins---#
            extra_incident_list = ExtraIncident.objects.filter(is_active=True).order_by('finalized')

            page = request.GET.get('page')
            paginator = Paginator(extra_incident_list, 100)
            try:
                extra_incidents = paginator.page(page)
            except PageNotAnInteger:
                extra_incidents = paginator.page(1)
            except EmptyPage:
                extra_incidents = paginator.page(paginator.num_pages)
            #---Pagination ends---#


            context['extra_incident_list'] = extra_incidents
            context['filter'] = ExtraIncidentFilter(request.GET)
            context['count'] = ExtraIncident.objects.all()
            context['incident_filter'] = ExtraIncidentFilter(self.request.GET, queryset=extra_incident_list)
            context['extra_incidents'] = True
            context['app'] = Application.objects.filter(is_active=True)
            context['type'] = TYPE
            context['source'] = INC_SOURCE
            context['user_creation'] = User.objects.filter(is_active=True)
            return render(request, 'extra_incident_list.html', context)
        else:
            return render(request, '404.html', context)


class CreateIncident(NeverCacheMixin, CSRFExemptMixin, LoginRequiredMixin, CreateView):

    model = ExtraIncident
    form_class = ExtraIncidentForm

    def get(self, request):

        context = {}
        user = request.user
        if not user.has_perm('extra_incidents.create_extra_incident'):
            return render(request, '404.html', context)
        else:
            context['new_incident'] = True
            context['form'] = ExtraIncidentForm()
            context['application_list'] = Application.objects.filter(is_active=True)

            return render(request, 'extra_incident_form.html', context)

    @transaction.atomic
    def post(self, request, *args):

        app = request.POST.get('application')
        title = request.POST.get('title').upper()
        type = request.POST.get('type')
        summary = request.POST.get('summary')
        inc_source = request.POST.get('inc_source')
        user =  request.user.id

        """
        if exec_date is None or exec_date == '':
            msg = 'Execution date is empty, please select a start date'
            messages.error(request, msg)
            form = ExtraIncidentForm(
                initial = {
                    'application': app,
                    'title': title,
                    'type': type,
                    'exec_date': exec_date,
                    'summary': summary,
                    'inc_source': inc_source
                }
            )
            context = {}
            context['form'] = form
            return render(request, 'extra_incident_form.html', context)
        """
        if not ExtraIncident.objects.filter(title=title):
            new = ExtraIncident(
                application=Application.objects.get(id=app),
                title=title,
                type=type,
                summary=summary,
                inc_source=inc_source,
                user=User.objects.get(id=user)
            )
            new.save()

            msg = 'Incident ' + title + ' saved successfully'
            messages.success(request, msg)
            return HttpResponseRedirect(reverse_lazy('extra_incidents:list'))
        else:
            msg = 'Incident ' + title + ' already has been registered, try with another one'
            messages.error(request, msg)

            form = ExtraIncidentForm(
                initial = {
                    'application': app,
                    'title': title,
                    'type': type,
                    'summary': summary,
                    'inc_source': inc_source
                }
            )
            context = {}
            context['form'] = form
            return render(request, 'extra_incident_form.html', context)


class UpdateExtraIncident(NeverCacheMixin, CSRFExemptMixin, LoginRequiredMixin, UpdateView):

    model = ExtraIncident
    template_name = 'extra_incident_form.html'
    form_class = ExtraIncidentForm
    success_url = reverse_lazy('extra_incidents:list')

    @transaction.atomic
    def form_valid(self, form):

        title = form.cleaned_data['title'].upper()
        app = form.cleaned_data['application']
        type = form.cleaned_data['type']
        summary = form.cleaned_data['summary']
        inc_source = form.cleaned_data['inc_source']

        inc_id = self.kwargs['pk']
        extra_incident = ExtraIncident.objects.filter(is_active=True, title=title).exclude(id=inc_id)

        #Falta validación para que title no se duplique.
        if not extra_incident:

            e_i = ExtraIncident.objects.filter(id=inc_id)
            e_i.title=title
            e_i.application=app
            e_i.type=type
            e_i.summary=summary
            e_i.inc_source=inc_source
            e_i.user=User.objects.get(id=self.request.user.id)

            e_i.update()
            msg = 'Incident ' + title + ' updated successfully'
            messages.success(self.request, msg)
            return super(UpdateExtraIncident, self).form_valid(form)
        else:

            form = ExtraIncidentForm(
                initial = {
                    'application': app,
                    'title': title,
                    'type': type,
                    'summary': summary,
                    'inc_source': inc_source
                }
            )
            context = {}
            context['form'] = form
            msg = 'Incident title ' + title + ' already exist, try with another one'
            messages.error(self.request, msg)
            return HttpResponseRedirect(reverse('extra_incidents:update', kwargs={'pk': inc_id}))


class IncidentDetail(NeverCacheMixin, CSRFExemptMixin, LoginRequiredMixin, View):

    def get(self, request, **kwargs):

        usr = User.objects.get(id=request.user.id)
        detail_id = kwargs.get('pk')

        context = {}
        context['pk'] = {'pk': detail_id}

        if usr.has_perm('extra_incidents.view_extra_incident_detail'):

            inc = ExtraIncident.objects.get(id=self.kwargs.get('pk'))

            #Cálculo para fecha de resolución
            if inc.end_date:
                """
                start_date = datetime.datetime.strptime(str(inc.created)[:19], "%Y-%m-%d %H:%M:%S").time()
                end_date = datetime.datetime.strptime(str(inc.end_date)[:19], "%Y-%m-%d %H:%M:%S").time()

                print(start_date , '\n', end_date)

                h = end_date.hour - start_date.hour
                m = end_date.minute - start_date.minute
                s = end_date.second - start_date.second
                resol_time = str(h) + ':' + str(m) + ':' + str(s)
                """

                created = datetime.datetime.strptime(str(inc.created)[:19], "%Y-%m-%d %H:%M:%S")
                print(datetime.datetime.now())
                finalized = inc.end_date

                sub_days = finalized + relativedelta(days=-created.day) #ready
                sub_months = finalized + relativedelta(months=-created.month) #ready
                #sub_years = finalized + relativedelta(years=-created.year) #not yet

                sub_hours = finalized + relativedelta(hours=-created.hour) #not yet
                sub_minutes = finalized + relativedelta(minutes=-created.minute) #not yet
                sub_seconds = finalized + relativedelta(seconds=-created.second) #not yet

                print('CURRENT HOUR: ', created)
                print('SUB HOUR:', sub_hours.hour)
                print('SUB DAYS:', sub_days.day)
                print('SUB MONTH', sub_months.month)

            else:
                resol_time = 'Inc has not end time.'
            #context['resol_time'] = resol_time
            context['detail'] = inc
            return render(request, 'incident_detail.html', context )
        else:
            return ListView.as_view()(request)
