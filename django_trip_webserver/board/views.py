from django.shortcuts import render
from board.models import Trip, Review

import json

from django.http import Http404
from .forms import CommentForm
from .forms import BoardForm
from django.urls import reverse
from django.shortcuts import redirect
from django.http import HttpResponse
from django.shortcuts import render
from django.utils import timezone
from .models import Trip, TripComment, User

# def index(request):
#     trip_page =  

def trip_list(request):
    trip_data = Trip.objects.all()
    trip_comment = TripComment.objects.all()
    return render(request, "board/trip_list.html",{'trip_data': trip_data, 'trip_comment': trip_comment})


def trip_detail(request, board_id):
    board = Trip.objects.get(pk=board_id)

    board_history = request.session.get('board_history')
    if not board_history:
        request.session['board_history'] = []
    request.session['board_history'] += [board_id]

    if not (board and board.is_active):
        return Http404("요청하신 페이지가 없습니다.")

    

    form = CommentForm()

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            TripComment(
                content=data['content'],
                board_id=board_id
            ).save()
            return redirect(reverse('board:trip_detail',
                                    kwargs={'board_id': board_id}))

    resp = render(request,
                "board/trip_detail.html",
                {'board': board, 'form': form})

    # comment_list = Trip.get_active_list().prefetch_related('TripComment_set').all()
    trip_comment = TripComment.objects.all()
    return render(request, 'trip_detail.html', {'trip_comment': trip_comment})

# # 여행지 리스트
# def trip_list(request):
#     return render(request, 'board/trip_list.html', {})

# # 여행지 상세
# def trip_detail(request, trip_id):
#     return render(request, 'board/trip_detail.html', {})

#여행지 새 글
def trip_write(request):
    form = BoardForm()
    if request.method == 'POST':
        form = BoardForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('board:trip_list'))

    return render(request, "board/trip_write.html", {'form': form})


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
    if request.method == 'POST':
        data = request.POST
        title = data.get('title')
        image1 = data.get('image1')
        image2 = data.get('image2')
        image3 = data.get('image3')
        image4 = data.get('image4')
        image5 = data.get('image5')
        content = data.get('content')
        Review.objects.create(
            # user_id = request.headers.get('HTTP_USER_ID'),
            user_id = User.objects.get(id = 1), # 로그인 기능 구현 후 바꾸기
            trip_id = Trip.objects.get(id = trip_id),
            review_title = title,
            review_content = content,
            review_time = timezone.localtime(),
            review_image1 = image1,
            review_image2 = image2,
            review_image3 = image3,
            review_image4 = image4,
            review_image5 = image5,
            is_deleted = False
        )
        return redirect(reverse('board:review_list', args = [trip_id]))
    return render(
        request,
        'board/review_write.html',
        {

        }
    )
