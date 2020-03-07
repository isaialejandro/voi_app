from django import forms

from django.contrib.auth.models import User

import django_filters

from apps.bajas_semanales.models import BajaSemanal, TipoBaja


class BajaSemanalFilter(django_filters.FilterSet):

    subject = django_filters.CharFilter(lookup_expr='icontains')
    user_code = django_filters.CharFilter(lookup_expr='icontains')
    user_name = django_filters.CharFilter(lookup_expr='icontains')
    #request_date = django_filters.NumberFilter()
    #user #exclude Administrador


    class Meta:
        model = BajaSemanal

        fields = [
            'type',
            'subject',
            'user_code',
            'user_name',
            'request_date',
            'created_date',
            'already_checked',
            'user',
            'last_user_update'
        ]
