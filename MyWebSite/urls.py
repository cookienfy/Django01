from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^(?P<Id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^(?P<Id>[0-9]+)/results/$', views.results, name='results'),
    url(r'^(?P<Id>[0-9]+)/vote/$', views.vote, name='vote'),
]
