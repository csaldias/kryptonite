from django.conf.urls import url
from django.contrib import admin

from . import views

app_name = 'bentobox'
admin.site.site_header = 'Panel de Administracion'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^search/$', views.searchPage, name='search'),
    url(r'^register/$', views.register, name='register'),
    url(r'^search/results/$', views.searchResults, name='results'),
]
