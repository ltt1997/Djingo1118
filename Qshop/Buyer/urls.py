from django.urls import path,include
from .views import *

urlpatterns = [
    path('index/',index),
    path('register/',register),
    path('login/',login),
    path('logout/',logout),
    path('base/',base),
    path('cart/',cart),
    path('place_order/',place_order),
    path('goods_detail/',goods_detail),
    path('goods_list/',goods_list),
    path('user_center_info/',user_center_info),
    path('user_center_order/',user_center_order),
    path('user_center_site/',user_center_site),
    path('alipay_order/',alipay_order),
    path('pay_status/',pay_status),
    path('add_cart/',add_cart),
    path('change_cart/',change_cart),
    path('cart_place_order/',cart_place_order),
]
