import sys
from datetime import datetime
from django.utils import timezone

from django.views.generic.list import ListView, View
from django.contrib.auth.models import User

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

    def get(self, request):
        data = { 'message': 'Ok' }
        return Response(data)

    def post(self, request):

        data = {}
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
            self.create_hist(final_user_list)
            #export = Export(final_user_list)
            #export.export_to_csv()
        except Exception as t:
            data['message'] = str(t)
            print('Error trying to retrieve API: ', t)
        data['message'] = final_user_list
        data['status_code'] = '200'
        return Response(data)

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
                date=now,
                exec_user=User.objects.get(id=self.request.user.id)
            )
            print('Timezone: ', now)
            zendesk_hist.save()
            for u in ZendeskUser.objects.all():
                u.hist=ZendeskUserHistory.objects.get(id=zendesk_hist.id)
                u.save()
        except Exception as g:
            print('Error trying to create History: ', g)