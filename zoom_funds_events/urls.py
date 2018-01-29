from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^events_list/$', views.events_list, name='events_list'),
    url(r'^event_new/$', views.event_new, name='event_new'),
    url(r'^grants_list/$', views.grants_list, name='grants_list'),
    url(r'^grant_new/$', views.grant_new, name='grant_new'),
]