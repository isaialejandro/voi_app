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
                print('First API request: ', url)
                response = session.get(url)
            else:
                response = session.get(new_url)
        except Exception as i:
            logging.error('Error trying to access to requested API in main function . . .\n', i)
        return response
        
    def get(self):

        """Get request of entire object."""

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

            c = 1
            while next_page:
                try:
                    print('Current URL to Request: ', next_page)
                    response = self.auth(new_url=next_page)
                    new_data = response.json()
                    print('Count: ', new_data['count'])

                    # If the request object has "end_time" dict:
                    """current_end_time = new_data['end_time']
                    print('variable: ', type(current_end_time), ' - ', 'number: ', type(1577981101))
                    if ( int(current_end_time) == int(1577981101) ):
                        print('Current end time: ', current_end_time, ' - ', type(current_end_time))
                        print('Breaking While . . .\n')
                        break"""
                    
                    if c == 80:
                        break 
                    c +=1
                    print('Flag: ', c)

                    # Hacer merge entre todos los jsons obtenidos de cada
                    # solicitud por paginación a la API.
                    full_json_response.append(new_data)
                    next_page = new_data['next_page']
                except Exception as d:
                    print('Exception. ', d, ' NOT found here. Avoiding . . .\n')
                    break
            return full_json_response        
        

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
        path = '/api/v2/users/'

        count = 1
        for r in user_list:
            data_api = GetAPI(domain, path + str(r['id']) + '/groups.json', api_filter=None)
            response = data_api.get()

            # Getting Group dict only.
            group = response[0]
            group = group['groups']

            group_list = []
            for g in group:
                group_list.append(g['name'])
            
            r['group(s)'] = group_list
            print('# ', count , r['group(s)'])
            count += 1
        return user_list


class AuthorizationError(Exception):

    """
    Raised from the client if the server generated an error while generating
    an access token.
    """

    def __init__(self, http_code, message):
        msg = message, '\nStatus Code: ', http_code
        super(AuthorizationError, self).__init__(msg)
        self.http_code = http_code
        print(http_code)