from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=32)
    age = models.IntegerField()
    phone = models.CharField(max_length=15)
    email = models.EmailField(default='111111@qq.com')
    class Meta:
        db_table = "user"
        verbose_name_plural = 'user'
        # ordering = ["age"]

# class Type(models.Model):
#     name = models.CharField(max_length=32)
#     description = models.TextField()
#
#
# class Article(models.Model):
#     title = models.CharField(max_length=32)
#     date = models.DateField()
#     content = models.TextField()
#     description = models.TextField()


# class Author(models.Model):
#     name = models.CharField(max_length=32)
#     gender = models.CharField(max_length=32)
#     age = models.IntegerField()
#     email = models.EmailField()

class Publish(models.Model):
    name = models.CharField(max_length=32,verbose_name='出版社名字')
    address = models.CharField(max_length=32,verbose_name='出版社地址')
    class Meta:
        db_table = 'publish'   ## 修改数据库中显示的表名


class Book(models.Model):
    name = models.CharField(max_length=32,verbose_name='书名')
    money = models.IntegerField(verbose_name='价钱')
    num = models.IntegerField(default=1,verbose_name='编号')
    pub = models.ForeignKey(to=Publish,to_field='id',on_delete=models.CASCADE)
    class Meta:
        db_table = 'book'


class Person(models.Model):
    name = models.CharField(max_length=32,verbose_name="学生姓名")
    age = models.IntegerField(verbose_name="学生年龄")
    class Meta:
        db_table = 'person'


class Teacher(models.Model):
    name = models.CharField(max_length=32,verbose_name="教师姓名")
    gender = models.IntegerField(verbose_name='教师性别')
    age = models.IntegerField(verbose_name='教师年龄')
    person = models.ManyToManyField(to=Person)
    class Meta:
        db_table = 'teacher'


class Type(models.Model):
    name = models.CharField(max_length=32,verbose_name='类型名字')
    description = models.TextField(verbose_name='描述')
    class Meta:
        db_table = 'type'


class Author(models.Model):
    name = models.CharField(max_length=32,verbose_name='作者姓名')
    gender = models.CharField(max_length=32,verbose_name='性别')
    age = models.IntegerField(verbose_name='作者年龄')
    email = models.EmailField(verbose_name='作者邮箱')
    class Meta:
        db_table = 'author'


class Article(models.Model):
    title = models.CharField(max_length=32,verbose_name='文章描述')
    data = models.DateField(verbose_name='时间日期')
    content = models.TextField(verbose_name='文章内容')
    description = models.TextField(verbose_name='文章描述')
    author = models.ForeignKey(to=Author,to_field='id',on_delete=models.CASCADE)
    type = models.ManyToManyField(to=Type)
    class Meta:
        db_table = 'article'













