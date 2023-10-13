from django.shortcuts import render

# 로그인
def login(request):
    return render(request, 'user/login.html', {})