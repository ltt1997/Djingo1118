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

class Type(models.Model):
    name = models.CharField(max_length=32)
    description = models.TextField()


class Article(models.Model):
    title = models.CharField(max_length=32)
    date = models.DateField()
    content = models.TextField()
    description = models.TextField()


class Author(models.Model):
    name = models.CharField(max_length=32)
    gender = models.CharField(max_length=32)
    age = models.IntegerField()
    email = models.EmailField()


class Publish(models.Model):
    name = models.CharField(max_length=32,verbose_name='出版社名字')
    address = models.CharField(max_length=32,verbose_name='出版社地址')
    class Meta:
        db_table = 'publish'   ## 修改数据库中显示的表名


class Book(models.Model):
    name = models.CharField(max_length=32,verbose_name='书名')
    money = models.IntegerField(verbose_name='价钱')
    pub = models.ForeignKey(to=Publish,to_field='id',on_delete=True)
    class Meta:
        db_table = 'book'




