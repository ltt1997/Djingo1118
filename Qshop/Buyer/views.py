from django.shortcuts import render
from django.http import HttpResponseRedirect,HttpResponse,JsonResponse
import hashlib
from django.db.models import Sum


from Sheller.models import *
from .models import *
# Create your views here.

## 登陆装饰器
def loginzsq(func):
    def inner(request,*args,**kwargs):
        cookie_email = request.COOKIES.get('buy_email')
        session_email = request.session.get('buy_email')
        if cookie_email and session_email and cookie_email == session_email:

            return func(request,*args,**kwargs)
        else:
            return HttpResponseRedirect('/login/')
    return inner

## 退出登录
def logout(request):
    reponse = HttpResponseRedirect('/login/')
    reponse.delete_cookie('buy_email')
    reponse.delete_cookie('buy_username')
    reponse.delete_cookie('buy_userid')
    del request.session['buy_email']
    return reponse

## 密码加密
def setPassword(password):
    md5 = hashlib.md5()
    md5.update(password.encode())
    result = md5.hexdigest()
    return result

## 首页
def index(request):
    #  {"type":"新鲜水果.obj","goods":"goods.obj"}
    goods_type = GoodsType.objects.all()
    res = []
    for one in goods_type:
        goods = one.goods_set.order_by('id').all()
        if len(goods) > 0:
            goods_list = goods[:4]
            res.append({'type':one,'goods':goods_list})

    return render(request,'buyer/index.html',locals())

## 注册页面
def register(request):
    if request.method == "POST":
        email = request.POST.get('email')
        username = request.POST.get('user_name')
        password = request.POST.get('pwd')
        repassword = request.POST.get('cpwd')
        if email and password and repassword and password == repassword:
            regUser.objects.create(email=email, password=setPassword(password),username=username)
            return HttpResponseRedirect('/login/')
        else:
            message = '密码或邮箱格式错误'
    return render(request,'buyer/register.html',locals())

##登录页面
def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('pwd')
        user = regUser.objects.filter(username=username,password=setPassword(password),user_type=1).first()
        if user:
            response = HttpResponseRedirect('/')
            response.set_cookie("buy_email",user.email)
            response.set_cookie("buy_username",user.username)
            response.set_cookie("buy_userid",user.id)
            request.session['buy_email'] = user.email
            return response
        else:
            message = '账号密码输入错误'
    else:
        message ='账号密码为空'


    return render(request,'buyer/login.html',locals())

## 商品列表
def goods_list(request):
    goods_name = request.GET.get('goods_name')
    req_type = request.GET.get('req_type')
    if req_type == 'findall':
        goods = Goods.objects.filter(goods_type_id=goods_name)
    else:
        goods = Goods.objects.filter(goods_name__contains=goods_name).all()
    goods_new = Goods.objects.order_by('-goods_pro_time').all()[:2]

    return render(request,'buyer/goods_list.html',locals())

## 商品详情
def goods_detail(request):
    goods_id = request.GET.get('goods_id')
    goods = Goods.objects.get(id = goods_id)
    goods_new = Goods.objects.order_by('-goods_pro_time').all()[:2]
    return render(request,'buyer/goods_detail.html',locals())


## 定单页面
import uuid
def get_order_num():
    number = uuid.uuid4()
    return number



## 订单
@loginzsq
def place_order(request):

    user_id = request.COOKIES.get("buy_userid")
    goods_id = request.GET.get('goods_id')
    goods_count = int(request.GET.get('goods_count'))
    goods = Goods.objects.get(id=goods_id)
    order_info = OrderInfo.objects.filter(goods_id=goods_id).first()
    if order_info and order_info.order.order_user_id == int(user_id) and order_info.order.order_status == 1:
        pay_order = order_info.order
        pay_order.order_number = get_order_num()
        pay_order.order_total = pay_order.order_total + goods.goods_price * goods_count
        pay_order.save()

        order_info.goods_price = goods.goods_price
        order_info.goods_count =  order_info.goods_count + goods_count
        order_info.goods_total_price = order_info.goods_total_price + goods.goods_price * goods_count
        order_info.save()
    else:
        pay_order = PayOrder()
        pay_order.order_number = get_order_num()
        pay_order.order_status = 1
        pay_order.order_total = goods.goods_price * goods_count
        pay_order.order_user_id = int(user_id)
        pay_order.save()

        order_info = OrderInfo()
        order_info.order = pay_order
        order_info.goods = goods
        order_info.goods_price = goods.goods_price
        order_info.goods_count = goods_count
        order_info.goods_total_price = goods.goods_price * goods_count
        order_info.store = goods.goods_store
        order_info.save()




    return render(request,'buyer/place_order.html',locals())

from Qshop.settings import alipay
def alipay_order(request):
    payorder_id = request.GET.get('payorder_id')
    payorder = PayOrder.objects.get(id=payorder_id)
    ## 创建一个订单
    order_str = alipay.api_alipay_trade_page_pay(
        subject='生鲜交易',
        out_trade_no= payorder.order_number,
        total_amount= str(payorder.order_total + 10),
        return_url='http://127.0.0.1:8000/buyer/pay_status/',
        notify_url=None
    )

    res = 'https://openapi.alipaydev.com/gateway.do?' + order_str
    return HttpResponseRedirect(res)

def pay_status(request):
    out_trade_no = request.GET.get("out_trade_no")
    payorder = PayOrder.objects.get(order_number=out_trade_no)
    payorder.order_status = 2
    payorder.save()
    return render(request,"buyer/pay_result.html",locals())

@loginzsq
def cart(request):
    user_id = request.COOKIES.get('buy_userid')
    cart = Cart.objects.filter(cart_user_id=user_id)
    all_total = cart.aggregate(sum_num = Sum('goods_number'),sum_total = Sum('goods_total'))
    return render(request,'buyer/cart.html',locals())


@loginzsq
def add_cart(request):
    res = {"code":10000,"msg":'添加购物车成功'}
    data = request.POST
    user_id = request.COOKIES.get('buy_userid')
    goods_count = int(data.get('goods_count',1))
    goods_id = data.get("goods_id")
    goods = Goods.objects.get(id = goods_id)
    cart = Cart.objects.filter(goods=goods).first()
    if cart:
        cart.goods_number += goods_count
        cart.goods_total = goods.goods_price * (goods_count + cart.goods_number)
    else:
        cart = Cart()
        cart.goods = goods
        cart.goods_number = goods_count
        cart.goods_total = goods.goods_price * goods_count
        cart.cart_user_id = user_id
    try:
        cart.save()
        res = {"code":10000,"msg":'添加购物车成功'}
    except:
        res = {"code": 10001, "msg": '添加购物车失败'}

    return JsonResponse(res)

def base(request):
    return render(request,'buyer/base.html')



def user_center_info(request):
    return render(request,'buyer/user_center_info.html')
def user_center_order(request):
    return render(request,'buyer/user_center_order.html')
def user_center_site(request):
    return render(request,'buyer/user_center_site.html')

def change_cart(request):
    res = {"code":10000,"msg":"计算失败",'data':{}}
    data = request.POST
    # print(data)
    cart_id = data.get("cart_id")
    js_type = data.get('js_type')
    cart = Cart.objects.get(id = int(cart_id))
    if js_type == 'add':
        cart.goods_number += 1
        cart.goods_total += cart.goods.goods_price
    else:
        cart.goods_number -= 1
        cart.goods_total -= cart.goods.goods_price
    cart.save()
    res = {"code":10000,"msg":'操作成功',"data":{"goods_number":cart.goods_number,"goods_total":cart.goods_total}}
    return JsonResponse(res)

def cart_place_order(request):
    data = request.POST
    res = []
    for key,val in data.items():
        print(key,val)
        if key.startswith('cart_id'):
            res.append(val)
    user_id = request.COOKIES.get("buy_userid")
    pay_order = PayOrder()
    pay_order.order_number = get_order_num()
    pay_order.order_status = 1
    pay_order.order_total = 0
    pay_order.order_user_id = int(user_id)
    pay_order.save()
    for one in res:
        cart = Cart.objects.filter(id=one).first()
        order_info = OrderInfo()
        order_info.order = pay_order
        order_info.goods = cart.goods
        order_info.goods_price = cart.goods.goods_price
        order_info.goods_count = cart.goods_number
        order_info.goods_total_price = cart.goods_total
        order_info.store = cart.goods.goods_store
        order_info.save()
        cart.delete()
    payorder_total = pay_order.orderinfo_set.aggregate(sum_total=Sum("goods_total_price")).get("sum_total")
    print(payorder_total)
    pay_order.order_total = payorder_total
    pay_order.save()
    return render(request,'buyer/place_order.html',locals())





