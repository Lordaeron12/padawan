"""
WSGI config for padawan project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/howto/deployment/wsgi/
"""

from __future__ import absolute_import, unicode_literals

import os

from raven.contrib.django.raven_compat.middleware.wsgi import Sentry
from django.core.wsgi import get_wsgi_application

application = Sentry(get_wsgi_application())
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "padawan.settings.production")

application = Sentry(get_wsgi_application())
