from  django.conf.urls import url ,include
from .views import *


app_name='blog'


urlpatterns =[



    url(r'^post/$', post, name='post'),
    url(r'^header/$', Header, name='header'),
    url(r'^odeme/$', odeme, name='odeme'),
    url(r'^index/$', index, name='index'),
    url(r'^(?P<id>\d+)/detail/$', detail, name='detail'),
    url(r'^(?P<id>\d+)/update/$', Update, name='update'),
    url(r'^radialmenu/$', radialmenu, name='radialmenu'),

]