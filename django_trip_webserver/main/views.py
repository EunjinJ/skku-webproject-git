from django.shortcuts import render

# 메인화면(홈)
def main(request):
    return render(request, 'main/main.html', {})