from .base import *

import dj_database_url



# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


DATABASES = {
    'default': dj_database_url.config()
    }


#StaticFiles for production
#STATIC_URL = '/staticfiles/'

STATIC_ROOT = '/staticfiles/'
STATIC_URL = '/static/'


#Cloud Storage
#STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'