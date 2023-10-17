from django.shortcuts import render
from board.models import Trip, Review, ReviewComment

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
from django.core.paginator import Paginator

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

    page = request.GET.get('page', '1')  # 페이지
    review_list = Review.objects.order_by('-review_time')
    paginator = Paginator(review_list, 20)  # 페이지당 20개씩 보여주기
    page_obj = paginator.get_page(page)

    return render(
        request,
        'board/review_list.html',
        {
            'trip': trip,
            'review_list': page_obj
        }
    )

# 리뷰 상세
def review_detail(request, trip_id, review_id):
    review = Review.objects.get(pk=review_id)

    page = request.GET.get('page', '1')  # 페이지
    comment_list = ReviewComment.objects\
            .filter(review_id = Review.objects.get(id = review_id))\
            .order_by('-review_comment_time')
    paginator = Paginator(comment_list, 15)  # 페이지당 15개씩 보여주기
    page_obj = paginator.get_page(page)

    if request.method == 'POST':
        data = request.POST
        comment_content = data.get('content')
        ReviewComment.objects.create(
            # user_id = request.headers.get('HTTP_USER_ID'),
            user_id = User.objects.get(id = 1), # 로그인 기능 구현 후 바꾸기
            review_id = Review.objects.get(id = review_id),
            review_comment_content = comment_content,
            review_comment_time = timezone.localtime(),
            is_deleted = False
        )
        return redirect(reverse('board:review_detail', args=[trip_id, review_id]))
    return render(
        request,
        'board/review_detail.html',
        {
            'review': review,
            'comment_list': page_obj
        }
    )

# 리뷰 작성
def review_write(request, trip_id):
    if request.method == 'POST':
        data = request.POST
        title = data.get('title')
        content = data.get('content')
        images = [''] * 6
        for i in range(1, 6):
            if f'image{i}' in request.FILES.keys():
                images[i] = request.FILES[f'image{i}']

        Review.objects.create(
            # user_id = request.headers.get('HTTP_USER_ID'),
            user_id = User.objects.get(id = 1), # 로그인 기능 구현 후 바꾸기
            trip_id = Trip.objects.get(id = trip_id),
            review_title = title,
            review_content = content,
            review_time = timezone.localtime(),
            review_image1 = images[1],
            review_image2 = images[2],
            review_image3 = images[3],
            review_image4 = images[4],
            review_image5 = images[5],
            is_deleted = False
        )
        return redirect(reverse('board:review_list', args=[trip_id]))
    return render(
        request,
        'board/review_write.html',
        {
            
        }
    )
