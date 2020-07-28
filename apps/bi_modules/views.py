import random

import datetime

import pandas as pd
#import numpy as np
from django.shortcuts import render

from django.contrib import messages

from django.views.generic import View, TemplateView

from apps.tools.decorators import NeverCacheMixin, CSRFExemptMixin

from apps.bi_modules.models import CuentasPorCobrarHistory


now = datetime.datetime.now()


class IngresosYCuentasPorCobrarView(View):

    def get(self, request):
        context = {}
        context['cuenntas_por_cobrar_dashboard'] = True
        return render(request, 'cuentas_por_cobrar_dashboard.html', context)

    def get_random_process_code(process_code):
        for x in range(1):
            process_code = random.randint(1, 2000001)
            print(process_code)

    def validate_files(csv_files):

        files_list = pd.read_csv(csv_files)

        #validación de archivos cargados
        for c in files_list:
            if csv_files.endswith('csv'):
                return True
            else:
                msg = messages.error(request, 'The files to process must be all' +
                ' in *csv, check your files.')
                return render(request, 'cuentas_por_cobrar_dashboard.html')


    #def process_files():

    def post(self, request, *args):

        new_process = CuentasPorCobrarHistory()

        csv_files=request.POST.getlist('files[]') #check this in front
        validated_data = validate_files(csv_files) #archivos validados.

        processed_data = process_files(validated_data) #procesamiento de data


        process_code = get_random_process_code(process_code)

        new_process.process_code=process_code
        new_process.process_date=now

        processed_by_year=request.POST.get('processed_by_year')
        processed_by_month=request.POST.get('processed_by_month')

        if processed_by_year:
            new_process.processed_years=True
        if processed_by_year:
            new_process.processed_months=True
        user=self.request.user

        sucess_process.save()

        messages.success(request, 'Proccess no. ' + process_code + ' finished successfully')
        return HttpResponse('/cuenntas_por_cobrar_dashboard/')

    
