from django import forms

from apps.applicant.models import Applicant

class ApplicantForm(forms.ModelForm):
    class Meta:
        model = Applicant

        fields = [
            'first_name',
            'frst_lastname',
            'scnd_lastname',
            'email'
        ]

        widgets =  {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'frst_lastname': forms.TextInput(attrs={'class': 'form-control'}),
            'scnd_lastname': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
        }
