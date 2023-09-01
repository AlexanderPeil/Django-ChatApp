# urls.py:
# 1.) Definiert URL-Muster für das Django-Projekt oder eine Django-App.
# 2.) Jedes Muster wird einer bestimmten Ansichtsfunktion oder -klasse zugeordnet.
# 3.) Erlaubt es, benutzerfreundliche URLs zu erstellen und zu steuern, welcher Code ausgeführt wird, wenn ein bestimmter Pfad in der URL angefordert wird.



"""
URL configuration for django_chat_app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from chat.views import index, login_view, signup_view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('chat/', index, name='chat'),
    path('login/', login_view, name='login'),
    path('signup/', signup_view, name='signup'),
]
