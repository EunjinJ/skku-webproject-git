from django.shortcuts import render
from board.models import Trip

import json

from django.http import Http404
from .forms import CommentForm
from .forms import BoardForm
from django.urls import reverse
from django.shortcuts import redirect
from django.http import HttpResponse
from django.shortcuts import render

from .models import Trip, TripComment

def trip_list(request):
    trip_data = Trip.objects.all()
    return render(request, "board/trip_list.html",{'trip_data': trip_data})


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
    trip_data = Trip.objects.all()
    return render(request, 'trip_detail.html', {'trip_comment': trip_comment, 'trip_data': trip_data})


#여행지 새 글
def trip_write(request):
    return render(request, 'board/trip_write.html', {})