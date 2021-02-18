import sys, json
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

from apps.zendesk.models import ZendeskUser

from apps.tools.http.services import GetAPI, GetZendeskUser, UserGroup, Export
from apps.zendesk.models import ZendeskUser, ZendeskUserHistory


now = datetime.now()

class GetActiveUsersAPI(APIView):

    authentication_classes = [ SessionAuthentication, BasicAuthentication ]
    permission_classes = [ IsAuthenticated ]

    @transaction.atomic
    def get(self, request):
        data = {}
        hist = None
        domain = 'https://volaris.zendesk.com/'
        path = 'api/v2/users.json'
        filter_query = '?role[]=admin&role[]=agent'
        path = path + filter_query
        final_user_list = None
        try:
            data_api = GetAPI(domain, path)
            response = data_api.get()

            get_user = GetZendeskUser(response)
            user_list = get_user.get_user()
            print('Getting User Groups . . .')
            get_user_group = UserGroup(user_list, domain)
            final_user_list = get_user_group.get_user_group()
            for u in final_user_list:
                zendeskUser = ZendeskUser(
                    user_id=u['id'],
                    name=u['name'],
                    email=u['email'],
                    role=u['role'],
                    group=u['group(s)']
                )
                zendeskUser.save()
            hist = self.create_hist(final_user_list)
            data['total_occupied'] = hist.total_occupied_licenses
            data['current_admins'] = hist.current_admins
            data['current_agents'] = hist.current_agents
            data['success'] = True
            data['message'] = final_user_list
            data['status_code'] = '200'
            return Response(data)
        except Exception as t:
            data['message'] = str(t)
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
            for u in ZendeskUser.objects.all():
                u.hist=ZendeskUserHistory.objects.get(id=zendesk_hist.id)
                u.save()
            return zendesk_hist
        except Exception as g:
            print('Error trying to create History: ', g)

class ExportUserAPI(APIView):
    
    def post(self, request):
        data = {}
        user_list = []
        #print('OBJECT: \n', request.data)
        try:
            full_data = request.data
            c = 0
            for k, v in full_data.items():
                match_substr = 'data[' + str(c) + ']'
                r =[v for k, v in full_data.items() if match_substr in k]
                user_list.append(r)
                c = c + 1
            headers = ['Id', 'Name', 'Email', 'Role', 'Active', 'Group(s)']

            export = Export(user_list, headers)
            export.export_to_csv()
            print('Exported:', export)
            data['success'] = True
            data['message'] = 'File exported Successfully!'
        except Exception as f:
            data['message'] = str(f)
            print('EXC: ', f)
        return Response(data)
