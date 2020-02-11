from django.shortcuts import render

from django.contrib import messages
from django.contrib.auth.models import User

from django.db import transaction

from django.urls import reverse_lazy

from django.utils import timezone

from django.views.generic import ListView
from django.views.generic.edit import CreateView

from django.http import HttpResponseRedirect

from django.shortcuts import render

from apps.application.models import Application

from braces.views import LoginRequiredMixin

from apps.bajas_semanales.models import BajaSemanal
from apps.bajas_semanales.forms import BajaSemanalForm
from apps.tools.decorators import NeverCacheMixin, CSRFExemptMixin,\
 PermissionRequiredMixin

now = timezone.now()


class BajasSemanalesList(NeverCacheMixin, CSRFExemptMixin, LoginRequiredMixin, ListView):

    model = BajaSemanal
    template_name = 'bajas_semanales_list.html'

    def get_context_data(self, **kwargs):
        context = super(BajasSemanalesList, self).get_context_data(**kwargs)
        context['bajas_semanales_list'] = True
        context['bajas'] = BajaSemanal.objects.order_by('-created_date')
        return context

class CreateBajaSemanal(NeverCacheMixin, CSRFExemptMixin, LoginRequiredMixin, CreateView):

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
                type = type,
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
            return HttpResponseRedirect(reverse_lazy('bajas_semanales:list'))
