"""
URL configuration for gas_project project.

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
from app01.views import data, home, profile, setting, account

urlpatterns = [
    path('home/main/', home.home_main),
    path('home/dashboard/',home.home_dashboard),
    #path('setting/', setting),
    #path('profile/', profile),
    # log in
path('login/',account.login),
path('logout/',account.logout),
path('image/code/', account.image_code),
]
