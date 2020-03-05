import datetime

from django.db import transaction
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.models import User

from rest_framework.views import APIView
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from apps.ticket.models import Ticket, TicketHistory

from apps.tools.decorators import LoginRequiredMixin, NeverCacheMixin, CSRFExemptMixin


now = datetime.datetime.now()


class CloseCurrentTicket(NeverCacheMixin, CSRFExemptMixin, APIView):

    #authentication_classes = []
    #permission_classes = []

    @transaction.atomic
    def post(self, request):

        data = {"success": True}

        ticket = Ticket.objects.get(id=request.POST.get('id'))

        try:
            ticket.status='closed'
            ticket.solution_date=now
            ticket.is_active=False

            #Ticket History
            close_comment = request.POST.get('close_comment')

            hist = TicketHistory(
                ticket=ticket,
                summary= close_comment,
                registry_date=now,
                update=False,
                finished=True,
                user=User.objects.get(id=request.POST.get('user_id'))
            )
            ticket.save()
            hist.save()
            data['title'] = 'Ticket close successfully.'
            data['message'] = 'Ticket ' + ticket.folio_number + ' closed';
            data['button'] = '<button id="btn_modal_back_close" ' + \
                             'class="btn btn-sm btn-success pull-right' + \
                             'm-t-n-xs" data-dismiss="modal" type="button">' + \
                             '<strong>Close</strong></button>'
        except Exception as f:
            data['success'] = False
            data['message'] = 'Error trying to close the ticket ' + ticket.folio_number + \
                              '. Please contact with the administrator: \n' + \
                              str(f);
        except Ticket.DoesNotExist():
            data['success'] = False
            data['message'] = 'Ticket '+ ticket.folio_number +' does not exist.';
        return Response(data)
