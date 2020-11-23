from django.shortcuts import render

from apps.zendesk.models import ZendeskUserHistory, ZendeskUser
from django.views.generic.list import ListView


class Zendesk(ListView):

    model = ZendeskUser
    template_name = 'active_user_list.html'
    
    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        #context['active_users'] = True
        return context



#class ActiveUsersHist(ListView):