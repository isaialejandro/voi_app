import datetime

from django.db import transaction

from django.shortcuts import render, render_to_response
from django.shortcuts import redirect

from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.urls import reverse_lazy
#from django.views.decorators.csrf import csrf_protect
from django.views import View
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.detail import DetailView

from braces.views import LoginRequiredMixin

from apps.tools.decorators import NeverCacheMixin, CSRFExemptMixin
from apps.ticket.models import Ticket, TicketHistory
from apps.application.models import Application
from apps.applicant.models import Applicant
from apps.ticket.forms import TicketForm, TicketUpdateForm, HistoryTicketForm


now = datetime.datetime.now()


class TicketDetail(NeverCacheMixin, CSRFExemptMixin, View):

    def get(self, request, *args, **kwargs):

        ticket_id = self.kwargs['pk']
        current_ticket = Ticket.objects.get(id=ticket_id)
        detail = TicketHistory.objects.filter(ticket_id=ticket_id).order_by('-registry_date')

        context = {}
        context['current_ticket'] = current_ticket
        context['ticket_detail'] = detail
        context['last_updated'] = TicketHistory.objects.last()
        return render(request, 'ticket_detail.html', context)


class NewTicket(NeverCacheMixin, CSRFExemptMixin, CreateView):


    def get(self, request):

        if request.user.is_authenticated:
            context = {}
            context['new_ticket'] = True
            context['form'] = TicketForm
            context['history_form'] = HistoryTicketForm
            context['application'] = Application.objects.filter(is_active=True,app_type='NORMAL')
            context['assigned_to'] = User.objects.filter(is_active=True,is_superuser=False).exclude(username='Pending')
            return render(request, 'ticket_form.html', context)
        else:
            return render(request, '404.html')

    @transaction.atomic
    def post(self, request):

        title = request.POST.get('title').upper()
        folio_no = request.POST.get('folio_number').upper()
        priority = request.POST.get('priority')
        status = request.POST.get('status')
        applicant = request.POST.get('applicant')
        application = request.POST.get('application')
        assigned_to = request.POST.get('assigned_to')
        request_type =request.POST.get('request_type')
        beneficiary_name = request.POST.get('beneficiary_name')
        beneficiary_last_name = request.POST.get('beneficiary_last_name')
        approval_owner = request.POST.get('approval_owner')
        approval_executor = request.POST.get('approval_executor')
        approve = request.POST.get('approve')
        created_by = request.POST.get('created_by')
        item_type = request.POST.get('item_type')
        path = request.POST.get('path')
        desc = request.POST.get('description')
        is_active = True

        summary_data = request.POST.get('summary')

        if Ticket.objects.filter(title = title):

            msg = 'Title ticket ' + title + ' already exist. Reassign the user again'
            messages.error(request, msg)

            f = TicketForm(
                    initial={
                        'title': title,
                        'folio_number': folio_no,
                        'priority': priority,
                        'status': status,
                        'applicant': applicant,
                        'application': application,
                        'assigned_to': assigned_to,
                        'request_type': request_type,
                        'beneficiary_name': beneficiary_name,
                        'beneficiary_last_name': beneficiary_last_name,
                        'approval_owner': approval_owner,
                        'approval_executor': approval_executor,
                        'approve': approve,
                        'created_by': created_by,
                        'item_type': item_type,
                        'path': path,
                        'description': desc,
                        }
                )
            h = HistoryTicketForm(initial={'summary': summary_data})

            context = {}
            context['new_ticket'] = True
            context['form'] = f
            context['history_form'] = h
            context['assigned_to'] = User.objects.filter(is_active=True,is_superuser=False).exclude(username='Pending')
            return render(request, 'ticket_form.html', context)

        elif Ticket.objects.filter(folio_number = folio_no):

            msg = 'Folio ticket ' + folio_no + ' already exist!'
            messages.error(request, msg)

            f = TicketForm(
                    initial={
                        'title': title,
                        'folio_number': folio_no,
                        'priority': priority,
                        'status': status,
                        'applicant': applicant,
                        'application': application,
                        'assigned_to': assigned_to,
                        'request_type': request_type,
                        'beneficiary_name': beneficiary_name,
                        'beneficiary_last_name': beneficiary_last_name,
                        'approval_owner': approval_owner,
                        'approval_executor': approval_executor,
                        'approve': approve,
                        'created_by': created_by,
                        'item_type': item_type,
                        'path': path,
                        'description': desc
                        }
                )
            h = HistoryTicketForm(initial={'summary': summary_data})

            context = {}
            context['form'] = f
            context['history_form'] = h
            return render(request, 'ticket_form.html', context)
        else:
            new_ticket = Ticket(
                title = title,
                folio_number = folio_no,
                priority = priority,
                status = status,
                applicant = Applicant.objects.get(id=applicant),
                application = Application.objects.get(id=application),
                assigned_to = User.objects.get(id=assigned_to),
                request_type = request_type,
                beneficiary_name =beneficiary_name,
                beneficiary_last_name = beneficiary_last_name,
                approval_owner = approval_owner,
                approval_executor = approval_executor,
                approve = approve,
                created_by = created_by,
                item_type = item_type,
                path = path,
                description=desc,
                is_active = True,
                user = User.objects.get(id=request.user.id)
            )
            new_ticket.save()

            hist = TicketHistory(
                ticket = Ticket.objects.get(id=new_ticket.id),
                #sox = ,
                summary = 'Ticket CREATION with status: ' + new_ticket.status.upper(),
                registry_date = now,
                update = False,
                not_finished_type = True,
                user = User.objects.get(id=request.user.id)
            )

            hist.save()

            messages.success(request, 'Ticket ' + new_ticket.folio_number + ' created successfully')
        return HttpResponseRedirect('/')


class UpdateTicket(NeverCacheMixin, CSRFExemptMixin, View):

    def get(self, request, pk):
        context = {}
        context['update_ticket'] = True
        context['application'] = Application.objects.filter(is_active=True,app_type='NORMAL')

        current_ticket = Ticket.objects.get(id=pk)

        priority = current_ticket.priority
        applicant = current_ticket.applicant
        application = current_ticket.application
        assigned_to = current_ticket.assigned_to
        request_type = current_ticket.request_type
        ben_name = current_ticket.beneficiary_name
        ben_last_name = current_ticket.beneficiary_last_name
        app_owner = current_ticket.approval_owner
        app_executor = current_ticket.approval_executor
        approve = current_ticket.approve
        created_by = current_ticket.created_by
        item_type = current_ticket.item_type
        path = current_ticket.path
        desc = current_ticket.description

        f = TicketUpdateForm(
            initial={
                'priority': priority,
                'applicant': applicant,
                'aplication': application,
                'assigned_to': assigned_to,
                'request_type': request_type,
                'beneficiary_name': ben_name,
                'beneficiary_last_name': ben_last_name,
                'approval_ownner': app_owner,
                'approval_executor': app_executor,
                'approve': approve,
                'created_by': created_by,
                'item_type': item_type,
                'path': path,
                'description': desc
                }
        )
        context['current_ticket'] = current_ticket
        context['form'] = f
        context['history_form'] = HistoryTicketForm
        return render(request, 'ticket_form.html', context)

    @transaction.atomic
    def post(self, request, pk):

        ticket_id = pk
        current_user = User.objects.get(id=self.request.user.id)

        prior = request.POST.get('priority')
        applicant = request.POST.get('applicant')
        application = request.POST.get('application')
        assigned_to = request.POST.get('assigned_to')
        request_type = request.POST.get('request_type')
        ben_name = request.POST.get('beneficiary_name')
        ben_last_name = request.POST.get('beneficiary_last_name')
        app_owner = request.POST.get('approval_owner')
        app_executor = request.POST.get('approval_executor')
        approve = request.POST.get('approve')
        created_by = request.POST.get('created_by')
        item_type = request.POST.get('item_type')
        path = request.POST.get('path')
        desc = request.POST.get('description')

        #Falta validación de Actualización
        update = Ticket.objects.get(id=ticket_id)
        update.priority=prior
        update.applicant=Applicant.objects.get(id=applicant)
        update.appplication=Application.objects.get(id=application)
        update.assigned_to=current_user
        update.request_type=request_type
        update.beneficiary_name=ben_name
        update.beneficiary_last_name=ben_last_name
        update.approval_owner=app_owner
        update.approval_executor=app_executor
        update.approve=approve
        update.created_by=created_by
        update.item_type=item_type
        update.path=path
        update.description=desc

        update.save()

        #history
        summary = request.POST.get('summary')
        history = TicketHistory(
            ticket = Ticket.objects.get(id=ticket_id),
            registry_date=now,
            update=True,
            user = current_user,
            summary = summary.capitalize()
        )
        history.save()

        msg = 'Ticket ' + update.folio_number + ' updated successfully'
        messages.success(request, msg)
        return HttpResponseRedirect('/dashboard/')
