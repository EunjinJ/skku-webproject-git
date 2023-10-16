# ~~~ DB 입력 시 제한사항 ~~~

# 별점을 1~5 사이로 제한
from django.core.exceptions import ValidationError
def validate_star_range(value):
    if 1 > value and value < 5:
        raise ValidationError('별점은 1에서 5 사이의 값이어야 합니다')



# ~~~ 데이터 베이스 ~~~
from django.db import models
from main.models import TripCategory
from main.models import AreaM
from user.models import User
from main.models import AreaM

class Trip(models.Model):
    id = models.AutoField(primary_key=True)
    trip_category_id = models.ForeignKey(TripCategory, on_delete=models.SET_NULL, null=True)
    trip_category_detail = models.CharField(max_length=255)
    trip_name = models.CharField(max_length=255)
    trip_address = models.TextField()

    # trip_open = models.TimeField() # 영업 시작시간
    # trip_closed = models.TimeField() # 영업 종료시간
    # trip_break_start = models.TimeField()
    # trip_break_end = models.TimeField()
    # trip_last_order = models.TimeField()
    area_m_ID = models.ForeignKey(AreaM, on_delete=models.SET_NULL, null=True)
    trip_time = models.CharField(max_length=512, null=True)
    trip_phone = models.CharField(max_length=255) # 031-000-0000 이렇게 문자열로
    trip_homepage = models.TextField()
    is_deleted = models.BooleanField(default=False)

    @classmethod
    def get_active_list(cls):
        return cls.objects.filter(is_deleted=False)

    @property
    def is_active(self):
        return not self.is_deleted

class Menu(models.Model):
    id = models.AutoField(primary_key=True)
    trip_id = models.ForeignKey(Trip, on_delete=models.SET_NULL, null=True)
    menu_content = models.CharField(max_length=255) # 메뉴 이름이 255자를 넘어가진 않겠지
    menu_price = models.IntegerField()

class Info(models.Model):
    id = models.AutoField(primary_key=True)
    trip_id = models.ForeignKey(Trip, on_delete=models.SET_NULL, null=True)
    info_content = models.TextField()

class TripComment(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    trip_id = models.ForeignKey(Trip, on_delete=models.SET_NULL, null=True)
    trip_comment_content = models.TextField()
    trip_commnet_time = models.DateTimeField(auto_now_add=True)
    trip_comment_star = models.IntegerField(validators=[validate_star_range]) # 1 2 3 4 5 정수로 넣을 수 있음
    is_deleted = models.BooleanField()

class Review(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    trip_id = models.ForeignKey(Trip, on_delete=models.SET_NULL, null=True)
    review_title = models.CharField(max_length=255)
    review_content = models.TextField()
    review_time = models.DateTimeField(auto_now_add=True)
    is_deleted = models.BooleanField()

class ReviewComment(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    review_id = models.ForeignKey(Review, on_delete=models.SET_NULL, null=True)
    review_comment_content = models.TextField()
    review_commnet_time = models.DateTimeField(auto_now_add=True)
    is_deleted = models.BooleanField()

class ReviewRecommend(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    review_id = models.ForeignKey(Review, on_delete=models.SET_NULL, null=True)
    review_recommend = models.BooleanField()
    is_deleted = models.BooleanField()