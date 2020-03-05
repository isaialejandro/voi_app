from django import forms

from apps.application.models import Application


class ApplicationForm(forms.ModelForm):

    is_for_bajas_semanales = forms.Select()

    class Meta:

        model = Application

        fields = [
            'name',
            'app_type',
            'is_for_bajas_semanales',
        ]

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'app_type': forms.Select(attrs={'class': 'form-control'}),
        }
