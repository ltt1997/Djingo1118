from django.shortcuts import render,render_to_response
from django.http import HttpResponse
from django.core.paginator import Paginator



# Create your views here.
from .models import *
def index(request):
    return render_to_response('index.html')
def about(request):
    return render_to_response('about.html')
def listpic(request):
    return render_to_response('listpic.html')

def newslistpic(request,page):
    article = Article.objects.all().order_by('id')
    pagnitor_obj = Paginator(article,6)
    page_obj = pagnitor_obj.page(page)
    page_num = page_obj.number
    if pagnitor_obj.num_pages <= 5:
        page_range = pagnitor_obj.page_range
    else:
        start = page_num - 2
        end = page_num + 3
        if start <= 1:
            start = 1
            end = start + 5
        elif end >= pagnitor_obj.num_pages:
            end = pagnitor_obj.num_pages
            start = end - 5

        # page_range = pagnitor_obj.page_range[start:end]
        page_range = range(start,end)



    article = Article.objects.all()



    return render_to_response('newslistpic.html',locals())

def articleinfo(request,id):
    article = Article.objects.get(id = id)

    return render_to_response('articleinfo.html',locals())

def addmany(request):
    # for i in range(100):
    #     article = Article()
    #     article.title = 'titlt_% s'% i
    #     article.content = 'content_% s'% i
    #     article.description = 'description_% s'% i
    #     article.author = Author.objects.get(id=1)
    #     article.save()
    #     article.type.add(Type.objects.get(id=2))
    #     article.save()
    Article.objects.filter(author_id=1).delete()

    return HttpResponse('加入多条数据')


def ft_text(request):
    ## 查询文章方法
    article = Article.objects.all().order_by('id')
    # print(article)
    ## paginator
    paginator_obj = Paginator(article,10)
    # print(paginator_obj)   # 对象
    # print(paginator_obj.count)  # 数据条数
    # print(paginator_obj.num_pages)  # 总共分了多少页
    # print(paginator_obj.page_range)   # 可迭代的总页数
    page_obj = paginator_obj.page(4)  ## 第几页的数据，可迭代
    print(page_obj)  #  <Page 1 of 11>
    # for i in page_obj:   # 便利可得到分页的数据
    #     print(i)
    print(page_obj.has_next())   ## 是否有下一页  返回 True 或 False
    print(page_obj.has_previous())  ## 是否有上一页 返回 True 或 False
    print(page_obj.number)    # 当前所在的页码
    print(page_obj.previous_page_number()) ## 上一页的页码
    print(page_obj.next_page_number()) ## 下一页的页码
    print(page_obj.has_other_pages())  ## 是否有其他页 返回 True 或 False



    return HttpResponse('分页')

