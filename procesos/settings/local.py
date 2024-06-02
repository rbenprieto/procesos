from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        "NAME": os.environ.get("NAME_PROCESOS"),
        "USER": os.environ.get("USER_PROCESOS"),
        "PASSWORD": os.environ.get("PASSWORD_PROCESOS"),
        "HOST": os.environ.get("HOST_PROCESOS"),
        "PORT": os.environ.get("PORT_PROCESOS")
    }
}