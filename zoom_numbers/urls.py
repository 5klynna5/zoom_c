from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^monthly_numbers/$', views.monthly_numbers, name = 'monthly_numbers'),
    url(r'^ymca_visits/$', views.ymca_visits, name = 'ymca_visits'),
    url(r'^food_shelf_visits/$', views.food_shelf_visits, name = 'food_shelf_visits'),
    url(r'^ymca/new/$', views.ymca_new, name='ymca_new'),
]