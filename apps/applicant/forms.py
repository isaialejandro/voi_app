from django import forms

from apps.applicant.models import Applicant

class ApplicantForm(forms.ModelForm):
    class Meta:
        model = Applicant

        fields = [
            'first_name',
            'last_name',
            'email'
        ]
    
        widgets =  {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
        }