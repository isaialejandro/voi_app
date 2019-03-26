from django import forms

from apps.sox.models import SOXRegistry


class SOXForm(forms.ModelForm):
    
    class Meta:
        model = SOXRegistry
        fields = [
            'folio_number',
            'application',
            'request_type',
            'affected_user',
            'executor',
            'execution_date',
            'status',
            'sent_email_to_exec',
            'confirmed_by_exec',
            'exec_confirmed_date',
            'first_source',
            'first_source_date',
            'first_source_executor',
            'second_source',
            'second_source_date',
            'second_source_executor',
        ]
    
        widgets = {
            'folio_number': forms.TextInput(attrs={'class': 'form-control'}),
            'application': forms.Select(attrs={'class': 'form-control'}),
            'request_type': forms.Select(attrs={'class': 'form-control'}),
            'affected_user': forms.TextInput(attrs={'class': 'form-control'}),
            'executor': forms.Select(attrs={'class': 'form-control'}),
            'execution_date': forms.TextInput(attrs={'class': 'form-control exec-date'}),
            'status' : forms.Select(attrs={'class': 'form-control'}),
            'sent_email_to_exec': forms.Select(attrs={'class': 'form-control'}),
            'confirmed_by_exec': forms.Select(attrs={'class': 'form-control'}),
            'exec_confirmed_date': forms.TextInput(attrs={'class': 'form-control'}),
            'first_source': forms.Select(attrs={'class': 'form-control'}),
            'first_source_date': forms.TextInput(attrs={'class': 'form-control'}),
            'first_source_executor': forms.Select(attrs={'class': 'form-control'}),
            'second_source': forms.Select(attrs={'class': 'form-control'}),
            'second_source_date': forms.TextInput(attrs={'class': 'form-control'}),
            'second_source_executor': forms.Select(attrs={'class': 'form-control'}),
        }
