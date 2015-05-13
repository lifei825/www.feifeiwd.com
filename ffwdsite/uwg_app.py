#!/usr/bin/python
import sys 
import os
 
sys.path.append(os.path.abspath(os.path.dirname(__file__)))
os.environ['DJANGO_SETTINGS_MODULE'] = 'ffwdsite.settings'
 
#import django.core.handlers.wsgi
from django.core.wsgi import get_wsgi_application 
application = get_wsgi_application()
