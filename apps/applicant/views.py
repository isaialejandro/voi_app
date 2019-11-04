import datetime

from django.db import transaction

from django.urls import reverse_lazy

from django.http import HttpResponseRedirect

from django.shortcuts import render

from django.views.generic.edit import View


from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth.models import User

from apps.applicant.models import Applicant
from apps.applicant.forms import ApplicantForm

from apps.tools.decorators import NeverCacheMixin, CSRFExemptMixin

from braces.views import LoginRequiredMixin

now = datetime.datetime.now()

"""
class ApplicantList(View):

    def get(self, request):

        usr = request.POST.get('username')
        pwd = request.POST.get('password')

        user = authenticate(request, user= usr, password=pwd)

        if not request.user.is_authenticated:
            return render(request, '404.html')
        else:
            return render(request, 'list.html')
"""


class CreateApplicant(NeverCacheMixin, CSRFExemptMixin, View):

    def get(self, request):

        user = request.user

        if not user.has_perm('applicant.create_applicant'):
            return render(request, '404.html')
        else:
            context = {}
            context['new_applicant'] = True
            context['form'] = ApplicantForm
            return render(request, 'applicant_form.html', context)

    @transaction.atomic
    def post(self, request):

        first_name = request.POST.get('first_name')
        second_name = request.POST.get('second_name')
        last1 = request.POST.get('first_lastname')
        last2 = request.POST.get('second_lastname')
        email = request.POST.get('email')

        if Applicant.objects.filter(is_active=True, first_lastname=last1, second_lastname=last2):

            msg = 'Applicant ' + first + ' already exist!'
            messages.error(request, msg)

            form = ApplicantForm(
                initial = {
                    'first_name': first_name,
                    'second_name': second_name,
                    'first_lastname': last1,
                    'second_lastname': las2,
                    'email': email
                }
            )
            context = {}
            context['form'] = form
            return render(request, 'applicant_form.html', context)

        elif Applicant.objects.filter(is_active=True, email=email):

            msg = 'Applicant email ' + email + ' already exist!'
            messages.error(request, msg)

            form = ApplicantForm(
                initial = {
                    'first_name': first_name,
                    'second_name': second_name,
                    'first_lastname': last1,
                    'second_lastname': las2,
                    'email': email
                }
            )
            context = {}
            context['form'] = form
            return render(request, 'applicant_form.html', context)
        else:

            new = Applicant(
                first_name=first_name.capitalize(),
                second_name=second_name.capitalize(),
                first_lastname=last1.capitalize(),
                second_lastname=last2.capitalize(),
                registry_date=now,
                email=email,
                is_active=True,
                user=User.objects.get(id=request.user.id)
            )
            new.save()
            msg = 'Applicant ' + new.first_name + ' ' + new.first_lastname + ' saved successfully'
            messages.success(request, msg)

            user = request.user
            if not user.has_perm('applicant.view_applicant_list'):
                return HttpResponseRedirect(reverse_lazy('dashboard'))
            else:
                return HttpResponseRedirect(reverse_lazy('application:list'))
