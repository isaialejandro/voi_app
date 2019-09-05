from django import forms

from apps.applicant.models import Applicant

class ApplicantForm(forms.ModelForm):
    class Meta:
        model = Applicant

        fields = [

            'first_name',
            'second_name',
            'first_lastname',
            'second_lastname',
            'email'
        ]

        widgets =  {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'second_name': forms.TextInput(attrs={'class': 'form-control'}),
            'first_lastname': forms.TextInput(attrs={'class': 'form-control'}),
            'second_lastname': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
        }
