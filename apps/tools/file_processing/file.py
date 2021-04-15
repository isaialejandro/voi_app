import glob, os

from django.http import HttpResponse

from django.conf import settings

import pandas as pd

"""
class File:
    def __init__(self, filepath, file_type):
        self.filepath = filepath
        self.file_type = file_type

    def getFile(self):
        
        try:
            filepath = self.filepath
            file_list = glob.glob(filepath)
            return file_list
        except Exception as g:
            print('Except: ', g)

    def exportToFile(self, created_at=None, filename=None):
        
        #Export csv file with all datakeys like file rows.
        
        #Validate if current file to export is or not a pandas DataFrame.
        if not isinstance(created_at, pd.DataFrame):
            df = pd.DataFrame(created_at)
        else:
            df = created_at

        #output_path = self.filepath
        file_type = self.file_type
        print('Exporting file: ', filename + file_type)
        media_path = os.path.dirname(os.path.abspath('voi/')) + '/voi/media/user_files/'
        print('media: ', media_path)
        df.to_csv(media_path + filename + file_type, index=False, encoding='utf-8')
        
        #Downloading generated file:
        #self.download_file(filename=filename, media_path=media_path, file_type=file_type)
        print('File ' + filename + ' has stored successfully . . .\n', \
            media_path + filename + file_type)


    def download_file(self, filename=None, media_path=None, file_type=None):

        #Function that download generated files by other processes, in a custom format.

        media_path = media_path
        file_type = file_type

        print('Current file type: ', filename, file_type)

        response = HttpResponse(open(media_path + filename + file_type, 'rb').read())
        response['Content-Type'] = 'text/csv' + file_type # 'text/csv'
        response['Content-Disposition'] = 'attachment; filename=' + filename + file_type
        return response
"""