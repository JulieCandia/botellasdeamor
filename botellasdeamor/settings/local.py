from .base import *


SECRET_KEY = 'django-insecure-j%(l#uu#_e8q6fr(9vhwkcbo$f-+6r=aeflqb#4ucyt1psc9oq'


DEBUG = True

ALLOWED_HOSTS = ['*']


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
