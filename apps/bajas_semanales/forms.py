from django import forms

from django.contrib import messages

from apps.application.models import Application
from apps.bajas_semanales.models import BajaSemanal

#from apps.extra_incidents.choices import *


class BajaSemanalForm(forms.ModelForm):

    #application = forms.MultipleChoiceField(
    #        required=True,
    #        widget=forms.CheckboxSelectMultiple,
    #    )

    class Meta:

        model = BajaSemanal

        fields = [
            'tipo',
            'subject',
            'user_code',
            'user_name',
            'request_date',
            'application',
        ]

        widgets = {
            'tipo': forms.TextInput(attrs={'class': 'form-control'}),
            'subject': forms.TextInput(attrs={'class': 'form-control'}),
            'user_code': forms.TextInput(attrs={'class': 'form-control'}),
            'user_name': forms.TextInput(attrs={'class': 'form-control'}),
            'request_date': forms.TextInput(attrs={'class': 'form-control'}),
            'application': forms.CheckboxSelectMultiple(),
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
