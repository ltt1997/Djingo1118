from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .models import User
def index(request):
    return HttpResponse('app index')

def adduser(request):
    #   增加数据  save
    # 第一种方法
    user = User()
    user.name = 'lisi'
    user.age = 20
    user.phone = '12301010101'
    user.email = 'lisi@qq.com'
    user.save()
    # 第二种方法
    user = User(name='zhangsan',age=20,phone='12302020202',email='zhangsan')
    user.save()
    # create 增加数据
    # 第一种
    User.objects.create(name='wangwu',age=31,phone='12303030303',email='wangwu@qq.com')
    # 第二种
    params = dict(name='zhaoliu',age=19,phone='12304040404',email='zhaoliu@qq.com')
    User.objects.create(**params)
    return HttpResponse('add user')

def getuser(request):
    ## all() 方法，返回所有符合条件的数据
    ## 返回类型 Queryset
    # user = User.objects.all()
    # print(user)
    # print(user[0].name)
    # for i in user:
    #     print(i)
    #     print(i.name)
    ## get 方法 ，返回符合条件的数据
    ## 返回类型 对象
    # 没有数据会报错，返回多条数据会报错
    #get方法只能获取存在的数据，只能返回一条
    # 一般情况下，get后面跟的参数为(id)
    # user = User.objects.get(id = 3)
    # print(user)
    # print(user.name,user.age)
    ## filter 过滤筛选
    # 返回符合条件的所有数据
    #返回值为 queryset
    ## 相当于sql里边的where条件查询 select * from user where ...
    # user = User.objects.filter(age = 20,id = 2)
    # print(user)
    # print(user[0].name)
    ## exclude  和 filter相反
    # 返回不符合条件的数据
    # 返回值为 queryset
    # user = User.objects.exclude(age = 20)
    # print(user)

    ## first  返回符合条件的第一条数据
    ## 返回类型 对象
    # user = User.objects.exclude(age = 20).first()
    # print(user)

    ## last  返回符合条件的最后一条数据
    ## 返回类型 对象
    # user = User.objects.exclude(age = 20).last()
    # print(user)

    ## order_by  排序
    # 升序
    # user = User.objects.filter(age = 20).order_by("id").first()
    # print(user)
    # 降序
    # user = User.objects.filter(age = 20).order_by("-id").first()
    # print(user)
    ## reverse 反转
    ## 返回结果    queryset
    # reverse 使用条件  reverse之前必须是排序过的数据
    # 如果未排序，reverse不生效
    # user = User.objects.order_by('age').reverse()
    # print(user)
    # user = User.objects.order_by('age'),all()
    # print(user)

    # values
    # 返回的是queryset   以字典的形式储存在queryset（结果集）里
    ## select * from user;
    # user = User.objects.values()
    # print(user)
    # ## select name,age from user;
    # user = User.objects.values("name",'age')
    # print(user)
    # ## 等同于where条件语句
    # user = User.objects.filter(age=20).values()
    # print(user)


    ## count 计数
    # 返回的值是数字类型
    # num = User.objects.filter(age=20).count()
    # print(num)


    # exists   判断数据是否存在
    # 返回的值类型是布尔类型  True    False
    # res = User.objects.filter(age=20).exists()
    # print(res)


    ## 切片  类似于MySQL中的分页【limit】
    #   与python种切片规则相同

    user = User.objects.all()[1:2]
    print(user)

    return HttpResponse('get user')

def updateuser(request):
    # save
    ## 更新数据
    # user = User.objects.get(id=2)
    # user.name = '小黑'
    # user.save()
    # user = User.objects.filter(age=20).all()  ## 返回值是queryset
    # for i in user:
    #     i.phone = '110'
    #     i.save()
    # # update
    User.objects.filter(id=7).update(name='Lisi')

    ## update 和save 都可以完成数据的更新，但用的地方不一样
    # update 属于queryset的fangfa
    #         queryset.update(属性=newvalue)
    # save 属于对象的方法
    #          先获取到对象   对象.save()

    return HttpResponse('update user')

def deleteuser(request):
    ## delete 删除
    User.objects.filter(id=5).delete()  ## filter 返回值是queryset

    User.objects.get(id=6).delete()  ## get 返回值是对象
    """
    在对象和queryset  中都有deletefangfa
    """
    return  HttpResponse('delete user')

def dou_line(request):
    # 上下划线查询
    # __lt   小于
    # user = User.objects.filter(age__lt=22)
    # for i in user:
    #     print(i.name)
    # __gt   大于
    # user = User.objects.filter(id__gt=8)
    # print(user)
    # __lte  小于等于 用法与__lt相同
    # __gte  大于等于 用法与__gt相同
    # __in   范围查询
    # user = User.objects.filter(age__in=[20,21,22]).all()
    # print(user)
    # exclude(属性__in=[])  等同于 not in
    # user = User.objects.exclude(age__in=[20,21,22])
    # print(user)
    """ 模糊查询"""
    # # __contains 类似于MySQL中 like
    # 区分大小写
    # user = User.objects.filter(name__contains='li')
    # print(user)
    #
    # # __icontains  加i不区分大小写
    # user = User.objects.filter(name__icontains='li')
    # print(user)

    # __startwith
    # 查询开头  区分大小写
    # user = User.objects.filter(name__startswith='li')
    # print(user)


    # __istartwith
    # 不区分大小写  iXXXX
    # user = User.objects.filter(name__istartswith='li')
    # print(user)
    # __endwith
    # 查询结尾 区分大小写
    # __iendwith
    # 查询结尾 不区分大小写
    return HttpResponse('双下划线方法')



