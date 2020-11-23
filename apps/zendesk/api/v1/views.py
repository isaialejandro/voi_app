import sys
from datetime import datetime

from django.views.generic.list import ListView, View
from django.contrib.auth.models import User

from rest_framework.views import APIView
from rest_framework.response import Response

from apps.zendesk.models import ZendeskUser

from apps.tools.http.services import GetAPI, GetZendeskUser, UserGroup, Export
from apps.zendesk.models import ZendeskUser, ZendeskUserHistory


now = datetime.now()

class GetActiveUsersAPI(APIView):

    authentication_classes = []
    permission_classes = []

    def get(self, request):

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
                print('USER: ', u['email'])
                zendeskUser = ZendeskUser(
                    user_id=u['id'],
                    name=u['name'],
                    email=u['email'],
                    role=u['role'],
                    group=u['group(s)']
                )
                #hist_id = self.create_hist(final_user_list)
                #zendeskUser.hist=ZendeskUserHistory.objects.get(id=hist_id)
                zendeskUser.save()

            #export = Export(final_user_list)
            #export.export_to_csv()
        except Exception as t:
            data['message'] = str(t)
            print('Error trying to retrieve API: ', t)
        data['message'] = final_user_list
        data['status_code'] = '200'
        return Response(data)

    def create_hist(self, userlist):
        user_list = userlist
        try:
            #total_licenses = len(user_list)

            admins, agents = []
            dict_len = len(user_list)
            print('LEN: ', dict_len)
            
                    #print(key['role'])
                    #admins.append({ key['id'] if key['role'] == 'admin' else None })
                    #agents.append({ key['id'] if key['role'] == 'agent' else None })
            sys.exit(1)
            """
            admins = len(admins)
            agents = len(agents)

            zendesk_hist = ZendeskUserHistory(
                total_occupied_licenses=total_licenses,
                current_admins=admins,
                current_agents=agents,
                date=now.strftime('%d-%m-%Y %H:%M:%S %p'),
                exec_user=User.objects.get(id=self.user.id)
            )
            zendesk_hist.save()
            return zendesk_hist
            """
        except Exception as g:
            print('Error trying to create History: ', g)