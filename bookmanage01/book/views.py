from django.shortcuts import render
from django.http import response
from django.views.generic import View
from django.template import Template, Context

# 导入中间件父类
from django.utils.deprecation import MiddlewareMixin

# Create your views here.
from django.http import HttpResponse

def index(request):

    return HttpResponse("OK")

def login(request):
    response=HttpResponse('ok')
    username = request.GET.get('username')
    response.set_cookie(key='username',value=username,max_age=60*60*24)
    return response

def get_cookie_01(request):
    cookie_01= request.COOKIES.get('username')
    print(cookie_01)
    return HttpResponse(cookie_01)

def set_session_01(request):
    request.session['user_id']='123456'
    return HttpResponse('set_session')

def get_session_01(request):
    aaa=request.session['user_id']
    return HttpResponse(aaa)

def register_method(request):
    if request.method == 'GET':
        return HttpResponse('get')
    if request.method == 'POST':
        return HttpResponse('post')

class RegisterView(View):
    def get(self,request):
        return HttpResponse('get')
    def post(self,request):
        return HttpResponse('post')

class TestMiddleware1(MiddlewareMixin):
    def process_request(self,request):
        # 请求被处理之前执行
        print('process_request1 被调用')
    #     处理视图之前被执行emplat
    def process_view(self,request,view_func,view_args,view_kwargs):
        print('process_view1被调用')
    def process_response(self,request,response):
#在响应反馈到浏览器之前执行
        print('process_response1被调用')
        return response


def vue_template(request):
    # template='vue.html'
    # context = Context({"name": "实验pResponse(template.render(c平台"})
    return render(request,'vue.html',{"name": "实验pResponse(template.render(c平台"})

    # return HttpResponse(template.render(context))



