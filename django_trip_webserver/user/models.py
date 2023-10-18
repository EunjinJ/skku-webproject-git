# ~~~ DB 입력 시 제한사항 ~~~

# 아직 없음



# ~~~ 데이터 베이스 ~~~
from django.db import models
from main.models import TripCategory


# 앞으로 우린 장고 제공 User를 이용할 것이므로 회원가입시 해당 DB 사용하지 않음
# 웹스크래핑한 결과에 있는 유저만 해당 DB에 넣어둠
class User(models.Model): 
    id = models.CharField(max_length=255, primary_key=True)
    user_name = models.CharField(max_length=255)
    user_password = models.CharField(max_length=255)
    user_type = models.CharField(max_length=20)
    trip_category_1_id = models.ForeignKey(TripCategory, on_delete=models.SET_NULL, null=True, related_name='user_trip_category_1')
    trip_category_2_id = models.ForeignKey(TripCategory, on_delete=models.SET_NULL, null=True, related_name='user_trip_category_2')
    trip_category_3_id = models.ForeignKey(TripCategory, on_delete=models.SET_NULL, null=True, related_name='user_trip_category_3')
    is_deleted = models.BooleanField()


# 장고 제공 User는 알아서 잘 있음
# 아래 DB는 장고 제공 User와 연결하는 용도
# from django.contrib.auth.models import User
class UserInfo(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.PROTECT)
    user_type = models.CharField(max_length=20)
    trip_category_1_id = models.ForeignKey(TripCategory, on_delete=models.SET_NULL, null=True, related_name='userinfo_trip_category_1')
    trip_category_2_id = models.ForeignKey(TripCategory, on_delete=models.SET_NULL, null=True, related_name='userinfo_trip_category_2')
    trip_category_3_id = models.ForeignKey(TripCategory, on_delete=models.SET_NULL, null=True, related_name='userinfo_trip_category_3')
    is_deleted = models.BooleanField()
