from __future__ import absolute_import, unicode_literals

from .base import *

DEBUG = True

SECRET_KEY = '3rsf0d&@7@in(ia4k%dyhrde(birxw2dn-_l$#y#wqz_qnkqgr'


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