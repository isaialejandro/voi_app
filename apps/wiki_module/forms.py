from django import forms

from pagedown.widgets import PagedownWidget

from apps.wiki_module.models import BlogDoc


class BlogDocForm(forms.ModelForm):

    content = forms.CharField(widget=PagedownWidget)
    publish_date = forms.DateField(widget=forms.SelectDateWidget)

    class Meta:

        model = BlogDoc

        fields = [
            'title',
            'description',
            'content',
            'publish_date',
            'related_tags',
            'status'
        ]

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.TextInput(attrs={'class': 'form-control'}),
            #'related_tags': forms.Select(attrs={'class': 'form-control'}),
        }
