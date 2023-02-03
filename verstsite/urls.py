"""verstsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.conf.urls.static import static
from django.conf import settings
from .views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('register', register, name='register'),
    path('login', log_in, name='login'),
    path('check', check, name='check'),
    path('reviews', reviews, name='reviews'),
    path('vacancy', vacancy, name='vacancy'),
    path('contacts', contacts, name='contacts'),
    path('sales', sales, name='sales'),
    path('buy', buy, name='buy'),
    path('choose', choose, name='choose'),
    path('choose1', choose1, name='choose1'),
    path('end', end, name='end'),
    path('add', add, name='add')
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
