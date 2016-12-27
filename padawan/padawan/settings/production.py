from __future__ import absolute_import, unicode_literals

from .base import *

DEBUG = False

try:
    from .local import *
except ImportError:
    pass

BASE_URL = 'https://www.ugyshop.com'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'padawan',
    }
}

MEDIA_ROOT = os.path.join('/home/django/media')
STATIC_ROOT = os.path.join('/home/django/static')