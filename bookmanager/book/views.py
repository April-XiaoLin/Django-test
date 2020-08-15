from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

#定义视图函数
def index(request):
    # return HttpResponse('ok')
    context = {'title':'图书管理系统首页'}
    return render(request,'index.html',context)