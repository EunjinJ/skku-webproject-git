from django.urls import path

from . import views # 현재 경로에 있는 views.py를 가져옴

from django.contrib.auth import views as auth_views # 로그인 및 로그아웃 할 때 사용

app_name = 'user'

urlpatterns = [
    path('', views.index, name='index'),
    
    # path('login/', views.login, name='user_login'),
    path('login/', auth_views.LoginView.as_view(template_name='user/login.html'), name='login'),

    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    path('signup/', views.signup, name='user_signup'),

    path('signup/complete/', views.signup_complete, name='user_signup_complete'),
]