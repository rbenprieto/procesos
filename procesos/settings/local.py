from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        "NAME": "procesos",
        "USER": "postgres",
        "PASSWORD": "roma-314",
        "HOST": "localhost",
        "PORT": "5432",
    }
}