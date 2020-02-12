from django.http import HttpResponse
def index1(resquest):
    return HttpResponse('holle word')

# import time
# def about(resquest):
#
#     t = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
#     return HttpResponse(t)

def retaxt(request,id):
    print(id)
    return HttpResponse('我是retaxt')

def mytaxt(request,year,city):
    res = '我%s年在%s' %(year,city)
    print('1234')
    return HttpResponse(res)

from django.template import Template,Context
def indexhtml(request,age):
    """
    编写一个html页面
    :param request:
    :return:
    """
    html = """
    <html>
        <head></head>
        <body>
        <h1>index页面</h1>
        <img src="https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1581409242398&di=5a746b1b15f890ad64b082cbaf767a95&imgtype=0&src=http%3A%2F%2Fimg02.tooopen.com%2Fimages%2F20160125%2Ftooopen_sy_155391981243.jpg">
        </body>
        姓名：{{ name }}
        年龄：{{ age }}
    </html>
    """
    # 返回一个相应对象
    # return HttpResponse(html)
    # # 渲染动态数据
    # 1 创建模板
    moban = Template(html)
    # 2 构建动态数据
    parmas = {'name':'刘亦菲','age':age}
    cont = Context(parmas)
    # 3 构建动态页面，渲染数据
    res = moban.render(cont)
    return HttpResponse(res)

# from django.template.loader import get_template
# def getindex(request):
#     # 第一种方式
#     # 返回页面。返回templates中的index.html页面
#     # 创建一个模板对象
#     templa = get_template('index.html')
#     # 创建一个返回对象  完成一个动态数据渲染
#     params = {'name':'zhangsan','age':19}
#     res = templa.render(params)
#     return HttpResponse(res)

from django.shortcuts import render_to_response
def getindex1(request,age):
    # 第二种方式
    # 返回index页面
    # 返回动态页面
    params = {'name':'lisi','age':age}
    return render_to_response("index.html",params)

from django.shortcuts import render
def getindex(request):
    """
    第三种方式
    :param request:
    :return:
    """
    parmas = {'name':'wangwu','age':20}
    return render(request,'index.html',parmas)


def temptest(request):
    name = 'lisi'
    age = 18
    hobby = ['唱歌','跳舞','LOL']
    score = {'python':100,'java':90,'C':70}
    subject = ('python','java','php')
    myjs = """
    <script>
    alert("myjs")
    </script>
    
    """



    return render_to_response('temptest.html',locals())



def mystatic(request):

    return render_to_response("mystatic.html")


def index(request):

    return render_to_response('index.html')


def about(request):
    return render_to_response('about.html')

def base(request):
    return render_to_response('base.html')

def listpic(request):
    return render_to_response('listpic.html')

def newslistpic(request):
    return render_to_response('newslistpic.html')














