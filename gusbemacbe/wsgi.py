"""
WSGI config for gusbemacbe project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""

import os
from django.core.wsgi import get_wsgi_application
from whitenoise.django import DjangoWhiteNoise

# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "{{ project_name }}.settings")
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gusbemacbe.settings')

application = get_wsgi_application()
application = DjangoWhiteNoise(application)
