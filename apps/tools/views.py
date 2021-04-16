import sys, os, glob

from django.core.files.storage import default_storage

from django.conf import settings

from django.shortcuts import render

from django.views import View

from django.http import HttpResponse
from django.http.response import Http404

import pandas as pd


"""
def generate_random_id(self):
    # Generates random id for new records or something.

    id = ''
    regexp = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTVWXYZ1234567890!@#$%&/()=?*-_'
    length = 50
    for r in range(length):
        id += regexp[random.randint(0, len(regexp)-1)]
    return id
"""


class File:
    def __init__(self, file_path, filename):
        self.file_path = file_path
        self.filename = filename

    def getFile(self):
        
        try:
            file_path = self.file_path
            file_list = glob.glob(file_path)
            return file_list
        except Exception as g:
            print('Except: ', g)

    def exportToFile(self, user_list):
        """
        Export csv file with all datakeys like file rows.
        """
        filename = self.filename
        #Validate if current file to export is or not a pandas DataFrame.
        if not isinstance(user_list, pd.DataFrame):
            df = pd.DataFrame(user_list)
        else:
            df = user_list

        print('Exporting file: ', filename)
        file_path = self.file_path
        print('media: ', file_path)
        df.to_csv(file_path + filename, index=False, encoding='utf-8')
        print('File ' + filename + ' has stored successfully . . .\n')
        

    def download_file(self, request):
        
        filename = self.request.GET.get('filename')
        user_path = 'user_files/' + filename
        file_path = os.path.join(settings.MEDIA_ROOT, user_path)
        f = default_storage.open(file_path).read()

        if os.path.exists(file_path):
            #print('exists!!!!')
            with open(file_path, 'rb') as f:
                response = HttpResponse(f.read(), content_type='application/csv')
                response['Content-Disposition'] = 'attachment; filename="' + os.path.basename(file_path) + '"'
                # response['Content-Disposition'] = 'attachment; filename="' + filename + '"'
                
                #return response
                return render(request, 'active_user_list.html')
        else:
            print('else!!')
            raise Http404
    