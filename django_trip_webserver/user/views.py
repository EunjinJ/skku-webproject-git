from django.shortcuts import render # html 불러오기

from django.urls import reverse # DB 저장 시 이용
from django.shortcuts import redirect 

from user.models import User
from main.models import TripCategory

# # 로그인
# def login(request):
#     return render(request, 'user/login.html', {})

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