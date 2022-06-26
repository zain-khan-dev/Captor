***REMOVED***
WSGI config for captor project.

It exposes the WSGI callable as a module-level variable named ``application``.

***REMOVED***
https://docs.djangoproject.com/en/4.0/howto/deployment/wsgi/
***REMOVED***

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'captor.settings')

application = get_wsgi_application()
