from django.http import HttpResponse
def index(resquest):
    return HttpResponse('holle word')

import time
def about(resquest):

    t = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    return HttpResponse(t)

def retaxt(request,id):
    print(id)
    return HttpResponse('我是retaxt')

def mytaxt(request,year,city):
    res = '我%s年在%s' %(year,city)
    return HttpResponse(res)