from django import forms

from django.contrib import messages

from django.core.exceptions import ValidationError

from apps.extra_incidents.models import ExtraIncident

from apps.extra_incidents.models import ExtraIncident

from apps.extra_incidents.choices import *

class ExtraIncidentForm(forms.ModelForm):

    type =  forms.ChoiceField(choices=TYPE, widget=forms.Select(attrs={'class': 'form-control'}), initial=REGISTRY),
    inc_source =  forms.ChoiceField(choices=INC_SOURCE, widget=forms.Select(attrs={'class': 'form-control'}), initial=PAPERLESS),

    class Meta:

        model = ExtraIncident

        fields = [
            'inc_number',
            'application',
            'type',
            'exec_date',
            'end_date',
            'summary',
            'extra_comments',
            'inc_source',
        ]

        widgets = {
            'inc_number': forms.TextInput(attrs={'class': 'form-control'}),
            'application': forms.Select(attrs={'class': 'form-control'}),
            'exec_date': forms.TextInput(attrs={'class': 'form-control input-group date'}),
            'end_date': forms.TextInput(attrs={'class': 'form-control input-group date'}),
            'summary': forms.Textarea(attrs={'class': 'form-control'}),
            'extra_comments': forms.Textarea(attrs={'class': 'form-control'}),
            #'inc_source': forms.TextInput(attrs={'class': 'form-control'})
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
