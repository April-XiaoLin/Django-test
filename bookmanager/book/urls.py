from django.urls import path
from book.views import index,msgproc

urlpatterns = [
    path('index/',index),
    path('msg/',msgproc)
]