"""
WSGI config for mikuna project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/howto/deployment/wsgi/
"""

import os
import sys

app_path=os.path.realpath(os.path.dirname(__file__) + '/../')
sys.path.append(app_path)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mikuna.settings")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
