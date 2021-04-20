# -*- coding: utf-8 -*-
from .base import *

import dj_database_url



# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

SECRET_KEY = os.getenv('SECRET_KEY')

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

# Cloud Storage
# vSTATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'


# Setup for media files
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR + '/media' #os.path.join(BASE_DIR, '/media/')


DATA_UPLOAD_MAX_NUMBER_FIELDS = 10000 # higher than the count of fields