import os
from .base import *


DEBUG = False

ALLOWED_HOSTS = ['*']


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases


#Raspberry Local
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'voireg_db',
        'HOST': '192.168.0.25',
        'USER': 'voireg_admin',
        'PORT': '5432',
        'PASSWORD': 'mario bross 2',
    }
}


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

#STATIC_URL = '/static/'
STATIC_URL = '/voi/staticfiles/'
STATIC_ROOT = os.path.join(os.path.dirname(BASE_DIR), "static")
#Indica la ruta para cargar la carpeta  static en el ambiente local.
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "staticfiles"),

]
