from django.shortcuts import render

# 상세검색 (여행지검색+여행지댓글검색+여행지리뷰검색+여행지리뷰댓글검색)
def search(request):
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