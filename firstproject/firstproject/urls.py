"""firstproject  Configuration

The `patterns` list routes s to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/s/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a  to patterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a  to patterns:  path('', Home.as_view(), name='home')
Including another conf
    1. Import the include() function: from django.s import include, path
    2. Add a  to patterns:  path('blog/', include('blog.s'))
"""
from django.contrib import admin
from django.urls import path
import wordcounter.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', wordcounter.views.home, name="home"),
    path('/about', wordcounter.views.about, name="about"),
    path('/count', wordcounter.views.count, name="count"),
    path('/select', wordcounter.views.select, name="select"),
]
