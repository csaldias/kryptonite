from django.conf.urls import url
from django.contrib import admin

from . import views

app_name = 'bentobox'
admin.site.site_header = 'Panel de Administracion'

urlpatterns = [
    url(r'^$', views.searchPage, name='index'),
    url(r'^login/$', views.login, name='login'),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^search/$', views.searchPage, name='search'),
    url(r'^register/$', views.register, name='register'),
    url(r'^search/results/$', views.searchResults, name='results'),
    url(r'^sugerir/$', views.sugerirContenido, name='sugerir'),
]
