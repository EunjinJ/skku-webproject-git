from django.urls import path

from . import views # 현재 경로에 있는 views.py를 가져옴

from django.contrib.auth import views as auth_views # 로그인 및 로그아웃 할 때 사용

from .views import CustomLoginView # 로그인창 내가 커스텀


app_name = 'user'

urlpatterns = [
    path('', views.index, name='index'),
    
    # path('login/', auth_views.LoginView.as_view(template_name='user/login.html'), name='login'),

    # path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    # path('signup/', views.signup, name='user_signup'),

    # path('signup/complete/', views.signup_complete, name='user_signup_complete'),

    # ~~~ 장고 제공 회원가입 및 로그인 ~~~
    path('signup/', views.signup, name='signup'),

    #빈칸으로 두면 장고 제공 로그인창 뜨고, template_name 넣으면 내가 넣은 로그인창 뜨나봄
    # path('login/', auth_views.LoginView.as_view(), name='login'),
    path('login/', CustomLoginView.as_view(),  name='login'),

    path('logout/', auth_views.LogoutView.as_view(), name='logout'),


]
