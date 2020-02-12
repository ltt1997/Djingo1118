# 编写自定义过滤器
# 1 导包
from django import template
# 2 实例化对象
register = template.Library()
## 前端调用
## 编写过滤器方法
@register.filter()
def myadd(num):
    return num+num

@register.filter()
def addtwo(num1,num2):
    return num1 + num2






