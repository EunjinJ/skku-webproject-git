from django.shortcuts import render, redirect # html 불러오기

from django.urls import reverse # DB 저장 시 이용

from user.models import User
from main.models import TripCategory

# 로그인 되어있는 상태일 때 아이디 정보 가져오는 법
# user_id = request.headers.get('HTTP_USER_ID')

# 로그인
def login(request):
    return render(request, 'user/login.html', {})

# 회원가입
def signup(request):

    # 입력정보 --> DB 저장
    if request.method == 'POST':
        data = request.POST
        user_id = data.get('user_id')
        user_password = data.get('user_password')
        user_type = data.get('user_type')
        trip_category_1_id = data.get('trip_category_1_id')
        trip_category_2_id = data.get('trip_category_2_id')
        trip_category_3_id = data.get('trip_category_3_id')
        # trip_category_n_id는 foreign키이므로 DB TripCategory에서 알맞은 인스턴스를 가져옴
        trip_category_1 = TripCategory.objects.get(id=trip_category_1_id)
        trip_category_2 = TripCategory.objects.get(id=trip_category_2_id)
        trip_category_3 = TripCategory.objects.get(id=trip_category_3_id)
        # DB user에 저장
        user = User(
            id=user_id,
            user_password=user_password,
            user_type=user_type,
            trip_category_1_id=trip_category_1,
            trip_category_2_id=trip_category_2,
            trip_category_3_id=trip_category_3,
            is_deleted=0,
        )
        user.save()
        
        return redirect(reverse('user_signup_complete'))

    return render(request, 'user/signup.html', {})

# 회원가입 성공
def signup_complete(request):
    return render(request, 'user/signup_complete.html', {})

# 회원정보
def index(request):
    print(request.session)
    print('session 확인')
    for k, v in request.session.items():
        print(k, v)
    print("Cookie 확인")
    history = request.COOKIES.get('board_history')
    print(history)
    return render(request, 'user/profile.html')




# # 장고 내장된 로그인 및 회원가입 이용

# from django.shortcuts import render, redirect
# from django.contrib.auth import login, authenticate
# from django.contrib.auth.forms import UserCreationForm

# def signup(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             login(request, user)
#             return redirect('index')
#     else:
#         form = UserCreationForm()
#     return render(request, 'user/signup.html', {'form': form})





# 로그인 뷰창 커스텀
from django.contrib.auth.views import LoginView

class CustomLoginView(LoginView):
    template_name = 'user/login.html'  # 로그인 템플릿 경로 설정
