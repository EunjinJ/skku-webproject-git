from django.shortcuts import render
from board.models import Trip, Review

import json

from django.http import Http404
from .forms import CommentForm
# from .forms import BoardForm
from django.urls import reverse
from django.shortcuts import redirect
from django.http import HttpResponse
from django.shortcuts import render

from .models import Trip, TripComment
from main.models import TripCategory, AreaL, AreaM
from user.models import User

from django.core.paginator import Paginator
from django.views.generic import ListView

from django.utils import timezone

# def index(request):
#     trip_page =  


class ContactListView(ListView):
    paginate_by = 10
    model = Trip

def trip_list(request):
    trip_data = Trip.objects.filter(is_deleted=0)
    trip_comment = TripComment.objects.all()

    posts_per_page = 10

    paginator = Paginator(trip_data, posts_per_page)

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        'trip_data': trip_data,
        'trip_comment': trip_comment,
        'paginator' : paginator,
        'page_number': page_number,
        'page_obj' : page_obj,
    }

    return render(request, "board/trip_list.html", context)


def trip_detail(request, trip_id):
    trip_data = Trip.objects.get(pk=trip_id)
    user_data = User.objects.all()
    trip_category = TripCategory.objects.all()

    if request.method == 'POST':
        data = request.POST
        comment_content = data.get('content')
        comment_star = data.get('rating')
        TripComment.objects.create(
            # user_id = request.headers.get('HTTP_USER_ID'),
            trip_id = Trip.objects.get(id=trip_id),
            user_id = User.objects.get(id = 1), # 로그인 기능 구현 후 바꾸기
            trip_comment_content = comment_content,
            trip_comment_star = comment_star,
            trip_commnet_time = timezone.localtime(),
            is_deleted = False
        )
        return redirect(reverse(f'board:trip_detail', args=[trip_id]))

    comment_list = Trip.get_active_list().prefetch_related('TripComment_set').all()
    trip_comment = TripComment.objects.all()

    context = {
        'user_data' : user_data,
        'trip_data': trip_data,
        'trip_category' : trip_category,
        'comment_list': comment_list,
        'trip_comment': trip_comment,
    }

    return render(request, 'board/trip_detail.html', context)


#여행지 새 글

import uuid
def trip_write(request):
    # form = BoardForm()
    # 장고폼 이용
    # if request.method == 'POST':
    #     form = BoardForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         return redirect(reverse('trip_list'))
    
    # 일반 폼 이용
    if request.method == 'POST':
        data = request.POST

        area_l = data.get('area_l')
        area_m = data.get('area_m')
        trip_category_name = data.get('trip_category_name')
        trip_description = data.get('trip_description')
        trip_category_detail = data.get('trip_category_detail')
        trip_address = data.get('trip_address')
        trip_time = data.get('trip_time')
        trip_phone = data.get('trip_phone')
        trip_homepage = data.get('trip_homepage')

        # random_id = uuid.uuid4()

        trip = Trip(
            # id = random_id,
            trip_name = trip_description,
            trip_category_detail = trip_category_detail,
            trip_address = trip_address,
            trip_time = trip_time,
            trip_phone = trip_phone,
            trip_homepage = trip_homepage
        )

# from main.models import TripCategory, AreaL, AreaM

        tripcategory = TripCategory(
            trip_category_name = trip_category_name,
        )

        areal = AreaL(
            area_l_name = area_l,
        )

        aream = AreaM(
            area_m_name = area_m,
        )
        
        trip.save()
        tripcategory.save()
        areal.save()
        aream.save()

        return redirect(reverse('board:trip_list'))
    return render(request, "board/trip_write.html")

# if request.method == 'POST':
    #     form = BoardForm(request.POST)

    #     if form.is_valid():
    #         board.title = form.cleaned_data['title']
    #         board.content = form.cleaned_data['content']
    #         board.author = form.cleaned_data['author']
    #         board.save()
    #         return redirect(reverse('board:detail', kwargs={
    #             'board_id': board_id
    #         }))
    # return render(request,
    #             "board/edit.html",
    #             {'form': form}
    #             )

def trip_edit(request, trip_id):
    trip = Trip.objects.get(id=trip_id)
    # tripctg = TripCategory.objects.get(id=category_id)
    # areal = AreaL.objects.get(id=l_id)
    # aream = AreaM.objects.get(id=m_id)

    if request.method == 'POST':
        data = request.POST

        area_l_name = data.get('area_l_name')
        area_m_name = data.get('area_m_name')
        trip_category_name = data.get('trip_category_name')
        
        trip_description = data.get('trip_description')
        trip_category_detail = data.get('trip_category_detail')
        trip_address = data.get('trip_address')
        trip_time = data.get('trip_time')
        trip_homepage = data.get('trip_homepage')

        # areal.area_l_name = area_l_name
        # aream.area_m_name = area_m_name
        # tripctg.trip_category_name = trip_category_name
        trip.trip_description = trip_description
        trip.trip_category_detail = trip_category_detail
        trip.trip_address = trip_address
        trip.trip_time = trip_time
        trip.trip_homepage = trip_homepage

        trip.save()
        # tripctg.save()
        # areal.save()
        # aream.save()

        return redirect(reverse('board:detail', kwargs={'board_id': trip_id}))

    return render(request, "board/edit.html", {
            'trip': trip,
        })




def trip_delete(request, trip_id):
    trip = Trip.objects.get(id=trip_id)
    trip.is_deleted = True
    trip.save()
    return redirect(reverse('board:trip_list'))


#comment 리스트
def comment_list(request):
    qs = TripComment.objects.all()

    html = ""
    for comment in qs:
        html += f"<li>{comment.user_id} | \
            {comment.trip_comment_content} | {comment.trip_comment_star} </li>"
    html = f"<ul>{html}</ul>"

    return HttpResponse(html)



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