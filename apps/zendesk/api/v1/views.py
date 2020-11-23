import json
from django.views.generic.list import ListView, View

from rest_framework.views import APIView
from rest_framework.response import Response

from apps.zendesk.models import ZendeskUser

from apps.tools.http.services import GetAPI, GetZendeskUser, UserGroup, Export


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

            export = Export(final_user_list)
            export.export_to_csv()
        except Exception as t:
            data['message'] = str(t)
            print('Error trying to retrieve API: ', t)
        data['message'] = final_user_list
        return Response(data)
