***REMOVED***
ASGI config for captor project.

It exposes the ASGI callable as a module-level variable named ``application``.

***REMOVED***
https://docs.djangoproject.com/en/4.0/howto/deployment/asgi/
***REMOVED***

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'captor.settings')

application = get_asgi_application()
