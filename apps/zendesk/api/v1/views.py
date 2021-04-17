import sys, os

from datetime import datetime

from django.db import transaction

from django.contrib.auth.models import User

from rest_framework.views import APIView
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from dotenv import load_dotenv

import pandas as pd

from apps.zendesk.models import ZendeskUser

from apps.tools.http.services import GetAPI, GetZendeskUser, UserGroup
from apps.tools.views import File
from apps.zendesk.models import ZendeskUser, ZendeskUserHistory

load_dotenv()


now = datetime.now()

class GetActiveUsersAPI(APIView):

    """Get the active users lists only in json format."""

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
            filename = 'Active_Zendesk_usesrs_' + \
                datetime.now().strftime('%d-%m-%Y - %H.%m.%s')

            data['filename'] = filename + '.csv'
            data['total_occupied'] = hist.total_occupied_licenses
            data['current_admins'] = hist.current_admins
            data['current_agents'] = hist.current_agents
            data['success'] = True
            data['message'] = final_user_list
            data['status_code'] = '200'
        except Exception as t:
            data['message'] = t
            print('Error trying to retrieve API: ', str(t))
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
                exec_user=User.objects.get(id=self.request.user.id)
            )
            zendesk_hist.save()

            return zendesk_hist
        except Exception as g:
            print('Error trying to create History: ', g)
            return g


class ExportUserAPI(APIView):

    """ Export zendesk users data into a *csv file, in a subfolder allocated in the default 
        media project. """

    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
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

            filename = self.request.GET.get('filename')
            filepath = os.path.dirname(os.path.abspath('voi/')) + '/voi/media/user_files/'
            # Trigger the generation and file download for user purposes.
            export = File(filepath, filename)
            export.exportToFile(user_list=final_user_list)
            
            data['success'] = True
            data['message'] = 'File exported Successfully!'
        except Exception as f:
            data['message'] = str(f)
            print('Exc: ', f)
        return Response(data)


class GetTickets(APIView):

    """Return All tickets from a date range."""

    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):

        domain = os.getenv('ZENDESK_API_DOMAIN')
        path = os.getenv('ZENDESK_TICKETS_PATH')
        filter_query = os.getenv('ZENDESK_TICKETS_FILTER')

        try:
            data = {}
            data_api = GetAPI(domain, path, filter_query)
            json_response = data_api.get()

            ticket_list = []
            for item in json_response:
                # Getting Ticket list only, from incremental API
                for t in item['tickets']:
                    ticket_list.append(t)
            filename = 'Zendesk_tickets_' + \
                datetime.now().strftime('%d-%m-%Y - %H.%m.%s')
            filepath = os.path.dirname(os.path.abspath('user_files/')) + \
                '/zendesk_tickets/unstructured_datasets/'
            file_type = '.csv'
            export = File(filepath, file_type)
            export.exportToFile(created_at=ticket_list, filename=filename)

            data['tickets'] = 'Number of total items in List: ', len(ticket_list)
            data['success'] = True
        except Exception as g:
            print('Error: ', str(g))
            data['message'] = str(g)
        return Response(data)


class StructureTicket(APIView):

    """
    API that get all unstructured datasets outputs from 
    "GetTickets()", build an entire DataFRame and 
    separate every desired dataset in dataframes.
    It create a new file for each month \nEg. Enero-2020 , Febrero2020, etc.\n
    This function needs to be called every time when a new dataFrame needs to be
    created for future processes.\n

    For this execution, datasets needs to be in the folder: /zendesk_tickets/.
    """

    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        data = {}
        return Response(data)
    def buildDataFrame(self):
        """
        Get data into a list form 
        """
        path = os.path.dirname(os.path.abspath('user_files/')) + \
            '/zendesk_tickets/unstructured_datasets/' 
        file_format = '*csv'
        getFile = File(path + file_format)
        file_list = getFile.getFile()

        data_list = []
        c = 1
        for f in file_list:
            print('#', c)
            df = pd.read_csv(f, index_col=None, header=0)
            data_list.append(df)
            c += 1
        df = pd.concat(data_list, axis=0, ignore_index=True)
        print('DF head: \n', df.head())
        return df

    def post(self, request):

        data = {}
        print('Building DataFrame. .  .')
        data_df = self.buildDataFrame()
        months = {
            'Enero|': '2020-01',
            'Febrero': '2020-02',
            'Marzo': '2020-03',
            'Abril': '2020-04',
            'Mayo': '2020-05',
            'Junio': '2020-06',
            'Julio': '2020-07',
            'Agosto': '2020-08',
            'Septiembre': '2020-09',
            'Octubre': '2020-10',
            'Noviembre': '2020-11' ,
            'Diciembre': '2020-12'
        }
        c = 1
        for k, v in months.items():
            try:
                created_at_df = data_df[data_df['created_at'].str.contains(months[k], na=False)]
                current_yearmonth = k.replace('|', '') + v[:-3]
                filename = str(c) + '_ZendeskTickets-' + current_yearmonth

                # Quitar. Se repite en línea #196.
                path = '/Users/isaialejandro/Documents/workSpace/Django/voireg/voi_app/zendesk_tickets/final_data/'
                file = File(path)
                file.exportToFile(created_at=created_at_df, filename=filename)
                c += 1
            except Exception as x:
                print('ERROR: ', x)
                sys.exit(1)
        data['success'] = 'All files exported successfully!!'
        return Response(data)   
