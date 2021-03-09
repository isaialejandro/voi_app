import os, logging, base64, pathlib
from datetime import datetime

import requests
import pandas as pd


class GetAPI:
    def __init__(self, domain, path):
        self.domain = domain
        self.path = path
    def auth(self):
        response = None
        try:
            usr = 'isai.alejandro@voioutsourcing.com.mx'
            token = 'nK8eEU5MARifXI7aPqD4HJypgEf1VtJs7MtBh0nd'

            data = usr + '/token:' + token
            str_bytes = data.encode('ascii')
            base64_bytes = base64.b64encode(str_bytes)
            base64_str = base64_bytes.decode("ascii")
            
            session = requests.Session()
            session.headers = {
                'Content-Type': 'application/json',
                'Authorization': 'Basic ' + base64_str
            }
            full_api = self.domain + self.path
            response = session.get(full_api)
        except Exception as i:
            logging.error('Error trying to access to requested API . . .\n', i)
        return response
    def get(self):
        response = self.auth()
        if response.status_code != 200:
            msg = 'An error was occurred trying to get API response.'
            logging.error(msg)
            raise AuthorizationError(response.status_code, msg)
        return response
        
        
class AuthorizationError(Exception):
    """
    Raised from the client if the server generated an error while generating
    an access token.
    """
    def __init__(self, http_code, message):
        super(AuthorizationError, self).__init__(message)
        self.http_code = http_code
        print(http_code)


class GetZendeskUser:
    def __init__(self, response):
        self.response = response
    def get_user(self):
        json_response = self.response.json()
        count = 1
        user_list = []
        for item in json_response['users']:          
            user_list.append({
                'id': item['id'],
                'name': item['name'],
                'email': item['email'],
                'role': item['role'],
                'active': item['active'],
                'group(s)': None

            })
            count += 1
            
        """Get first get response and iterate trough next possible pagination"""
        next_page = json_response['next_page']
        if next_page:
            domain = next_page.split('/', 1)[1][1:] + '/'
            path = next_page.split('/')[-1]
            data_api = GetAPI('https://' + domain, path)
            response = data_api.get()
            get_user = GetZendeskUser(response)
            next_user_list_iterarion = get_user.get_user()

            for u in next_user_list_iterarion:
                user_list.append({
                    'id': u['id'],
                    'name': u['name'],
                    'email': u['email'],
                    'role': u['role'],
                    'active': u['active'],
                    'group(s)': None
                })
        return user_list


class UserGroup:
    def __init__(self, user_list, domain):
        self.user_list = user_list
        self.domain = domain  
    def get_user_group(self):
        user_list = self.user_list
        domain = self.domain
        path = '/api/v2/users/'

        count = 1
        for r in user_list:
            get_api = GetAPI(domain, path + str(r['id']) + '/groups.json')
            response = get_api.get()
            json_response = response.json()
            group_list = []
            for g in json_response['groups']:
                group_list.append(g['name'])
            r['group(s)'] = group_list
            print('# ', count , r['group(s)']) 
            count += 1
        return user_list


class Export:
    def __init__(self, file):
        self.file = file
    def export_to_csv(self):
        file = self.file
        df = pd.DataFrame(file)
        output_path = os.path.dirname(os.path.abspath('user_files/')) #Fix.
        #output_path = pathlib.Path().absolute()
        print('Output:', output_path)
        df.to_csv(
            output_path + '/user_files/' + '/Active_Zendesk_usesrs_' + 
                datetime.now().strftime('%d-%m-%Y - %H.%m.%s') + '.csv',
            index=False,
            encoding='utf-8'
        )
        print('File exported successfully!')