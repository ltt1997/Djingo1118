from django.shortcuts import render_to_response
from django.http import HttpResponse
# def index(request):
#     name = 'lisi'
#     age = 19
#     return render_to_response('index.html',locals())

def index(request):
    return render_to_response('index.html')

def base(request):
    return render_to_response('base.html')

def about(request):
    return render_to_response('about.html')

def listpic(request):
    return render_to_response('listpic.html')

def newslistpic(request):
    return render_to_response('newslistpic.html')






