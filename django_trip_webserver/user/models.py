# ~~~ DB 입력 시 제한사항 ~~~

# 아직 없음



# ~~~ 데이터 베이스 ~~~
from django.db import models
from main.models import TripCategory

class User(models.Model):
    id = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=255)
    user_password = models.CharField(max_length=255) # type 이거 맞나?
    trip_category_1_id = models.ForeignKey(TripCategory, on_delete=models.SET_NULL, null=True, related_name='trip_category_1')
    trip_category_2_id = models.ForeignKey(TripCategory, on_delete=models.SET_NULL, null=True, related_name='trip_category_2')
    trip_category_3_id = models.ForeignKey(TripCategory, on_delete=models.SET_NULL, null=True, related_name='trip_category_3')
    is_deleted = models.BooleanField()
