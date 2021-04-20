# -*- coding: utf-8 -*-
import os
from .base import *

SECRET_KEY = os.getenv('VOI_SECRET')

DEBUG = True

ALLOWED_HOSTS = ['*']

#DELL Optiplex780 - Local:
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('DEV_DB_NAME'),
        'HOST': os.getenv('DEV_DB_HOST'),
        'USER': os.getenv('DEV_DB_USR'),
        'PORT': os.getenv('DEV_DB_PORT'),
        'PASSWORD': os.getenv('DEB_DB_PWD'),
    }
}


STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "staticfiles"),
]
STATIC_URL = '/voi/staticfiles/'
MEDIA_ROOT = BASE_DIR + '/media' #os.path.join(BASE_DIR, '/media/')
MEDIA_URL = '/media/'
DATA_UPLOAD_MAX_NUMBER_FIELDS = 10000 # higher than the count of fields