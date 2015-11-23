import os
import sys

from django.core.wsgi import get_wsgi_application

# This file is a shim to expose a Django project as a WSGI application that can
# be run by gunicorn or other things that speak WSGI.

here = os.path.dirname(os.path.realpath(__file__))
# add parent dir to path so things like velociraptor.urls will resolve.
sys.path.insert(0, os.path.dirname(here))
os.environ['DJANGO_SETTINGS_MODULE'] = 'vr.server.settings'

app = get_wsgi_application()
