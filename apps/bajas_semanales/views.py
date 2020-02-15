from django.shortcuts import render

from django.contrib import messages
from django.contrib.auth.models import User

from django.db import transaction

from django.urls import reverse_lazy

from django.utils import timezone

from django.views.generic import ListView
from django.views.generic.edit import CreateView, View

from django.http import HttpResponseRedirect

from django.shortcuts import render

from apps.application.models import Application

from braces.views import LoginRequiredMixin

from apps.bajas_semanales.models import TipoBaja, BajaSemanal
from apps.bajas_semanales.forms import BajaSemanalForm, TipoBajaForm
from apps.tools.decorators import NeverCacheMixin, CSRFExemptMixin,\
 PermissionRequiredMixin

now = timezone.now()


class TipoBajaList(NeverCacheMixin, CSRFExemptMixin, LoginRequiredMixin, ListView):

    model = TipoBaja
    template_name = 'tipo_bajas_list.html'

    def get_context_data(self, **kwargs):
        context = super(TipoBajaList, self).get_context_data(**kwargs)
        context['tipo_bajas_list'] = True
        context['tipo_bajas'] = TipoBaja.objects.filter(is_active=True)
        context['count'] = TipoBaja.objects.filter(is_active=True)
        return context


class CreateTipoBaja(NeverCacheMixin, CSRFExemptMixin, LoginRequiredMixin, CreateView):

    def get(self, request):
        context = {}
        context['new_tipo_baja'] = True
        context['form'] = TipoBajaForm()
        return render(request, 'bajas_semanales_form.html', context)

    @transaction.atomic
    def post(self, request):

        type = request.POST.get('type').title()

        if not TipoBaja.objects.filter(is_active=True, type=type):
            new = TipoBaja(
                type = type,
                created_date=now,
                is_active=True
            )
            new.save()
            msg = 'Tipo ' + new.type + ' saved successfully'
            messages.success(request, msg)
            return HttpResponseRedirect(reverse_lazy('bajas_semanales:tipo_bajas_list'))
        else:

            #context = {}
            #form = TipoBajaForm(initial = {'type': type})
            #context['form'] = form

            msg = 'Tipo ' + type + ' already exists, try with another one'
            messages.error(request, msg)
            return HttpResponseRedirect(reverse_lazy('bajas_semanales:create_tipo_baja'), context)


class BajasSemanalesList(NeverCacheMixin, CSRFExemptMixin, LoginRequiredMixin, ListView):

    model = BajaSemanal
    template_name = 'bajas_semanales_list.html'

    def get_context_data(self, **kwargs):
        context = super(BajasSemanalesList, self).get_context_data(**kwargs)
        context['bajas_semanales_list'] = True
        context['bajas'] = BajaSemanal.objects.order_by('-created_date')
        context['count'] = BajaSemanal.objects.all()
        return context


class CreateBajaSemanal(NeverCacheMixin, CSRFExemptMixin, LoginRequiredMixin, CreateView):

    """
    Crea registro y aplicaciones.
    Puede crear multiples usuarios con sus respectivos id, todos relacionados al
     subject del registro.

    """

    def get(self, request):

        context = {}
        user = request.user
        if not user.has_perm('bajas_semanales.create_baja_semanal'):
            return render(request, '404.html', context)
        else:
            context['new_baja_semanal'] = True
            context['form'] = BajaSemanalForm(request.GET)
            context['application_list'] = Application.objects.filter(
                                            is_active=True,
                                            is_for_bajas_semanales=True
                                         )

            return render(request, 'bajas_semanales_form.html', context)

    @transaction.atomic
    def post(self, request, *args):

        type = request.POST.get('type')
        subject = request.POST.get('subject')
        user_code = request.POST.get('user_code')
        user_name = request.POST.get('user_name')
        request_date = request.POST.get('request_date')
        application_list = request.POST.getlist('application')

        if not BajaSemanal.objects.filter(user_code=user_code, user_name=user_name):

            new  = BajaSemanal(
                type = TipoBaja.objects.get(id=type),
                subject = subject,
                user_code = user_code.capitalize(),
                user_name = user_name.title(),
                request_date = request_date,
                created_date = now,
                user = User.objects.get(id=request.user.id)
            )
            new.save()

            for a in application_list:
                new.application.add(a)


            #Si el registro tiene todas las bajas marcar el "already checked"
            if new.application.all().count() == Application.objects.filter(
                                            is_active=True,
                                            is_for_bajas_semanales=True
                                        ).count():
                new.already_checked = True
                new.save()

            msg = 'Baja ' + subject + ' saved successfully'
            messages.success(request, msg)
            return HttpResponseRedirect(reverse_lazy('bajas_semanales:bajas_semanales_list'))


#Update es una API
