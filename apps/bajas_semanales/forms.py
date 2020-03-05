from django import forms

from django.contrib import messages

from apps.application.models import Application
from apps.bajas_semanales.models import TipoBaja, BajaSemanal

#from apps.extra_incidents.choices import *

class TipoBajaForm(forms.ModelForm):

    class Meta:

        model = TipoBaja
        fields = ['type']
        labels = {'type': 'Tipo de Baja Semanal'}
        widgets = {'type': forms.TextInput(attrs={'class': 'form-control'})}

class BajaSemanalForm(forms.ModelForm):

    def __init__(self, request, *args, **kwargs):
        super(BajaSemanalForm, self).__init__(*args, **kwargs)
        self.fields['type'].queryset=TipoBaja.objects.filter(is_active=True)
        self.fields['application'].queryset=Application.objects.filter(is_active=True, is_for_bajas_semanales=True)

    class Meta:

        model = BajaSemanal

        fields = [
            'type',
            'subject',
            'user_code',
            'user_name',
            'request_date',
            'application',
        ]

        widgets = {
            'type': forms.Select(attrs={'class': 'form-control select2'}),
            'subject': forms.TextInput(attrs={'class': 'form-control'}),
            'user_code': forms.TextInput(attrs={'class': 'form-control'}),
            'user_name': forms.TextInput(attrs={'class': 'form-control'}),
            'request_date': forms.TextInput(attrs={'class': 'form-control'}),
        }

    #Solo funciona cuando en la vista se usa la función "is_valid()"
    """
    def clean_inc_number(self):

        inc_number = self.cleaned_data['inc_number']

        if ExtraIncident.objects.filter(is_active=True, inc_number=inc_number):
            print('ERROR', inc_number)

            msg = 'Incident already exists, try with another one.'
            #messages.error(request, msg)

            raise ValidationError(inc_number + 'is already registered. Try with another one.')

        print('CLEAN')
        return inc_number
    """
