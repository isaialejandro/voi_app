import uuid
import random
import glob

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
    Saving to Formatted *txt File:
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

    def post(self, request, format=None):

        files_list = glob.glob('/home/isaialejandro/Documentos/Django_projects/voi_app/accounts/JunY42020/*.csv')  #request.FILES

        total = []
        account_period = []
        cuentas = []
        reference_date = []
        transaction_key = []
        local_curr = []
        local_amount = []

        for f in files_list:

            csv = pd.read_csv(f, index_col=None, header=0)
            filename = f.split('/')[-1]

            total_local_amount = csv.agg({'local_amount': ['sum'] })
            total_rows = len(csv.index)

            print('Reading <<' + filename + '>> file . . .\n\n')
            total.append({
                "File: ": filename,
                "Total Rows:": total_rows,
                "Aggregate": total_local_amount,
            })

            print('Creating list . . .')
            account_period.append(csv['account_period'])
            cuentas.append(csv['debit_account_number'])
            reference_date.append(csv['reference_date'])
            transaction_key.append(csv['transaction_key'])
            local_curr.append(csv['local_currency'])
            local_amount.append(csv['local_amount'])

        print('Creating DataFrames . . .')
        df_account = pd.DataFrame(account_period)
        df_cuentas = pd.DataFrame(cuentas)
        df_reference_date = pd.DataFrame(reference_date)
        df_transaction_key = pd.DataFrame(transaction_key)
        df_local_currency = pd.DataFrame(local_curr)
        df_local_amount = pd.DataFrame(local_amount)

        print('Concatenating DataFrames. . .')
        all_columns = pd.concat([df_account, df_cuentas,df_reference_date, df_transaction_key, df_local_currency])
        all_columns.to_csv(
            '/home/isaialejandro/Documentos/Django_projects/voi_app/accounts/JunY42020/output_Y4Jun2020.txt',
            sep='\t'
            )


        #Temporal random int generator:
        """
        import random
        new_ids = []
        for r in range(843748, 2990101):
            new_ids.append(r)

        df1 = pd.DataFrame(new_ids)
        df1.to_csv('/home/isaialejandro/Documentos/Django_projects/voi_app/accounts/JunY42020/random_int.csv')
        """

        return Response(data={
            "Files": "{} files uploaded".format(len(files_list)),
            "Total Local Amount": total,
            "Final Output": all_columns
            })
