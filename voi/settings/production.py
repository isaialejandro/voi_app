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
STATIC_URL = '/staticfiles/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "staticfiles"),

]

#Cloud Storage
#STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'