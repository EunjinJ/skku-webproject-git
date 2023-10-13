from django.urls import path

from . import views # 현재 경로에 있는 views.py를 가져옴

urlpatterns = [
    path('trip/', views.trip_list, name='trip_list'),
    path('trip/<int:board_id>', views.trip_detail, name='trip_detail'),
]