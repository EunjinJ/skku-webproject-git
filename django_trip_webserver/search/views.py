from django.shortcuts import render

# 상세검색 (여행지검색+여행지댓글검색+여행지리뷰검색+여행지리뷰댓글검색)
def search(request):

    # 여행지 검색 쿼리문
    if request.method == 'POST':
        data = request.POST
        area_l = data.get('area_l')
        area_m = data.get('area_m')
        trip_category = data.get('trip_category')
        star = data.get('star')
        review_num = data.get('review_num')
        search_category = data.get('search_category') # 1 = 제목 / 2 = 제목+내용
        pass


'''
데이터베이스 Trip table에서
area_l = 1 이고
area_m = 1 이고
trip_category = 1 이고
star = 4 이상이고
인 게시글의 title과 content를 모두 포함하는 데이터를 찾는 쿼리문을 짜줘

SELECT title, content
FROM Trip
WHERE area_l = 1
  AND area_m = 1
  AND trip_category = 1
  AND star >= 4
  AND (title LIKE '%검색할문자열%' OR content LIKE '%검색할문자열%');
  이 쿼리에서 %검색할문자열% 부분을 실제로 찾고자 하는 문자열로 대체해야 합니다. 이 쿼리는 title 또는 content 중 하나라도 지정한 문자열을 포함하는 게시물을 반환합니다.
'''
    

'''
위 쿼리문 결과의 개수가 
'''
    
    
     
    # 여행지댓글 검색 쿼리문

    # 여행지리뷰 검색 쿼리문

    # 여행지리뷰댓글 검색 쿼리문

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