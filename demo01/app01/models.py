from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=32)
    age = models.IntegerField()
    phone = models.CharField(max_length=15)
    email = models.EmailField(default='111111@qq.com')

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






