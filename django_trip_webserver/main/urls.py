from django.urls import path

from . import views # 현재 경로에 있는 views.py를 가져옴

urlpatterns = [
    path('', views.main, name='main'),
    path('main_seoul', views.main_seoul, name='seoul'),
]