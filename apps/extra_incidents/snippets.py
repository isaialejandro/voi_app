from django import forms

import django_filters

from apps.extra_incidents.models import ExtraIncident


class ExtraIncidentFilter(django_filters.FilterSet):

    class Meta:
        model = ExtraIncident

        fields = {
            'title',
            'application',
            'type',
            'end_date',
            'inc_source'
        }
