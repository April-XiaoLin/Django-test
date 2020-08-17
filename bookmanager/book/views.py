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
