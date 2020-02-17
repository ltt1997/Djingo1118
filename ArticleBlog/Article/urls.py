from django.urls import path,re_path
from .views import *
urlpatterns = [
    path('index/',index),
    path('about/',about),
    path('listpic/',listpic),
    re_path('newslistpic/(?P<page>\d+)/',newslistpic),
    path('addmany/',addmany),
    path('ft_text/',ft_text),
    re_path('articleinfo/(?P<id>\d*)/',articleinfo),
    # path('articleinfo/',articleinfo),
]




