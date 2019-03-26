from django import forms

from apps.application.models import Application


class ApplicationForm(forms.ModelForm):

    class Meta:
        model = Application

        fields = [
            'name',
            'app_type',
        ]

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'app_type': forms.Select(attrs={'class': 'form-control'}),
        }