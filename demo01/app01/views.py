from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .models import *
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
    # 双下划线查询
    # __lt   小于  less than（小于）
    # user = User.objects.filter(age__lt=22)
    # for i in user:
    #     print(i.name)
    # __gt   大于  greater than（大于）
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

def addmany(request):
    # Publish.objects.create(name='北京出版社',address='北京')
    # Publish.objects.create(name='上海出版社',address='上海')
    # Publish.objects.create(name='天津出版社',address='天津')
    # 第一种方法
    # 不推荐使用
    # Book.objects.create(name='python入门',money=50,pub_id=2)
    # 第二种方法
    # 正向 从外键所在表到关联表
    # pub_obj = Publish.objects.filter(name='北京出版社').first()
    # Book.objects.create(name='python全栈',money=78,pub=pub_obj)
    # 反向 从关联表到外键所在的表
    # pub_obj = Publish.objects.filter(name='北京出版社').first()
    # pub_obj.book_set.create(name='python web',money=45)
    # pub_obj = Publish.objects.filter(name='上海出版社').first()
    # pub_obj.book_set.create(name='java开发',money=88)
    # pub_obj = Publish.objects.filter(name='天津出版社').first()
    # pub_obj.book_set.create(name='python爬虫',money=73)



    return HttpResponse("一对多增加数据")

def getmany(request):
    # 正向  从外键所在表到关联表
    # 查询python入门是那个出版社出版的
    # book_obj = Book.objects.filter(name='python入门').values()
    # pub_obj = book_obj
    # print(pub_obj)


    # 反向  从关联表到外键所在表
    # 查询北京出版社出版了那些书籍
    pub_obj = Publish.objects.filter(name='北京出版社').first()
    book_obj = pub_obj.book_set.values('name')
    print(book_obj)
    return HttpResponse('一对多查询')

def updatemany(request):
    # 一对多关系修改
    # update
    # 使用 obj.id
    # pub_obj = Publish.objects.filter(name='上海出版社').first()
    # Book.objects.filter(name='python全栈').update(pub_id=pub_obj.id)
    # 正向 update
    # 修改书籍的出版社
    # pub_obj = Publish.objects.filter(name='天津出版社').first()
    # Book.objects.filter(name='python入门').update(pub=pub_obj)
    # 反向  set
    # 修改出版社里的书籍
    # pub_obj = Publish.objects.filter(name='上海出版社').first()
    # book_obj = Book.objects.filter(name='java入门').first()
    # pub_obj.book_set.set([book_obj])
    # 一次修改多个
    pub_obj = Publish.objects.filter(name='天津出版社').first()
    book_obj1 = Book.objects.filter(name='java入门').first()
    book_obj2 = Book.objects.filter(name='java开发').first()
    book_obj = Book.objects.filter(name='python web').first()
    pub_obj.book_set.set([book_obj,book_obj1,book_obj2])


    return HttpResponse('一对多修改')

def deletemany(request):
    ## 删除
    #  由于设置了on_delete = models.CASCADE 删除关联表的数据试试
    # 会将表中关联的数据一起删除
    # Publish.objects.filter(name='上海出版社').delete()
    Book.objects.filter(name='java开发').delete()


    return HttpResponse('一对多删除')

def addduo(request):
    # 增加数据
    # Person.objects.create(name='小明',age=15)
    # Person.objects.create(name='小红',age=22)
    # Person.objects.create(name='小美',age=16)
    # Person.objects.create(name='小黄',age=18)
    # Teacher.objects.create(name='老李',gender=1,age=42)
    # Teacher.objects.create(name='老刘',gender=1,age=52)
    # Teacher.objects.create(name='吴老师',gender=0,age=26)
    # Teacher.objects.create(name='老赵',gender=1,age=32)
    # add  增加数据关系
    # 针对已存在的数据增加数据
    # 正向
    # per_obj= Person.objects.filter(name='小明').first()
    # tea_obj = Teacher.objects.filter(name='老李').first()
    # tea_obj.person.add(per_obj)



    per_obj= Person.objects.filter(name='小红').first()
    per_obj1= Person.objects.filter(name='小黄').first()
    tea_obj = Teacher.objects.filter(name='老李').first()
    tea_obj.person.add(per_obj,per_obj1)



    # 反向
    # per_obj = Person.objects.filter(name='小美').first()
    # tea_obj = Teacher.objects.filter(name='吴老师').first()
    # per_obj.teacher_set.add(tea_obj)
    per_obj = Person.objects.filter(name='小美').first()
    tea_obj1 = Teacher.objects.filter(name='老李').first()
    tea_obj = Teacher.objects.filter(name='老赵').first()
    per_obj.teacher_set.add(tea_obj,tea_obj1)

    return HttpResponse('多对多关系增加')
def getduo(request):
    # 查询
    # 正向 查吴老师教的学生
    # tea_obj = Teacher.objects.filter(name='吴老师').first()
    # per_obj = tea_obj.person.all().values('name')
    # print(per_obj)

    # 反向  查小美有哪几个老师
    per_obj = Person.objects.filter(name='小美').first()
    tea_obj = per_obj.teacher_set.all().values('name')
    print(tea_obj)

    return HttpResponse('多对多关系查询')

def updateduo(request):
    # 修改 set
    # 在设置关系的时候会将之前的关系全部删除  *****
    # 正向
    # tea_obj = Teacher.objects.filter(name='老赵').first()
    # per_obj1 = Person.objects.filter(name='小美').first()
    # per_obj2 = Person.objects.filter(name='小红').first()
    # per_obj3 = Person.objects.filter(name='小黄').first()
    # tea_obj.person.set([per_obj1,per_obj2,per_obj3])
    # 反向  会删除per_obj之数据库中所有的关系数据并从新创建关系
    tea_obj = Teacher.objects.filter(name='老李').first()
    per_obj = Person.objects.filter(name='小红').first()
    per_obj.teacher_set.set([tea_obj])

    return HttpResponse('多对多关系修改')

def deleteduo(request):
    # remove
    # 删除某条数据数据与某条数据的关系
    # 删除teacher中id = 1 与 person中id = 1的关系
    # 正向
    # tea_obj = Teacher.objects.get(id=1)
    # per_obj = Person.objects.get(id=1)
    # tea_obj.person.remove(per_obj)
    # 反向
    # tea_obj = Teacher.objects.get(id=1)
    # per_obj = Person.objects.get(id=2)
    # per_obj.teacher_set.remove(tea_obj)

    # clear
    # 消除某个数据的所有关系
    # 删除teacher中id=3的数据
    # tea_obj = Teacher.objects.get(id=3)
    # tea_obj.person.clear()

    # 反向
    # 删除person中id=3的数据
    # per_obj = Person.objects.get(id=3)
    # per_obj.teacher_set.clear()


    # delete
    # 删除数据并去除关系
    # Teacher.objects.filter(id=1).delete()
    Person.objects.filter(id=4).delete()




    return HttpResponse('多对多关系删除')
from django.db.models import Max,Min,Avg,Count,F,Q
def juhe(request):
    ## 聚合查询
    # 返回的是字典 key 是默认生成的  查询的字段__用的方法
    # data = Person.objects.all().aggregate(Min('age'),Max('age'))
    # print(data)     # {'age__max': 22, 'age__min': 15}
    # 自己设置字典key值
    # data = Person.objects.all().aggregate(min_age=Min('age'),max_age=Max('age'))
    # print(data)     # {'max_age': 22, 'min_age': 15}
    # F  F对象
    # 能比较同一张 表中的不同字段
    ## 查询book表中num大于money的数据
    # book_obj = Book.objects.filter(num__gt=F('money')).values('name')
    # print(book_obj)
    # 查询book表中money大于等于num* 2的数据
    # book_obj = Book.objects.filter(money__gte=F('num') * 2).values('name')
    # print(book_obj)

    # Q  Q对象
    # 实现 and or not
    # 查询 num大于100 并且 money 大于100的数据
    res = Book.objects.filter(Q(num__gt=100) & Q(money__gt=100)).values('name')
    print(res)    #<QuerySet [{'name': 'python web'}]>
    # 查询 num大于100 或 money 大于100的数据
    res = Book.objects.filter(Q(num__gt=100) | Q(money__gt=100)).values('name')
    print(res)#<QuerySet [{'name': 'python web'}, {'name': 'python爬虫'}, {'name': '数据分析'}]>
    # ~  不等于
    res = Book.objects.filter(~Q(num__gt=100)).values('name')
    print(res)
    return HttpResponse('聚合查询')




