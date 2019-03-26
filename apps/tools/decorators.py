from django.utils.decorators import method_decorator

from django.contrib.auth.decorators import login_required

from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_exempt

from django.views import View

#from braces.views import LoginRequiredMixin


class LoginRequiredMixin(object):
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(LoginRequiredMixin, self).dispatch(*args, **kwargs)


class NeverCacheMixin(object):
    @method_decorator(never_cache)
    def dispatch(self, *args, **kwargs):
        return super(NeverCacheMixin, self).dispatch(*args, **kwargs)


class CSRFExemptMixin(object):
    @method_decorator(csrf_exempt)
    def dispatch(self, *args, **kwargs):
        return super(CSRFExemptMixin, self).dispatch(*args, **kwargs)

"""
from braces.views import AccessMixin

class SuperOrManagerPermissionsMixin(AccessMixin):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated():
            return self.handle_no_permission(request)
        if self.user_has_permissions(request):
            return super(SuperOrManagerPermissionsMixin, self).dispatch(
                request, *args, **kwargs)
        raise Http404 #or return self.handle_no_permission

    def user_has_permissions(self, request):
        return self.request.user.is_superuser or self.request.user.is_manage
"""