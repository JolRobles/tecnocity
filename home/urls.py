from django.conf.urls import url, include
from . import views
from django.contrib import admin


urlpatterns = [
    url(r'^$', views.mostrar_inicio, name='index'),

]