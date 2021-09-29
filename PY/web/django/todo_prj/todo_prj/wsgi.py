"""
WSGI config for todo_prj project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""

import os

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'todo_prj.settings')
os.environ['DJANGO_SETTINGS_MODULE'] = 'todo_prj.settings'

from django.core.wsgi import get_wsgi_application
# from django.contrib.auth.handlers.modwsgi import check_password


application = get_wsgi_application()
