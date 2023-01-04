from django.urls import re_path as url  # re_path는 path 뒤에 추가로 붙는 경로를 뜻한다.

from basic.dlearn.aitrader import views

urlpatterns = [
    url(r'aitrader', views.aitrader)
]