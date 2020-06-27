import io
import json
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView
from rest_framework import authentication, permissions
from rest_framework.response import Response

from django.db import transaction
from django.contrib import messages
from django.contrib.auth.models import User

from django.http import JsonResponse

from apps.application.models import Application
from apps.bajas_semanales.models import TipoBaja, BajaSemanal

from apps.bajas_semanales.api.v1.serializers import BajaSemanalSerializer


#no se usa
class GetSelectsData(APIView):

    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = []

    def get_tipo_bajas_data(self, request, **kwargs):

        data = {'success': True}
        try:
            tipo_bajas_list = []

            for t in TipoBaja.objects.filter(is_active=True):
                tipo_bajas_list.append({
                    "id": a.id,
                    "text": a.name
                })

            data = tipo_bajas_list
        except Exception as r:
            data['success'] = False
            data['message'] = 'Error: ', str(r)
        return Response(data)


class RecheckBaja(APIView):

    """
    Actualiza el campo de apps,
    Guarda un detalle del usuario que actualizó, y que campos/apps ha actualizado.
    """

    #authentication_classes = [authentication.TokenAuthentication]
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, **kwargs):

        id = request.GET.get('id')
        print(id)
        detail = BajaSemanal.objects.get(uid=id)
        data = {'success': True}

        try:
            baja = []
            tipo_bajas_list = []
            app_list = []

            baja.append({
                "type": str(detail.type),
                "subject": detail.subject,
                "user_code": detail.user_code,
                "user_name": detail.user_name,
                "request_date": detail.request_date,
            })

            for t in TipoBaja.objects.filter(is_active=True):
                if t.id == detail.type.id:
                    tipo_bajas_list.append({
                        "id": t.id,
                        "text": t.type,
                        "selected": True,
                    })
                else:
                    tipo_bajas_list.append({
                        "id": t.id,
                        "text": t.type
                    })


            for x in detail.application.all():
                app_list.append({
                    "id": x.id,
                    "text": x.name,
                    "selected": True
                })
            for a in Application.objects.filter(is_active=True, is_for_bajas_semanales=True):
                if a.name not in [t['text'] for t in app_list]:
                    app_list.append({
                        "id": a.id,
                        "text": a.name,
                        "selected": False
                    })

            data['baja_semanal'] = baja
            data['tipo_bajas'] = tipo_bajas_list
            data['results'] = app_list
        except Exception as r:
            data['success'] = False
            data['message'] = 'Error: ', str(r)
        return Response(data)

    def post(self, request):

        data = {'success': True}
        try:
            if request.user.is_authenticated:

                update = BajaSemanal.objects.get(uid=request.POST.get('id'))

                type = request.POST.get('type')
                subject = request.POST.get('subject')
                user_code = request.POST.get('user_code')
                user_name = request.POST.get('user_name')
                request_date = request.POST.get('request_date')
                new_detail_app_list = request.POST.getlist('application[]')


                update.type=TipoBaja.objects.get(id=type)
                update.subject=subject
                update.user_code=user_code
                update.user_name=user_name
                update.request_date=request_date
                update.save()

                #Removing previous app to detail and adding new setted apps in detail.
                for a in update.application.all():
                    update.application.remove(a)
                for a in new_detail_app_list:
                    update.application.add(a)

                #Validate if detail app list has all required apps for bajas_semanales.
                #If so, can close record, if don´t, just kepps pending.
                a001_list = []
                for a in Application.objects.filter(is_active=True, is_for_bajas_semanales=True):
                    a001_list.append(a)
                if len(new_detail_app_list) > 0:
                    if len(new_detail_app_list) == len(a001_list):
                            update.already_checked = True

                update.last_user_update=User.objects.get(id=request.user.id)
                update.save()

                msg = 'Baja ' + update.user_code + ' updated successfully'
                msg_01 = 'Baja ' + update.user_code + ' already checked'
                messages.success(request, msg)

                data['updated'] = msg
                data['already_checked'] = msg_01
                data['current_detail_status'] = update.already_checked
            else:
                data['success'] = False
                data['message'] = 'Cannot identify authenticated user..'
        except Exception as t:
            data['success'] = False
            data['message'] = 'Error: ', str(t)
        return Response(data)
