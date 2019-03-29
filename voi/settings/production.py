from .base import *

import dj_database_url



# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['*']


DATABASES = {
    'default': dj_database_url.config()
    }


#StaticFiles for production
#STATIC_URL = '/staticfiles/'
STATIC_ROOT = 'static/'



#Storage
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'