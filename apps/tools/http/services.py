import os, logging, base64, pathlib, sys, json
from collections import ChainMap
from datetime import datetime

from dotenv import load_dotenv

import requests
import pandas as pd

load_dotenv()


class GetAPI:
    def __init__(self, domain, path, api_filter):
        self.domain = domain,
        self.path = path,
        self.api_filter = api_filter
    def auth(self, new_url=None):
        response = None
        try:
            usr = os.getenv('ZENDESK_AUTH_USER')
            token = os.getenv('ZENDESK_AUTH_PWD')

            data = usr + '/token:' + token
            str_bytes = data.encode('ascii')
            base64_bytes = base64.b64encode(str_bytes)
            base64_str = base64_bytes.decode("ascii")
            
            session = requests.Session()
            session.headers = {
                'Content-Type': 'application/json',
                'Authorization': 'Basic ' + base64_str
            }

            if new_url is None:
                domain = ''.join(self.domain)
                path = ''.join(self.path)
                api_filter = '' if not self.api_filter else self.api_filter
                url = domain + path + api_filter
                response = session.get(url)
            else:
                response = session.get(new_url)
        except Exception as i:
            logging.error('Error trying to access to requested API in main function . . .\n', i)
        return response
    def get(self):
        """Get request of entire object."""
        #domain = ''.join(self.domain)
        #path = ''.join(self.path)
        #api_filter = '' if not self.api_filter else self.api_filter
        #url = domain + path + api_filter
        response = self.auth()
        if response.status_code != 200:
            msg = 'An error was occurred trying to get API response.'
            logging.error(msg)
            raise AuthorizationError(response.status_code, msg)
        else:
            json_response = response.json()
            next_page = json_response['next_page']
            full_json_response = []
            full_json_response.append(json_response)
            while next_page:
                print('Current URL to Request: ', next_page)
                response = self.auth(new_url=next_page)
                new_data = response.json()
                
                # Hacer merge entre todos los jsons obtenidos de cada solicitud por paginación a la API.
                full_json_response.append(new_data)
                next_page = new_data['next_page']
        return full_json_response        
        
        
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
    def __init__(self, json_response):
        self.json_response = json_response
    def get_user(self):
        """Get all users from whole API response (filtering users)."""
        json_response = self.json_response
        count = 1
        user_list = []
        for item in json_response:
            for i in item['users']:
                user_list.append({
                    'id': i['id'],
                    'name': i['name'],
                    'email': i['email'],
                    'role': i['role'],
                    'active': i['active'],
                    'group(s)': None
                })
                count +=1
        return user_list


class UserGroup:
    def __init__(self, user_list, domain):
        self.user_list = user_list
        self.domain = domain
    def get_user_group(self):
        user_list = self.user_list
        domain = self.domain
        path = 'api/v2/users/'

        count = 1
        for r in user_list:
            data_api = GetAPI(domain, path + str(r['id']) + '/groups.json', api_filter=None)
            response = data_api.get()
            group = response[0] # Getting Group dict only.
            group = group['groups']

            group_list = []
            for g in group:
                group_list.append(g['name'])
            
            r['group(s)'] = group_list
            print('# ', count , r['group(s)'])
            count += 1
        return user_list


class Export:
    def __init__(self, file, filename):
        self.file = file
        self.filename = filename
    def export_to_csv(self):
        file = self.file
        df = pd.DataFrame(file)
        output_path = os.path.dirname(os.path.abspath('user_files/'))
        print('Output:', output_path)
        
        df.to_csv(
            output_path + '/user_files/' + self.filename,
            index=False,
            encoding='utf-8'
        )
        #Downloading file direclty with requests python module:
        #r = requests.get(output_path + '/user_files/' + self.filename)
        #with open('full_path', 'wb') as f:
        #    f.write(r.content)

        print('File exported successfully!')