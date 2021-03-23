import sys, os
from itertools import groupby
from operator import itemgetter 
from datetime import datetime

from django.db import transaction

from django.views.generic.list import ListView, View
from django.contrib.auth.models import User

from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from dotenv import load_dotenv

from apps.zendesk.models import ZendeskUser

from apps.tools.http.services import GetAPI, GetZendeskUser, UserGroup, Export
from apps.zendesk.models import ZendeskUser, ZendeskUserHistory

load_dotenv()


now = datetime.now()

class GetActiveUsersAPI(APIView):

    authentication_classes = [ SessionAuthentication, BasicAuthentication ]
    permission_classes = [ IsAuthenticated ]

    @transaction.atomic
    def get(self, request):
        data = {}
        hist = None
        domain = os.getenv('ZENDESK_API_DOMAIN')
        path = os.getenv('ZENDESK_USERS_PATH')
        api_filter_query = os.getenv('ZENDESK_USERS_FILTER')
        final_user_list = None
        try:
            data_api = GetAPI(domain, path, api_filter=api_filter_query)
            json_response = data_api.get()
            get_user = GetZendeskUser(json_response)
            print('Getting User List . . .')
            user_list = get_user.get_user()

            print('Getting User Groups . . .')
            user_group = UserGroup(user_list, domain)
            final_user_list = user_group.get_user_group()
            
            hist = self.create_hist(final_user_list)
            for u in final_user_list:
                group = str(u['group(s)']).replace('[', '').replace("'", "").replace("]", "")
                zendeskUser = ZendeskUser(
                    user_id=u['id'],
                    name=u['name'],
                    email=u['email'],
                    role=u['role'],
                    group=group,
                    hist=ZendeskUserHistory.objects.get(id=hist.id)
                )
                zendeskUser.save()

            data['total_occupied'] = hist.total_occupied_licenses
            data['current_admins'] = hist.current_admins
            data['current_agents'] = hist.current_agents
            data['success'] = True
            data['message'] = final_user_list
            data['status_code'] = '200'
            return Response(data)
        except Exception as t:
            data['message'] = t
            print('Error trying to retrieve API: ', str(t))
    def create_hist(self, user_list):
        try:
            total_licenses = len(user_list)
            total_admins = []
            total_agents = []
            for u in user_list:
                for i in u.values():
                    total_admins.append( i if i == 'admin' else None )
                    total_agents.append( i if i == 'agent' else None )
            total_agents = [len(a) for a in total_agents if a == 'agent']
            total_admins = [len(a) for a in total_admins if a == 'admin']

            zendesk_hist = ZendeskUserHistory(
                total_occupied_licenses=total_licenses,
                current_admins=str(len(total_admins)),
                current_agents=str(len(total_agents)),
                exec_user=User.objects.get(id=self.request.user.id)
            )
            zendesk_hist.save()

            return zendesk_hist
        except Exception as g:
            print('Error trying to create History: ', g)
            return g

class ExportUserAPI(APIView):
    
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        data = {}
        final_user_list = []
        try:
            user_history = ZendeskUserHistory.objects.last()
            user_list = ZendeskUser.objects.filter(hist=user_history.id)
            c = 1
            for u in user_list:
                final_user_list.append({
                    'Name': u.name,
                    'Email': u.email,
                    'Role': u.role,
                    'Group(s)': u.group
                })
                c = c + 1
            filename = 'Active_Zendesk_usesrs_' + \
                datetime.now().strftime('%d-%m-%Y - %H.%m.%s') + '.csv'
            export = Export(final_user_list, filename)
            export.export_to_csv()
            data['success'] = True
            data['filename'] = filename
            data['message'] = 'File exported Successfully!'
        except Exception as f:
            data['message'] = str(f)
            print('EXC: ', f)
        return Response(data)


class GetTickets(APIView):

    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        """Return All tickets from date range."""
        
        domain = os.getenv('ZENDESK_API_DOMAIN')
        path = os.getenv('ZENDESK_TICKETS_PATH')
        #filter_query = os.getenv('ZENDESK_TICKETS_FILTER')
        filter_query = ''
        path = path + filter_query

        try:
            data = {}
            data_api = GetAPI(domain, path)
            response = data_api.get()

            json_response = response.json()
            tickets = [t for t in json_response['tickets']]

            filename = 'Zendesk_tickets_' + \
                datetime.now().strftime('%d-%m-%Y - %H.%m.%s') + '.csv'
            export = Export(tickets, filename)
            export.export_to_csv()

            #data['tickets'] = tickets
            data['success'] = True
        except Exception as g:
            print('Error: ', str(g))
            data['message'] = g

        return Response(data)