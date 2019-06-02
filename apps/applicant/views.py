import datetime

from django.db import transaction

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

        usr = request.POST.get('username')
        pwd = request.POST.get('password')

        user = authenticate(request, user= usr, password=pwd)

        if not request.user.is_authenticated:
            return render(request, '404.html')
        else:
            context = {}
            context['new_applicant'] = True
            context['form'] = ApplicantForm
            return render(request, 'applicant_form.html', context)

    @transaction.atomic
    def post(self, request):

        first = request.POST.get('first_name')
        last = request.POST.get('last_name')
        email = request.POST.get('email')

        if Applicant.objects.filter(is_active=True, first_name=first, last_name=last):

            msg = 'Applicant ' + first + ' already exist!'
            messages.error(request, msg)

            form = ApplicantForm(
                initial = {
                    'first_name': first,
                    'last_name': last,
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
                    'first_name': first,
                    'last_name': last,
                    'email': email
                }
            )
            context = {}
            context['form'] = form
            return render(request, 'applicant_form.html', context)
        else:

            new = Applicant(
                first_name=first.capitalize(),
                last_name=last.capitalize(),
                registry_date=now,
                email=email,
                is_active=True,
                user=User.objects.get(id=request.user.id)
            )
            new.save()
            msg = 'Applicant ' + new.first_name + ' ' + new.last_name + ' saved successfully.'
            messages.success(request, msg)
        return HttpResponseRedirect('/application/list/')
