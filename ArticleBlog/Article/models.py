from django.db import models

# Create your models here.


class Type(models.Model):
    name = models.CharField(max_length=32,verbose_name='类型名字')
    description = models.TextField(verbose_name='描述')
    def __str__(self):
        return self.name
    class Meta:
        db_table = 'type'

GENDER_STATUS = (
    (0,'女'),
    (1,'男'),
)


class Author(models.Model):
    name = models.CharField(max_length=32,verbose_name='作者姓名')
    gender = models.IntegerField(choices=GENDER_STATUS,verbose_name='性别')
    age = models.IntegerField(verbose_name='作者年龄')
    email = models.EmailField(verbose_name='作者邮箱')

    def __str__(self):
        return self.name
    class Meta:
        db_table = 'author'


class Article(models.Model):
    title = models.CharField(max_length=32,verbose_name='标题')
    data = models.DateField(auto_now=True,verbose_name='时间日期')
    content = models.TextField(verbose_name='文章内容')
    description = models.TextField(verbose_name='文章描述')
    image = models.ImageField(upload_to='images',verbose_name='图片')
    author = models.ForeignKey(to=Author,to_field='id',on_delete=models.CASCADE)
    type = models.ManyToManyField(to=Type)
    def __str__(self):
        return self.title
    class Meta:
        db_table = 'article'






