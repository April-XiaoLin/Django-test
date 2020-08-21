from django.shortcuts import render
from django.http import response
from django.views.generic import View

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




