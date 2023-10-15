from django.shortcuts import render

# 메인화면(홈)
def main(request):
    return render(request, 'main/main.html', {})

# 메인화면(홈-서울)
def main_seoul(request):
    return render(request, 'main/main_seoul.html', {})