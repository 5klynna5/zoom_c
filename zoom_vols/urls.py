from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^volunteer_home/$', views.volunteer_home, name='volunteer_home'),
    url(r'^volunteers/$', views.volunteer_list, name='volunteer_list'),
    url(r'^volunteer/(?P<pk>\d+)/$', views.volunteer_detail, name='volunteer_detail'),
    url(r'^hours/new/$', views.hours_new, name='hours_new'),
    url(r'^volunteer/new/$', views.volunteer_new, name='volunteer_new'),
    url(r'^volunteer/edit/(?P<pk>\d+)/$', views.volunteer_edit, name='volunteer_edit'),
    url(r'^group_hours/new/$', views.group_hours_new, name='group_hours_new'),
]