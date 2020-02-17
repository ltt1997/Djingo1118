from django.urls import path
from .views import *


urlpatterns =[
    path('index/',index),
    path('adduser/',adduser),
    path('getuser/',getuser),
    path('updateuser/',updateuser),
    path('deleteuser/',deleteuser),
    path('dou_line/',dou_line),
    path('addmany/',addmany),
    path('getmany/',getmany),
    path('updatemany/',updatemany),
    path('deletemany/',deletemany),
    path('addduo/',addduo),
    path('getduo/',getduo),
    path('updateduo/',updateduo),
    path('deleteduo/',deleteduo),
    path('juhe/',juhe),
]