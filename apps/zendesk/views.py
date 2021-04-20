from django.shortcuts import render

from apps.zendesk.models import ZendeskUserHistory, ZendeskUser
from django.views.generic.list import ListView

from apps.tools.mixins import LoginRequiredMixin, NeverCacheMixin, \
    PermissionRequiredMixin, CSRFExemptMixin

class Zendesk(LoginRequiredMixin, NeverCacheMixin, \
                PermissionRequiredMixin, CSRFExemptMixin, ListView):

    model = ZendeskUser
    template_name = 'active_user_list.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        #context['active_users'] = True
        return context
