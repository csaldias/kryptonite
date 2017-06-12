from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^search/$', views.searchPage, name='search'),
    url(r'^search/results/$', views.searchResults, name='results'),
]
