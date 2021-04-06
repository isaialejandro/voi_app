import glob, sys

from django.http import HttpResponse

import pandas as pd


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
        """
        Export csv file with all datakeys like file rows.
        """
        #Validate if current file to export is or not a pandas DataFrame.
        if not isinstance(created_at, pd.DataFrame):
            df = pd.DataFrame(created_at)
        else:
            df = created_at

        output_path = self.filepath
        file_type = self.file_type
        print('Exporting file: ', filename + file_type)
        df.to_csv(output_path + filename + file_type, index=False, encoding='utf-8')
        #Downloading generated file:
        self.download_file(filename=filename)
        print('File ' + filename + ' has exported successfully . . .\n', \
            output_path + filename + file_type)

    def download_file(self, filename=None):
        """
        Function that download generated files by other processes, in a custom file format.
        """
        output_path = self.filepath
        #file_type = filename.find('.')
        #file_type = filename[file_type:]
        file_type = self.file_type
        print('Current file type: ', file_type)

        response = HttpResponse(open(output_path + filename + file_type, 'rb').read())
        response['Content-Type'] = 'text/' + file_type #'text/csv'
        response['Content-Disposition'] = 'attachment; filename=' + filename + file_type
        return response