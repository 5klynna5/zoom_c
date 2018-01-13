from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name = 'home'),
    url(r'^activities/$', views.activities_list, name='activities_list'),
    url(r'^activity/(?P<pk>\d+)/$', views.activity_detail, name='activity_detail'),
    url(r'^activity/new/$', views.activity_new, name='activity_new'),
    url(r'^activity/(?P<pk>\d+)/add_attendance/$', views.attendance_new, name = 'attendance_new'),
    url(r'^activity/(?P<pk>\d+)/add_child_attendance/$', views.child_attendance_new, name = 'child_attendance_new'),
    url(r'^households/$', views.household_list, name='household_list'),
    url(r'^past_households/$', views.past_household_list, name='past_household_list'),
    url(r'^household/new/$', views.household_new, name='household_new'),
    url(r'^resident/(?P<pk>\d+)/$', views.resident_detail, name='resident_detail'),
    url(r'^goal/(?P<pk>\d+)/$', views.goal_detail, name='goal_detail'),
    url(r'^child/(?P<pk>\d+)/$', views.child_detail, name='child_detail'),
    url(r'^goal/(?P<pk>\d+)/new/$', views.goal_new, name='goal_new'),
    url(r'^goal/(?P<pk>\d+)/add_progress/$', views.add_progress, name="add_progress"),
    url(r'^household/(?P<pk>\d+)/add_resident/$', views.resident_new, name = 'resident_new'),
    url(r'^household/(?P<pk>\d+)/add_child/$', views.child_new, name = 'child_new'),
    url(r'^household/(?P<pk>\d+)/exit_interview/$', views.exit_new, name = 'exit_new'),
    url(r'^resident/edit/(?P<pk>\d+)/$', views.resident_edit, name = 'resident_edit'),
    url(r'^household/edit/(?P<pk>\d+)/$', views.household_edit, name = 'household_edit'),
    url(r'^resident/(?P<pk>\d+)/add_permissions/$', views.permissions_new, name = 'permissions_new'),
    url(r'^activity/(?P<pk>\d+)/$', views.activity_follow_up, name='activity_follow_up'),
]