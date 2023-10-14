from django.urls import path

from . import views # 현재 경로에 있는 views.py를 가져옴

urlpatterns = [
    path('/login', views.login, name='user_login'),
]

urlpatterns = [
    path('/signup', views.signup, name='user_signup'),
]