from django.shortcuts import render
from board.models import Trip

# 여행지 리스트
def trip_list(request):
    return render(request, 'board/trip_list.html', {})

# 여행지 상세
def trip_detail(request, trip_id): # trip_id는 urls.py에서 받아옴???
    return render(request, 'board/trip_detail.html', {})
