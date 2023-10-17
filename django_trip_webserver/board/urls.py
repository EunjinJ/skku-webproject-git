from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views # 현재 경로에 있는 views.py를 가져옴
app_name = 'board'
urlpatterns = [
    path('trip/', views.trip_list, name='trip_list'),  # trip_list 뷰에 대한 URL 경로 추가
    path('trip/<int:board_id>', views.trip_detail, name='trip_detail'),  # trip_detail 뷰에 대한 URL 경로 추가
    path('trip/write', views.trip_write, name='trip_write'), # trip_write 뷰에 대한 URL 경로 추가
    path('trip/<int:trip_id>/review', views.review_list, name='review_list'),
    path('trip/<int:trip_id>/review/<int:review_id>', views.review_detail, name='review_detail'),
    path('trip/<int:trip_id>/review/write', views.review_write, name='review_write'),
    # path('<int:board_id>/edit/', views.board_edit, name="edit"), # trip_edit 뷰에 대한 URL 경로 추가
    # path('<int:board_id>/del/', views.board_delete, name='delete'), # trip_delete 뷰에 대한 URL 경로 추가
    # path('comments/',views.comment_list, name="comment_list") # trip_comment 뷰에 대한 URL 경로 추가
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

