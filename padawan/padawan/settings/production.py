from __future__ import absolute_import, unicode_literals

from .base import *

DEBUG = False

try:
    from .local import *
except ImportError:
    pass

BASE_URL = 'https://padawan.herokuapp.com'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'project_title_db',
    }
}