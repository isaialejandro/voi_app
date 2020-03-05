import datetime
from django.utils import timezone

from django.db import transaction
from django.contrib import messages
from django.contrib.auth.models import User

from rest_framework.views import APIView
from rest_framework import authentication, permissions
from rest_framework.response import Response

#from apps.tools.decorators import NeverCacheMixin, CSRFExemptMixin, PermissionRequiredMixin

from apps.extra_incidents.models import ExtraIncident


now = datetime.datetime.now()


class FinalizeIncident(APIView):

    """
    Change extra_incident status: Finalize it
    """

    #authentication_classes = [authentication.TokenAuthentication]
    #permission_classes = [permissions.IsAdminUser]

    @transaction.atomic
    def post(self, request, format=None):

        if request.method == 'POST':

            usr = User.objects.get(id=request.user.id)

            flag = request.POST.get('flag')
            e = ExtraIncident.objects.get(id=request.POST.get('id'))
            current_usr = User.objects.get(id=request.user.id)

            try:
                data = {"success": True}

                if flag == "1": #Finalize it

                    e.finalized=True
                    e.end_date=now
                    e.final_user=current_usr
                    #e.closed=True
                    e.save()

                    msg = 'Incident ' + e.title + ' finalized successfully'
                    messages.success(request, msg)
                    data['inc_number'] = e.title
                    data['success_msg'] = msg
                    return Response(data)
                    """
                    if flag == "2": #Closed

                        close_comment = request.POST.get('close_comment')

                        e.close_comment=close_comment
                        e.closed=True
                        e.end_date=now
                        e.final_user=current_usr
                        e.save()

                        msg = 'Incident ' + e.inc_number + ' closed successfully'
                        messages.success(request, msg)
                        return Response(data)
                    """
                else:
                    msg = 'Flag Error'
                    messages.error(request, msg)
                    return Response(data)
            except Exception as f:
                data['success'] = False
                data['message'] = f

            return Response(data)
