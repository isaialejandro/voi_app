from datetime import datetime
import dateutil.parser
import uuid
import random
import glob
import sys

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

    permission_classes = [IsAuthenticated]
    #permission_classes = []
    #parser_classes = [FileUploadParser]

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

        print('Parsing dates of column: ', column, '\n')

        def get_new_format(d_time):
            
            prev_date = datetime.strptime(str(d_time), '%Y-%m-%d  %H:%M:%S')
            final_format = prev_date.strftime('%m/%d/%Y')
            return final_format

        date_list = []
        try:

            for date in df[column]:
                
                #Parsing each item to: "Y-m-d H-M-S"
                datetetime_obj = dateutil.parser.parse(date)
                time  = ' %H:%M:%S'
                bad_format = '%Y-%m-%d  %H:%M:%S'
                #Final desired format: "%m/%d/%Y"

                try:
                    prev_date = datetime.strptime(str(datetetime_obj), bad_format)
                    new_format = get_new_format(prev_date)
                except Exception as e:
                    print('Input format not found!')
                    
                date_list.append(new_format)

            df[column] = date_list
            return df

        except Exception as g:
            print("Enccountered exception trying to format date columns.\nSystem exit:\n")
            sys.exit(e)

    def FormatPNR(self, df, column):

        """
        Receive DF with all processed files and specific column name for formatting.
        """
        current_col = column
        pnr_list = []

        for col in df[current_col]:
            pnr_list.append(col[:-4])

        df[current_col] = pnr_list

        return df

    def CountFileRows(self, file_list):
        
        for f in file_list:

            #Getting filename & Counting all *csv Rows:
            filename = f.split('/')[-1]
            total_rows = len(csv.index)
            total_local_amount = csv.agg({'local_amount': ['sum'] })

            print('Reading: <<' + filename + '>> file . . .\n\n')
            sumatoria.append({
                "File: ": filename,
                "Total Rows:": total_rows,
                "Aggregate": total_local_amount,
            })

    def GetCSV(self, path):

        try:
            files_list = glob.glob(path + '*.csv')  #request.FILES

            csv_list = []
            #Getting unsorted columns form each file:
            current_cols = [
                'account_period',
                'debit_account_number', #Cuentas
                'local_amount',
                'transaction_key',
                'local_currency',
                'reference_date'
            ]

            for file in files_list:

                print('Processing File: \n', file.split('/')[-1] , '\n\n')
                
                csv_list.append(pd.read_csv(file, index_col=None, header=0, usecols=current_cols))
            
            full_data = pd.concat(csv_list, ignore_index=True)
            #Sorting columns:
            full_data = full_data.reindex(columns=[
                'account_period',
                'debit_account_number',
                'reference_date',
                'transaction_key',
                'local_currency',
                'local_amount'
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

            return df
        except BaseException as e:
            print('Error trying to read file (s).\nCheck your files route:')
            sys.exit(e)

    def post(self, request, format=None):
        
        #File Output
        linux_output_path = '/home/isaialejandro/Documentos/Django_projects/voi_app/accounts/JunY42020/output_Y4Jun2020.txt'
        osx_output_path = '/Users/isaialejandro/Downloads/Y4Jun2020/output_Y4Jun2020.txt'

        path = '/Users/isaialejandro/Downloads/Y4Jun2020/'

        #Getting All files in DataFrame from "get_csv()"
        df_csvs = self.GetCSV(path)


        #Passing entire DataFrame for format PNR column.
        df_formatted_01 = self.FormatPNR(df_csvs, 'Transaction Key')

        #Formating Date of 2 fields:
        df_formatted_02 = self.ConvertToDatetime(df_formatted_01, 'Account Period')
        df_formatted_03 =  self.ConvertToDatetime(df_formatted_02, 'Reference Date')

        #Rounding column data to 2 digits: - PENDING!!
        #df_formatted_04 =self.RoudToTwoDigits(df_formatted_03, 'Local Amount')

        #Aggregate LocalAmount column here:
        df_formatted_03.loc['Total Local Amount', 'Local Amount'] = df_formatted_03['Local Amount'].sum()

        #Exporting to *TXT:
        print('Exporting to *.TXT . . .')
        df_formatted_03.to_csv(osx_output_path, sep='\t', encoding='utf-8', index=False)
        print('File exported successfully to: \n', osx_output_path)




        #Temporal random int generator:
        """
        import random
        new_ids = []
        for r in range(843748, 2990101):
            new_ids.append(r)
        """

        #return Response(data={
        #    "Files": "{} files uploaded".format(len(files_list)),
        #    })
        return Response(data={"ok":"ok"})
