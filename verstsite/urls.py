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
from user import views as user_url
from django.urls import path, include

urlpatterns = [
    path('', index, name='index'),
    path('captcha/', include('captcha.urls')),
    path('admin/', admin.site.urls),


    # USER URL's

    path('register', user_url.register, name='register'),
    path('logout', user_url.log_out, name='logout'),
    path('cabinet', user_url.cabinet, name='cabinet'),
    path('login', user_url.log_in, name='login'),
    path('my_orders', user_url.my_orders, name='my_orders'),
    path('my_tickets', user_url.my_tickets, name='my_tickets'),
    path('my_paid_transactions', user_url.my_paid_transactions, name='my_paid_transactions'),
    path('my_exchanger_tickets', user_url.my_exchanger_tickets, name='my_exchanger_tickets'),
    path('create_issue', user_url.create_issue, name='create_issue'),
    path('balance', user_url.balance, name='balance'),

    path('check', check, name='check'),
    path('reviews', reviews, name='reviews'),
    path('vacancy', vacancy, name='vacancy'),
    path('contacts', contacts, name='contacts'),
    path('sales', sales, name='sales'),
    path('buy', buy, name='buy'),
    path('choose', choose, name='choose'),
    path('choose1', choose1, name='choose1'),
    path('end', end, name='end'),
    path('add', add, name='add'),
    path('error', tech_work, name='error')
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
