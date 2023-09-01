# asgi.py:
# 1.) Steht für "Asynchronous Server Gateway Interface".
# 2.) Ist eine Spezifikation ähnlich zu WSGI, aber sie unterstützt Asynchronität (z.B. WebSockets, HTTP2).
# 3.) In Django-Projekten dient asgi.py als Einstiegspunkt für Server, die asynchrone Funktionen unterstützen, wie z.B. Daphne oder Uvicorn.


"""
ASGI config for django_chat_app project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_chat_app.settings')

application = get_asgi_application()
