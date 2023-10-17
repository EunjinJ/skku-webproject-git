from django.urls import path

from . import views # 현재 경로에 있는 views.py를 가져옴

urlpatterns = [
    path('', views.search, name='search'),
    # path('trip/', views.search_trip, name='search_trip'),
    # path('trip_comment/', views.search_trip_comment, name='search_trip_comment'),
    # path('review/', views.search_review, name='search_review'),
    # path('review_comment/', views.search_review, name='search_review_comment'),
]