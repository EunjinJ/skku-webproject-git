from django.shortcuts import render

from board.models import Trip, TripComment, Review, ReviewComment

from django.db.models import Q


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
            area_category_Q = Trip.objects.filter(
                area_m_id = area_m,
                trip_category_id = trip_category)
            query = Q(trip_name__icontains=search_keyword) | Q(trip_category_detail__icontains=search_keyword)

            keyword_Q = area_category_Q.filter(query)
            print(keyword_Q)
                # 여행지에 서치키워드가 포함된 경우 |또는 세부유형에 서치키워드가 포함된 경우


            # 해당 관광지의 별점 평점이 star점 이상인 관광지
            
            # 해당 관광지의 리뷰 개수가 review_num개 이상인 관광지
            return keyword_Q


        
        # 데이터베이스 Trip table에서
        # area_l = 1 이고
        # area_m = 1 이고
        # trip_category = 1 이고
        # star = 4 이상이고
        # 인 게시글의 title과 content를 모두 포함하는 데이터를 찾는 쿼리문을 짜줘

        # SELECT title, content
        # FROM Trip
        # WHERE area_l = area_l
        #   AND area_m = area_m
        #   AND trip_category = trip_category
        #   AND star >= star
        #   AND (title LIKE 'search_keyword' OR content LIKE 'search_keyword');
        #   이 쿼리에서 %검색할문자열% 부분을 실제로 찾고자 하는 문자열로 대체해야 합니다. 이 쿼리는 title 또는 content 중 하나라도 지정한 문자열을 포함하는 게시물을 반환합니다.

        # 위 쿼리문 결과의 개수가 

    
       
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