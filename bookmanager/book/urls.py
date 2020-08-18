from django.urls import path
from book.views import index,msgproc,index01,getpath,getkeywords,getkeyword,login_json,jsonresponse,jsonresponse01,to_index
from book import views
from django.urls import converters



urlpatterns = [
    path('index/',index),
    path('msg/',msgproc),
    path('index01/',index01),
    path('getpath/<a>',getpath),
    path('getkeyword/',getkeyword),
    path('getkeywords/',getkeywords),
    path('login_json/',login_json),
    path('jsonresponse/',jsonresponse),
    path('jsonresponse01/',jsonresponse01),
    path('to_index/',to_index),
    path('p/<int:tieba_id>/',views.baidu_tieba),
    path('<mobile:tel>/<q>/',views.tele)

]