from django.urls import path
from .views import *


urlpatterns =[
    path('index/',index),
    path('adduser/',adduser),
    path('getuser/',getuser),
    path('updateuser/',updateuser),
    path('deleteuser/',deleteuser),
    path('dou_line/',dou_line),
]