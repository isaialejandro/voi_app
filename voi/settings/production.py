from .base import *

import dj_database_url



# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['*']


DATABASES = {
    'default': dj_database_url.config()
    }


# STatic files setup for Production ENV:
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),

]

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'


#For media files
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR + '/media' #os.path.join(BASE_DIR, '/media/')

#Cloud Storage
#STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

DATA_UPLOAD_MAX_NUMBER_FIELDS = 10000 # higher than the count of fields