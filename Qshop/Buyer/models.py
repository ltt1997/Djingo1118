from django.db import models
from Sheller.models import *

# Create your models here.

ORDER_STATUS = (
    (1,'未支付'),
    (2,'已支付'),
    (3,'待发货'),
    (4,'已发货'),
    (5,'拒收'),
    (6,'已完成'),
)

class PayOrder(models.Model):
    order_number = models.CharField(max_length=36,verbose_name='订单编号',unique=True)
    order_data = models.DateField(auto_now=True,verbose_name='时间')
    order_status = models.IntegerField(choices=ORDER_STATUS,verbose_name='订单状态')
    order_total = models.FloatField(verbose_name='点单总金额')
    order_user = models.ForeignKey(to=regUser,on_delete=models.CASCADE,verbose_name='买家')
    class Meta:
        db_table = 'pay_order'


class OrderInfo(models.Model):
    order = models.ForeignKey(to=PayOrder,on_delete=models.CASCADE)
    goods = models.ForeignKey(to=Goods,on_delete=models.CASCADE)
    goods_price = models.FloatField(verbose_name='商品价格')
    goods_count = models.IntegerField(verbose_name='商品数量')
    goods_total_price = models.IntegerField(verbose_name='订单总金额')
    store = models.ForeignKey(to=regUser,on_delete=models.CASCADE,verbose_name='卖家')
    class Meta:
        db_table = 'order_info'

class Cart(models.Model):
    goods = models.ForeignKey(to=Goods,on_delete=models.CASCADE)
    goods_number = models.IntegerField(verbose_name='商品数量')
    goods_total  = models.FloatField(verbose_name='商品价格')
    cart_user = models.ForeignKey(to=regUser,on_delete=models.CASCADE,verbose_name='买家')
    class Meta:
        db_table = 'cart'



class UserAdress(models.Model):
    user_name = models.CharField(max_length=16,verbose_name="收件人")
    adress = models.TextField(verbose_name="详细地址")
    zip_code = models.CharField(max_length=8,verbose_name='邮编')
    phone = models.CharField(max_length=11,verbose_name='手机号')
    user = models.ForeignKey(to=regUser,on_delete=models.CASCADE)
    adress_status = models.IntegerField(default=1,verbose_name="当前地址状态")  ## 0 当前地址 1 未使用地址
    class Meta:
        db_table = 'user_adress'

