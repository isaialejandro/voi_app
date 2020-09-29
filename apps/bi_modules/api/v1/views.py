from datetime import datetime
import dateutil.parser
import uuid
import random
import glob
import sys
import logging

from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import FileUploadParser, MultiPartParser
from rest_framework.response import Response
from rest_framework import authentication, permissions

from django.contrib.auth.models import User

import numpy as np
import pandas as pd

from apps.bi_modules.models import Account
from apps.bi_modules.api.v1.serializers import AccountSerializer


now = datetime.now()
#Logging:
logging.basicConfig(

    filename ='Account_processing - ' + str(now.strftime("%d-%m-%Y %H:%M:%S")) ,
    level=logging.INFO,
    format='%(asctime)s: %(levelname)s:%(message)s',
    datefmt='%d-%m-%Y %I:%M:%S %p'
    )


class AccountList(ListAPIView):

    queryset = Account.objects.all() #raw('SELECT * FROM bi_modules_account')
    serializer_class = AccountSerializer
    permission_classes = [IsAuthenticated]


class MatchAcountFiles(APIView):

    """
    1.- Obtiene multiples cuentas en *csv.\n
    2.- Filtro de campos específicos.\n
    3.- Formateo de data en campo "TransactionKey" eg: "CDFMXN-2" >> "CDFMXN".\n
    4.- Formateo de fecha en campo "ReferenceDate" eg: "06/06/2020" >> "06-06-2020"\n
    5.- Creación de DF para campos filtrados por cada archivo.\n
    6.- Suma de total de campo "LocalAmount". Creación de nueva columna.\n
    """

    """
    Output to Formatted *txt File:
    *AccountPeriod
    *Cuentas
    *ReferenceDate
    *TransactionKey
    *LocalCurrency
    *LocalAmount
    """

    permission_classes = [ IsAuthenticated ]

    def get(self, request):
        data = {}
        return Response(data)

    def RoudToTwoDigits(self, df,  column):
        print('Rounding column: ', column, ' to 2 digits . . .')
        rounded_list = []

        rounded = df[column].round(decimals=2)
        df[column] = rounded 
        
        return df

    def ConvertToDatetime(self, df, column):
        """
        Receive specific date column of entire DF for date formatting.
        """
        def get_new_format(d_time): 
            prev_date = datetime.strptime(str(d_time), '%Y-%m-%d  %H:%M:%S')
            final_format = prev_date.strftime('%m/%d/%Y 12:00:00')
            return final_format

        try:
            logging.info('Date formatting BEGIN.\nParsing dates of column: ' + column + '\n')
            date_list = []
            for date in df[column]:
                #Parsing each item to: "Y-m-d H-M-S"
                datetetime_obj = dateutil.parser.parse(date)
                #Final desired format: "%m/%d/%Y"
                try:
                    prev_date = datetime.strptime(str(datetetime_obj), '%Y-%m-%d %H:%M:%S')
                    new_format = get_new_format(prev_date)
                    date_list.append(new_format)
                    #df[column] = df[column].replace([date], new_format)
                except Exception as e:
                    logging.warning('Input not found:\n')
                    logging.error(e)
                    sys.exit()
            df[column] = date_list
            logging.info('Date formatting END successfully.\n')
            return df
        except Exception as g:
            logging.error('Enccountered exception trying to format date columns.\nSystem exit:\n', g)
            sys.exit(e)

    def FormatPNR(self, df, column):
        """
        Receive DF with all processed files and specific column name for formatting.
        """
        pnr_list = []
        current_col = column
        logging.info('STARTING PNR Format . . .')
        for col in df[current_col]:    
            #strip_record = col.strip()
            pnr_list.append(col[0:6])
            #df[current_col] = df[current_col].replace([col], col[0:6])
        df[current_col] = pnr_list
        logging.info('PNR Format FINISH successfully.')
        return df

    def CountFileRows(self, file_list): #NOT IN USE
        for f in file_list:
            #Getting filename & Counting all *csv Rows:
            filename = f.split('/')[-1]
            total_rows = len(csv.index)
            total_local_amount = csv.agg({'local_amount': ['sum'] })
            #sumatoria.append({
            #    "File: ": filename,
            #    "Total Rows:": total_rows,
            #    "Aggregate": total_local_amount,
            #})

    def GetCSV(self, path):
        try:
            files_list = glob.glob(path + '*.csv')
            csv_list = []
            #Getting unsorted columns form each file:
            current_cols = [
                'Account Period',
                'Debit Account Number', #Cuentas
                'LocalAmount',
                'Transaction Key',
                'LocalCurrency',
                'Reference Date'
            ]

            no = 1
            for file in files_list:
                filename = file.split('/')[-1]
                csv_list.append(pd.read_csv(file, index_col=None, header=0, usecols=current_cols))
                logging.info('Getting file #' + str(no) + ': ' + filename)
                no += 1

            full_data = pd.concat(csv_list, ignore_index=True)
            #Sorting columns:
            full_data = full_data.reindex(columns=[
                'Account Period',
                'Debit Account Number', #Cuentas
                'Reference Date',
                'Transaction Key',
                'LocalCurrency',
                'LocalAmount'
            ])

            full_data.columns = [
                'Account Period',
                'Cuentas',
                'Reference Date',
                'Transaction Key',
                'Local Currency',
                'Local Amount'
            ]
            df = pd.DataFrame(full_data)
            logging.info('All files ready for process . . .')
            return df
        except BaseException as e:
            print('Error trying to read file (s).\nCheck your files route:')
            logging.error('Error trying to read file (s).\nCheck your files route:', e)
            sys.exit(e)

    def post(self, request, format=None):
        #File Output:
        osx_output_path = '/Users/isaialejandro/Downloads/Y4Jun2020/test/output_Y4Jun2020' + str(now.strftime("%Y-%m-%d_%H-%M-%S")) + '.txt'
        path = '/Users/isaialejandro/Downloads/Y4Jun2020/test/'
        #Getting All files in DataFrame from "get_csv()"
        df_csvs = self.GetCSV(path)
        #Passing entire DataFrame for format PNR column.
        df_formatted = self.FormatPNR(df_csvs, 'Transaction Key')
        #Formating Date of 2 fields:
        df_formatted = self.ConvertToDatetime(df_formatted, 'Account Period')
        df_formatted =  self.ConvertToDatetime(df_formatted, 'Reference Date')
        df_formatted['Cuentas'] = df_formatted['Cuentas'].astype(str)
        #Aggregate LocalAmount column here:
        df_formatted.loc['Total Local Amount', 'Local Amount'] = df_formatted['Local Amount'].sum()
        #Exporting to *TXT:
        logging.info('Exporting file to: ' + osx_output_path)
        df_formatted.to_csv(osx_output_path, sep=',', encoding='utf-8', index=False)
        logging.info('File successfully exported. \nProcess FINISHED.')
        #return Response(data={
        #    "Files": "{} files uploaded".format(len(files_list)),
        #    })
        return Response(data={"ok":"ok"})




#Temporal random int generator:
"""
import random
new_ids = []
for r in range(843748, 2990101):
    new_ids.append(r)
"""
