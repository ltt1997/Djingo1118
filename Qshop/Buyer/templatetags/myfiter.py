from django import template
register = template.Library()


@register.filter()
def myadd(num1,num2):
    return num1 + num2

@register.filter()
def myfloat(num):
    return '%.2f'%num




