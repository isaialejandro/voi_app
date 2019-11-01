import datetime

from django.db import transaction

from django.http import HttpResponseRedirect

from django.shortcuts import render

from django.contrib import messages
from django.contrib.auth import authenticate

from django.contrib.auth.models import User

from django.contrib.auth.mixins import PermissionRequiredMixin

from django.views.generic.edit import View

from apps.application.models import Application

from apps.sox.models import SOXRegistry, SoxHistory
from apps.sox.forms import SOXForm

from braces.views import LoginRequiredMixin

from apps.tools.decorators import NeverCacheMixin, CSRFExemptMixin


now = datetime.datetime.now()


class SoxList(NeverCacheMixin, CSRFExemptMixin, PermissionRequiredMixin, View):

    permission_required = ('sox.view_sox_list', 'sox.disable_sox' )

    def get(self, request):

        usr = request.POST.get('username')
        pwd = request.POST.get('password')

        if not request.user.is_authenticated:
            return render(request, '404.html')
        else:
            context = {}
            context['sox_list'] = True
            context['sox_registries'] = SOXRegistry.objects.filter(is_active=True)
            return render(request, 'sox_list.html', context)


class CreateSOX(NeverCacheMixin, CSRFExemptMixin, PermissionRequiredMixin, View):

    permission_required = 'sox.create_sox'

    def get(self, request):

        if request.user.is_authenticated:

            context = {}
            context['form'] = SOXForm
            context['new_sox'] = True
            context['sox_applications'] = Application.objects.filter(is_active=True, app_type='SOX')
            context['executor'] = User.objects.filter(is_active=True,is_superuser=False).exclude(username='Pending')
            context['1st_2nd_source_executor'] = User.objects.filter(is_active=True,is_superuser=False)
            return render(request, 'sox_form.html', context)
        else:
            return render(request, '404.html')

    @transaction.atomic
    def post(self, request):

        folio = request.POST.get('folio_number').upper()
        app = request.POST.get('application')
        req_type = request.POST.get('request_type')
        affected_user = request.POST.get('affected_user')
        executor = request.POST.get('executor')
        exec_date = request.POST.get('date_1')
        status = request.POST.get('status')
        sent_email_to_exec = request.POST.get('sent_email_to_exec')
        confirmed_by_exec = request.POST.get('confirmed_by_exec')
        exec_conf_date = request.POST.get('date_2')
        first_source = request.POST.get('first_source')
        first_source_date = request.POST.get('date_3')
        first_source_exec = request.POST.get('first_source_executor')
        second_source = request.POST.get('second_source')
        second_source_date = request.POST.get('date_4')
        second_source_exec = request.POST.get('second_source_executor')


        if SOXRegistry.objects.filter(is_active=True, folio_number=folio):

            context = {}
            context['executor'] = User.objects.filter(is_active=True,is_superuser=False).exclude(username='Pending')
            context['1st_2nd_source_executor'] = User.objects.filter(is_active=True,is_superuser=False)

            """
            se necesita traer el usuario seleccionado inicialmente si el form se
            reconstruye por alguna validación.

            executr = User.objects.get(id=first_source_exec)
            context['1st_2nd_source_executor'] = SOXForm(
                initial = {
                    'executor': executor,
                    'first_source_executor': executr.username,
                    'second_source_executor': second_source_exec
                }
            )
            """
            context['form'] = SOXForm(
                initial = {

                    'folio_number': folio,
                    'application': app,
                    'request_type': req_type,
                    'affected_user': affected_user,
                    'executor': executor,
                    'execution_date': exec_date,
                    'status': status,
                    'sent_email_to_exec': sent_email_to_exec,
                    'confirmed_by_exec': confirmed_by_exec,
                    'exec_confirmed_date': exec_conf_date,
                    'first_source': first_source,
                    'first_source_date': first_source_date,
                    'first_source_executor': first_source_exec,
                    'second_source': second_source,
                    'second_source_date': second_source_date,
                    'second_source_executor': second_source_exec
                }
            )
            msg = 'Folio number ' + folio + ' already exist. Select again the follow fields: *Executor. \n *1rst Source Executor.\n*Second Source Executor'

            messages.error(request, msg)
            return render(request, 'sox_form.html', context)
        else:
            if exec_date == '':
                exec_date = None
            if exec_conf_date == '':
                exec_conf_date = None
            if first_source_date == '':
                first_source_date = None
            if second_source_date == '':
                second_source_date = None

            new = SOXRegistry(
                folio_number = folio,
                application = Application.objects.get(id=app),
                request_type = req_type,
                affected_user = affected_user,
                executor = User.objects.get(id=executor),
                execution_date = exec_date,
                status = status,
                sent_email_to_exec = sent_email_to_exec,
                confirmed_by_exec = confirmed_by_exec,
                exec_confirmed_date = exec_conf_date,
                first_source = first_source,
                first_source_date = first_source_date,
                first_source_executor = User.objects.get(id=first_source_exec),
                second_source = second_source,
                second_source_date = second_source_date,
                second_source_executor = User.objects.get(id=second_source_exec),
                registry_date = now,
                is_active = True,
                user = User.objects.get(id=request.user.id)
            )
            new.save()

            hist = SoxHistory(
                sox = SOXRegistry.objects.get(id=new.id),
                registry_date=now,
                update=False,
                user=User.objects.get(id=request.user.id)
            )
            hist.save()
        msg = 'SoxReg ' + new.folio_number + ' saved successfully'
        messages.success(request, msg)
        return HttpResponseRedirect('/sox/list/')



class UpdateSox(NeverCacheMixin, CSRFExemptMixin, PermissionRequiredMixin, View):

    permission_required = 'sox.update_sox'

    def get(self, request):
        context = {}
        context['update_sox '] = True
        return render(request, 'sox_form.html')

    def post(self, request):

        current_sox = Sox.objects.get(id=request.GET.get('id'))

        folio_number = request.POST.get()
        application = request.POST.get()
        request_type = request.POST.get()
        affected_user = request.POST.get()
        executor = request.POST.get()
        execution_date = request.POST.get()
        status = request.POST.get()

        sent_email_to_exec = request.POST.get()
        confirmed_by_exec = request.POST.get()
        exec_confirmed_date = request.POST.get()

        first_source = request.POST.get()
        first_source_date = request.POST.get()
        first_source_executor = request.POST.get()

        second_source = request.POST.get()
        second_source_date = request.POST.get()
        second_source_executor = request.POST.get()

        registry_date = request.POST.get()
        is_active = request.POST.get()
        user = request.POST.get()
