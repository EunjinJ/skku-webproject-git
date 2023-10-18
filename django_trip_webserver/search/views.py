from django.shortcuts import render

from board.models import Trip, TripComment, Review, ReviewComment

from django.db.models import Q # 단어 포함 쿼리문 날릴 때 사용
from django.db.models import Count # 데이터 개수 셀 때 사용
from django.db.models import Avg # 평균낼 때 사용

from django.urls import reverse
from django.shortcuts import redirect 

from django import forms # 입력값 누락 시 경고 처리할 때 사용


# 상세검색 (여행지검색+여행지댓글검색+여행지리뷰검색+여행지리뷰댓글검색)
def search(request):
    print(request.POST)

    # 변수 한번에 받기 (각 폼마다 받는 input 차이는 None으로 나오고 에러 안나므로 ㄱㅊ음)
    if request.method == 'POST':
        data = request.POST

        area_l = data.get('area_l')
        area_m = data.get('area_m')
        trip_category = data.get('trip_category')
        star = data.get('star') # search_trip만 O
        review_num = data.get('review_num') # search_trip만 O
        start_date = data.get('start_date') # search_trip만 X
        end_date = data.get('end_date') # search_trip만 X
        search_category = data.get('search_category') # 1 = 제목 / 2 = 제목+내용
        search_keyword = data.get('search_keyword')
        

            
    
        # 여행지 검색 쿼리문
        if 'search_trip' in data:

            # 지역 l
            if area_l != '지역':
                area_m_ids = Trip.objects.filter(area_m_id=area_m).values_list('id', flat=True)
                # area_l에 해당하는 모든 area_m들의 id를 1차원(flat) 리스트
                area_l_Q = Trip.objects.filter(area_m_id__in=area_m_ids) # area_m_ids인 데이터
            else:
                area_l_Q = Trip.objects.all()
            
            # 지역 m
            if area_m != '세부지역':
                area_m_Q = area_l_Q.filter(area_m_id = area_m,)
            else:
                area_m_Q = area_l_Q

            # 관광카테고리
            if trip_category != '선택':
                category_Q = area_m_Q.filter(trip_category_id = trip_category,)
            else:
                category_Q = area_m_Q

            # 검색키워드
            popup = ''
            if search_keyword:
                # 제목
                if search_category == '1': 
                    query = Q(trip_name__icontains=search_keyword)
                    keyword_Q = category_Q.filter(query)
                # 제목+내용
                elif search_category == '2': 
                    query = Q(trip_name__icontains=search_keyword) | Q(trip_category_detail__icontains=search_keyword)
                    keyword_Q = category_Q.filter(query)
                # 검색카테고리를 안정했는데 검색키워드는 입력한경우
                else: 
                    popup='data-bs-toggle="modal" data-bs-target="#myModal"' # search/search.html의 버튼창을 모달로 바꿈
                    # return render(request, 'search/popup.html', {'error_title': '입력값 누락!', 'error_detail' : '제목 혹은 제목+선택을 입력하세요'})
                
            else: # 검색카테고리도 없고 검색 키워드도 없음
                keyword_Q = category_Q

            # 리뷰개수
            if review_num:
                review_count_Q = keyword_Q.annotate(review_count=Count('review_set')) # 리뷰 개수 세기 + review_count라는 컬럼에 일시적 저장
                review_Q = review_count_Q.filter(review_count__gte=5) # 개수 필터링 __gte는 이상이라는 뜻
            else:
                review_Q = keyword_Q

            # 별점
            if star:
                star_avg_Q = review_Q.annotate(avg_score=Avg('tripcomment_set__trip_comment_star'))
                # TripComment라는 DB테이블에 trip_comment_star라는 컬럼--> 의 평균 --> 을 새 컬럼에 일시저장
                star_Q = star_avg_Q.filter(avg_score__gte=star)
            else:
                # tripcomment가 들어와야 별점 넣는데 아예 tripcomment를 못넣었음
                # star_avg_Q = review_Q.annotate(avg_score=Avg('tripcomment_set__trip_comment_star'))
                # star_Q = star_avg_Q.filter(avg_score__gte=0)
                star_Q = review_Q

            return render(request, 'search/search.html', {'search_results': star_Q, 'popup':popup})

    
       
        # 여행지댓글 검색 쿼리문
        elif 'search_trip_comment' in request.POST:
            print(2)

        


        # 여행지리뷰 검색 쿼리문
        elif request.method == 'POST' and 'search_review' in request.POST:
            print(3)


        # 여행지리뷰댓글 검색 쿼리문
        elif request.method == 'POST' and 'search_review_comment' in request.POST:
            print(4)


    return render(request, 'search/search.html', {})

# # 여행지 검색
# def search_trip(request):
#     return render(request, 'search/search_trip.html', {})

# # 여행지 댓글 검색
# def search_trip_comment(request):
#     return render(request, 'search/search_trip_comment.html', {})

# # 여행지 리뷰 검색
# def search_review(request):
#     return render(request, 'search/search_review.html', {})

# # 여행지 리뷰 댓글 검색
# def search_review_comment(request):
#     return render(request, 'search/search_review_comment.html', {})