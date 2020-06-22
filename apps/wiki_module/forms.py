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
            'blog_tags',
            'status'
        ]

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control select2'}),
            'description': forms.TextInput(attrs={'class': 'form-control select2'}),
            'content': forms.TextInput(attrs={'class': 'form-control select2'}),
        }
