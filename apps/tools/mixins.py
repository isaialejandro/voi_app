from django.utils.decorators import method_decorator

from django.contrib.auth.decorators import login_required, permission_required

from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_exempt

from django.views import View


class LoginRequiredMixin(object):
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(LoginRequiredMixin, self).dispatch(*args, **kwargs)


class PermissionRequiredMixin(object):
    @method_decorator(permission_required)
    def dispatch(self, *args, **kwargs):
        return super(PermissionRequiredMixin, self).dispatch(*args, **kwargs)


class NeverCacheMixin(object):
    @method_decorator(never_cache)
    def dispatch(self, *args, **kwargs):
        return super(NeverCacheMixin, self).dispatch(*args, **kwargs)


class CSRFExemptMixin(object):
    @method_decorator(csrf_exempt)
    def dispatch(self, *args, **kwargs):
        return super(CSRFExemptMixin, self).dispatch(*args, **kwargs)
