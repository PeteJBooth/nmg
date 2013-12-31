import os
import sys

from django.core.handlers.wsgi import WSGIHandler

os.environ['DJANGO_SETTINGS_MODULE'] = 'nmg.settings'

sys.path.append('/home/petejbooth/webapps/nmg/nmg')
sys.path.append('/home/petejbooth/webapps/nmg')

application = WSGIHandler()
