from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

# Create your views here.

#定义视图函数
def index(request):
    # return HttpResponse('ok')
    context = {'title':'图书管理系统首页'}
    return render(request,'index.html',context)
#定义留言板函数
def msgproc(request):
    datalist = []
    if request.method == 'POST':
        userA = request.POST.get('userA',None)
        userB = request.POST.get('userB',None)
        msg = request.POST.get('msg',None)
        time = datetime.now()
        with open('msgdata.txt','a+')as f:
            f.write("{}--{}--{}--{}--\n".format(userB,userA,msg,time.strftime("%Y-%m-%d %H:%M:%s")))
    if request.method == 'GET':
        userC = request.GET.get('userC',None)
        if userC != None:
            with open("msgdata.txt","r")as f:
                cnf = 0
                for line in f:
                    linedata = line.split('--')
                    if linedata[0] == userC:
                        cnf = cnf+1
                        d = {'userA':linedata[1],'msg':linedata[2],'time':linedata[3]}
                        datalist.append(d)
                    if cnf>=10:
                        break
    return render(request,'MsgSingleWeb.html',{'data':datalist})


# 20200817练习
from django.http import HttpResponse

def index01(request):
    return HttpResponse("OK")


def getpath(request,a):
    # keyword01=request.GET.get(a)
    # keyword02=request.GET.get('kw02')
    print(a)
    return HttpResponse(a)

def getkeyword(request):
    kw1=request.GET.get('keyword1')
    kw2=request.GET.get('keyword2')
    print(kw1,kw2)
    kw=kw1+kw2
    return HttpResponse(kw)

def getkeywords(request):
    kw1=request.GET.getlist('keyword1')
    kw2=request.GET.get('keyword2')
    print(kw1,kw2)
    # kw=kw1+kw2
    # 此处为啥只能返回一个字符串参数？能不能同时返回多个字符串参数？
    return HttpResponse(kw2)

def login_json(request):
    import json
    body=request.body
    body_str=body.decode()
    json.loads(body_str)
    print(body_str)
    body_json=json.dumps(body_str)
    print(body_json)
#    网页返回值为："{\"username\":\"xiaoxiao\",\n\"user_id\":123}"是正常的吗？
    return HttpResponse(body_json)

def jsonresponse(request):
    import json
    userinfo={'user':'xiaoxiao','user_id':'123'}
    user=json.dumps(userinfo)
    return HttpResponse(user)




from django.http import JsonResponse
def jsonresponse01(request):
    userinfo = {'user': 'xiaoxiao', 'user_id': '123'}
    return JsonResponse(userinfo)

# 重定向redirect
from django.shortcuts import redirect
def to_index(request):
    return redirect('http://baidu.com')
    # return redirect(index)




