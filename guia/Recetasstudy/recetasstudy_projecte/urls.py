"""recetasstudy_projecte URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from recetasstudy_app import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('recetas', views.recetas , name= 'recetas'),
    path('pizza', views.pizza, name='pizza'),
    path('canelons', views.canelons, name='canelons'),
    path('gazpacho', views.gazpacho, name='gazpacho'),
    path('calabacin', views.calabacin, name='calabacin'),
    path('ensaladilla', views.ensaladillarusa, name='ensaladilla'),
    path('carbonara', views.carbonaraspecial, name='carbonara'),
    path('sopa', views.sopa, name='sopa'),
    path('mafe', views.mafespecial, name='mafe'),
    path('feijoada', views.feijoadaspecial, name='feijoada'),
    path('menuinfantil', views.menuinfantil, name='menuinfantil'),
]