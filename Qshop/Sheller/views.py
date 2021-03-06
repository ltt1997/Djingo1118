from django.shortcuts import render
from django.http import HttpResponseRedirect,HttpResponse,JsonResponse
from .models import *
from django.core.paginator import Paginator
import hashlib
import json
# Create your views here.
## 登陆装饰器
def loginzsq(func):
    def inner(request,*args,**kwargs):
        cookie_email = request.COOKIES.get('email')
        session_email = request.session.get('email')
        if cookie_email and session_email and cookie_email == session_email:

            return func(request,*args,**kwargs)
        else:
            return HttpResponseRedirect('/sheller/login/')
    return inner

## 推出登录
def logout(request):
    reponse = HttpResponseRedirect('/sheller/login/')
    reponse.delete_cookie('email')
    reponse.delete_cookie('email')
    del request.session['email']
    return reponse
## 密码加密
def setPassword(password):
    md5 = hashlib.md5()
    md5.update(password.encode())
    result = md5.hexdigest()
    return result
## 注册
import datetime
def register(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        repassword = request.POST.get('repassword')
        code = request.POST.get("code")
        code_info = CodeInfo.objects.filter(email=email,code=code).order_by("-id").first()
        if email and password and repassword and password == repassword and code:
            if code == code_info.code:
                now_time = datetime.datetime.now()
                create_time = code_info.create_time
                t = (now_time - create_time).total_seconds()
                code_info.delete()
                if t < 120:
                    user_email = regUser.objects.filter(email=email,user_type=0).exists()
                    if user_email:
                        message = '账号已存在'
                    else:
                        regUser.objects.create(email=email,password=setPassword(password),user_type=0)
                        return HttpResponseRedirect('/sheller/login/')
                else:
                    message = "验证码已失效"

            else:
                message = "验证码输入错误"
        else:
            message = '密码或邮箱格式错误'


    return render(request,'sheller/register.html',locals())
## 登录
def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = regUser.objects.filter(email=email,password=setPassword(password),user_type=0).first()
        if user:
            response = HttpResponseRedirect('/sheller/index')
            response.set_cookie("email",user.email)
            response.set_cookie("userid",user.id)
            request.session['email'] = user.email
            return response
        else:
            message = '账号密码输入错误'
    else:
        message ='账号密码为空'
    return render(request,'Sheller/login.html',locals())
from CeleryTask.tasks import test
@loginzsq
def index(request):
    test.delay()
    return render(request,'sheller/index.html')
@loginzsq
def tables(request,status,page=1):
    # goods = Goods.objects.all()
    goods = Goods.objects.filter(goods_status=status,goods_store_id=request.COOKIES.get('userid')).order_by('id')
    goods_obj = Paginator(goods,10)
    goods_list = goods_obj.page(page)
    goods_num = goods_list.number
    start = goods_num - 2
    end = goods_num + 3
    if goods_obj.num_pages < 5:
        start = 1
        end = goods_obj.num_pages + 1
    else:
        if start <= 1:
            start = 1
            end = start + 5
        elif end >= goods_obj.num_pages + 1:
            end = goods_obj.num_pages + 1
            start = end - 5
    page_range = range(start,end)
    return render(request,'sheller/tables.html',locals())

import random


def goods_status(request,id,status):
    goods = Goods.objects.get(id = id)
    if status == 'up':
        goods.goods_status = 1
        goods.save()
    else:
        goods.goods_status = 0
        goods.save()
    url = request.META.get("HTTP_REFERER")
    print(url)
    return HttpResponseRedirect(url)
@loginzsq
def about(request):
    userid = request.COOKIES.get('userid')
    user = regUser.objects.get(id = userid)
    if request.method == 'POST':
        data = request.POST
        user.username = data.get('username')
        user.phone = data.get('phone')
        user.age = int(data.get('age'))
        user.gender = int(data.get('gender'))
        user.address = data.get('address')
        if request.FILES.get("img"):
            user.photo = request.FILES.get("img")

        user.save()
        print(data)


    return render(request,'sheller/about.html',locals())
@loginzsq
def goods_add(request):
    goods_type = GoodsType.objects.all()
    if request.method == 'POST':
        user_id = request.COOKIES.get('userid')
        data = request.POST
        goods = Goods()
        goods.goods_number = data.get("goods_number")
        goods.goods_name = data.get("goods_name")
        goods.goods_price = data.get("goods_price")
        goods.goods_count = data.get("goods_count")
        goods.goods_location = data.get("goods_location")
        goods.goods_safe_date = data.get("goods_safe_date")
        # goods.goods_picture = data.get("goods_number")
        goods.goods_type_id = int(data.get("goods_type"))
        goods.goods_store = regUser.objects.get(id=user_id)
        goods.goods_picture = request.FILES.get("img")
        goods.save()
    return render(request,'sheller/goods_add.html',locals())

from sdk.sendemail import sendemail
import random
def get_code(request):
    res = {"code":10000,"msg":"验证码发送成功"}
    email = request.GET.get('email')
    code = random.randint(1000,9999)
    params = {
        "subject":"天天生鲜",
        "content":"您的验证码为：{}，打死不要告诉别人偶！！！".format(code),
        "recver": email
    }
    sendemail(params)
    code_info = CodeInfo()
    code_info.email = email
    code_info.code = code
    code_info.save()

    return JsonResponse(res)


