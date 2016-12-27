from __future__ import absolute_import, unicode_literals

from .base import *

DEBUG = True

try:
    from .local import *
except ImportError:
    pass

BASE_URL = 'http://localhost.org:9000'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'padawan',
    }
}

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
STATIC_ROOT = os.path.join(BASE_DIR, 'static')