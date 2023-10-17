from django.shortcuts import render

from board.models import Trip, TripComment, Review, ReviewComment

from django.db.models import Q # 단어 포함 쿼리문 날릴 때 사용
from django.db.models import Count # 데이터 개수 셀 때 사용
from django.db.models import Avg # 평균낼 때 사용

from django.urls import reverse
from django.shortcuts import redirect 


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
            if search_keyword:
                if search_category == '1': # 제목
                    query = Q(trip_name__icontains=search_keyword)
                elif search_category == '2': # 제목+내용
                    query = Q(trip_name__icontains=search_keyword) | Q(trip_category_detail__icontains=search_keyword)
                keyword_Q = category_Q.filter(query)
            else:
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
                star_Q = review_Q


            print('아아아악', star_Q)
            return render(request, 'search/search.html', {'search_results': star_Q})

    
       
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