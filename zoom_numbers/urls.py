from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^monthly_numbers/$', views.monthly_numbers, name = 'monthly_numbers'),
    url(r'^ymca_visits/$', views.ymca_visits, name = 'ymca_visits'),
    url(r'^food_shelf_visits/$', views.food_shelf_visits, name = 'food_shelf_visits'),
    url(r'^ymca/new/$', views.ymca_new, name='ymca_new'),
    url(r'^food_shelf/new/$', views.food_shelf_new, name='food_shelf_new'),
    url(r'^police_calls/$', views.police_calls, name = 'police_calls'),
    url(r'^police_calls/new/$', views.police_calls_new, name = 'police_calls_new'),
    url(r'^questions_of_month/$', views.questions_of_month, name = 'questions_of_month'),
    url(r'^question_month_detail/(?P<pk>\d+)/$', views.question_month_detail, name = 'question_month_detail'),
    url(r'^question_of_month/new/$', views.question_month_new, name = 'question_month_new'),
]