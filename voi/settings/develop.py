import os
from .base import *


DEBUG = False

ALLOWED_HOSTS = ['voiregadmin.com']


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases


#Raspberry Local
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'voireg_db',
        'HOST': '192.168.3.151',
        'USER': 'voireg_admin',
        'PORT': '5432',
        'PASSWORD': 'mario bross 2',
    }
}


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_URL = '/home/isai/Django_projects/static/'
STATIC_ROOT = '/home/isai/Django_projects/static'
MEDIA_ROOT = '/home/isai/Django_projects/media'

#STATICFILES_DIRS = [
#    os.path.join(BASE_DIR, "staticfiles"),
#]
