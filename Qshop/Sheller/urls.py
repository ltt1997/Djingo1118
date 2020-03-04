from django.urls import path,re_path
from .views import *

urlpatterns = [
    path('login/',login),
    path('logout/',logout),
    path('register/',register),
    path('tables/', tables),
    path('index/', index),
    path('about/', about),
    path('goods_add/', goods_add),
    path('get_code/', get_code),
    re_path('tables/(?P<status>\d+)/(?P<page>\d+)/', tables),
    re_path('tables/(?P<id>\d+)/(?P<status>\w+)/', goods_status),

]
