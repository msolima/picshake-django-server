#!/usr/bin/env python2.6
import sys,os
# Tell Passenger to run our virtualenv python
INTERP = "/home/picshare/djangoenv/bin/python"
if sys.executable != INTERP: os.execl(INTERP, INTERP, *sys.argv)
# Setup paths and environment variables
sys.path.append(os.getcwd())
os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'
# Set the application
import django.core.handlers.wsgi
from paste.exceptions.errormiddleware import ErrorMiddleware
application = django.core.handlers.wsgi.WSGIHandler()
# Use paste to display errors
application = ErrorMiddleware(application, debug=True)
