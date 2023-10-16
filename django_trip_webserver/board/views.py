from django.shortcuts import render
from board.models import Trip, Review

# 여행지 리스트
def trip_list(request):
    return render(request, 'board/trip_list.html', {})

# 여행지 상세
def trip_detail(request, trip_id): # trip_id는 urls.py에서 받아옴???
    return render(request, 'board/trip_detail.html', {})

# 리뷰 리스트
def review_list(request, trip_id):
    trip = Trip.objects.get(pk=trip_id)
    return render(
        request,
        'board/review_list.html',
        {
            'trip': trip
        }
    )

# 리뷰 상세
def review_detail(request, trip_id, review_id):
    review = Review.objects.get(pk=review_id)
    return render(
        request,
        'board/review_detail.html',
        {
            'review': review
        }
    )

# 리뷰 작성
def review_write(request, trip_id):
    return render(
        request,
        'board/review_write.html',
        {

        }
    )
