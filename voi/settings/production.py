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

STATIC_URL = '/staticfiles/'
STATIC_ROOT = 'static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "staticfiles"),

]

#For media files
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR + '/media' #os.path.join(BASE_DIR, '/media/')

#Cloud Storage
#STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

DATA_UPLOAD_MAX_NUMBER_FIELDS = 10000 # higher than the count of fields