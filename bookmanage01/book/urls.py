from django.urls import path
from book.views import index,login,get_cookie_01,set_session_01,get_session_01
from book import views
urlpatterns = [
    path('index/', index),
    path('login/', login),
    path('get_cookie_01/',get_cookie_01),
    path('set_session/',set_session_01),
    path('get_session/',get_session_01),
    path('register_method/',views.register_method),
    path('class+method/',views.RegisterView.as_view()),
    # 中间件不需要设置路径，在SETTING注册，注册后不需有调用语句即可按照信息处理流程自行执行
    # path('TestMiddleware1/',views.TestMiddleware1.as_view()),
]