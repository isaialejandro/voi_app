from django import forms

from apps.ticket.models import Ticket, TicketHistory
from apps.application.models import Application


class TicketForm(forms.ModelForm):

    #"application": forms.Select(attrs={'class': 'form-control select2'}),
    application = forms.ModelChoiceField(empty_label=None, \
                queryset=Application.objects.filter(is_active=True, app_type='NORMAL'),\
                widget=forms.Select(attrs={
                'class': 'form-control', 'required': 'required'}))

    class Meta:
        model = Ticket
        fields = [
            "title",
            "folio_number",
            "priority",
            "status",
            "applicant",
            "application",
            "assigned_to",
            "request_type",
            "beneficiary_name",
            "beneficiary_last_name",
            "approval_owner",
            "approval_executor",
            "approve",
            "created_by",
            "item_type",
            "path",
            "description"
        ]

        widgets = {
            "title": forms.TextInput(attrs={'class': 'form-control'}),
            "folio_number": forms.TextInput(attrs={'class': 'form-control'}),
            "priority": forms.Select(attrs={'class': 'form-control select2'}),
            "status": forms.Select(attrs={'class': 'form-control select2'}),
            "applicant": forms.Select(attrs={'class': 'form-control select2'}),
            #"application": forms.Select(attrs={'class': 'form-control select2'}),
            "assigned_to": forms.Select(attrs={'class': 'form-control select2'}),
            "request_type": forms.Select(attrs={'class': 'form-control select2'}),
            "beneficiary_name": forms.TextInput(attrs={'class': 'form-control select2'}),
            "beneficiary_last_name": forms.TextInput(attrs={'class': 'form-control'}),
            "approval_owner": forms.Select(attrs={'class': 'form-control'}),
            "approval_executor": forms.Select(attrs={'class': 'form-control select2'}),
            "approve": forms.Select(attrs={'class': 'form-control select2'}),
            "created_by": forms.TextInput(attrs={'class': 'form-control select2'}),
            "item_type": forms.Select(attrs={'class': 'form-control select2'}),
            "path": forms.TextInput(attrs={'class': 'form-control'}),
            "description": forms.Textarea(attrs={'class': 'form-control'}),
        }

"""
    def clean_field(self):
        data = self.cleaned_data["ticket_code"]
        if len(data)> 10:
            raise forms.ValidationError('Error form')
        return data

    def save(self, commit=True):
        print(self)

        form = super(TicketForm, self).save(commit=False)
        print(form)

        ticket = Ticket.objects.filter(ticket_code=self.ticket_code)

        if not form.ticket_code == ticket:
            if commit:
                form.user = self.request.user
                form.save()
        return form
"""


class TicketUpdateForm(forms.ModelForm):

    class Meta:
        model = Ticket
        fields = [
            "priority",
            "applicant",
            "application",
            "assigned_to",
            "request_type",
            "beneficiary_name",
            "beneficiary_last_name",
            "approval_owner",
            "approval_executor",
            "approve",
            "created_by",
            "item_type",
            "path",
            "description"
        ]

        widgets = {
            "priority": forms.Select(attrs={'class': 'form-control select2'}),
            "applicant": forms.Select(attrs={'class': 'form-control select2'}),
            "application": forms.Select(attrs={'class': 'form-control select2'}),
            "assigned_to": forms.Select(attrs={'class': 'form-control select2'}),
            "request_type": forms.Select(attrs={'class': 'form-control select2'}),
            "beneficiary_name": forms.TextInput(attrs={'class': 'form-control select2'}),
            "beneficiary_last_name": forms.TextInput(attrs={'class': 'form-control'}),
            "approval_owner": forms.Select(attrs={'class': 'form-control'}),
            "approval_executor": forms.Select(attrs={'class': 'form-control select2'}),
            "approve": forms.Select(attrs={'class': 'form-control select2'}),
            "created_by": forms.TextInput(attrs={'class': 'form-control select2'}),
            "item_type": forms.Select(attrs={'class': 'form-control select2'}),
            "path": forms.TextInput(attrs={'class': 'form-control'}),
            "description": forms.Textarea(attrs={'class': 'form-control'}),

        }


class HistoryTicketForm(forms.ModelForm):

    class Meta:
        model = TicketHistory
        fields = [
            "summary"
        ]

        widgets = {
            "summary": forms.Textarea(attrs={'class': 'form-control'})
        }
