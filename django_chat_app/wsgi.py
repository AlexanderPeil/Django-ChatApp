# wsgi.py:
# 1.) Steht für "Web Server Gateway Interface".
# 2.) Ist ein Standard für Python-Webanwendungen, um mit Webservern zu kommunizieren.
# 3.) In Django-Projekten dient wsgi.py als Einstiegspunkt, damit Webserver wie Apache, Nginx usw. die Django-Anwendung bedienen können.


"""
WSGI config for django_chat_app project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_chat_app.settings')

application = get_wsgi_application()
