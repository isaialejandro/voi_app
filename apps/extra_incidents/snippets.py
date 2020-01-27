from django import forms

import django_filters

from apps.extra_incidents.models import ExtraIncident


class ExtraIncidentFilter(django_filters.FilterSet):

    CHOICES = (
        ('asencing', 'Ascending'),
        ('descending', 'Descending'),
    )

    title = django_filters.CharFilter(lookup_expr='icontains')
    date_ordering = django_filters.ChoiceFilter(label='Date Ordering', choices=CHOICES, method='filter_by_date')

    class Meta:
        model = ExtraIncident


        fields = (
            'title',
            'application',
            'type',
            'created_date',
            'end_date',
            'inc_source',
            'finalized',
        )

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
        }

        """
        fields = {
            'title': ['icontains'],
            'application',
            'type',
            'created_date',
            'end_date',
            'inc_source',
            'finalized',
        }
        """

    #Recheck
    def filter_by_date(self, queryset, name, value):

        expression = 'created_date' if value == 'ascending' else '-created_date'
        return queryset.order_by(expression)
