from django.conf.urls import patterns, url
from django.conf import settings
from rango import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^about/$', views.about, name='about')
    
    )
    
