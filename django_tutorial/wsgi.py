"""
WSGI config for django_tutorial project.
<<<<<<< HEAD
It exposes the WSGI callable as a module-level variable named ``application``.
=======

It exposes the WSGI callable as a module-level variable named ``application``.

>>>>>>> bc6295723152e1e860cfa52200c992f903c3e498
For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_tutorial.settings')

application = get_wsgi_application()
