__author__ = 'xxmmdj'
from django.conf.urls import patterns, url
from Show import views


urlpatterns = patterns('',
    url(r'^$', views.show, name='show'),
)