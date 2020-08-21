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
]