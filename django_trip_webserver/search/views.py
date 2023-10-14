from django.shortcuts import render

# 여행지 검색
def search_trip(request):
    return render(request, 'search/search_trip.html', {})

# 여행지 댓글 검색
def search_trip_comment(request):
    return render(request, 'search/search_trip_comment.html', {})

# 여행지 리뷰 검색
def search_review(request):
    return render(request, 'search/search_review.html', {})

# 여행지 리뷰 댓글 검색
def search_review_comment(request):
    return render(request, 'search/search_review_comment.html', {})