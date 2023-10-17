# ~~~ DB 입력 시 제한사항 ~~~

# 아직 없음



# ~~~ 데이터 베이스 ~~~
from django.db import models

class TripCategory(models.Model):
    id = models.AutoField(primary_key=True)
    trip_category_name = models.CharField(max_length=255)

class AreaL(models.Model):
    id = models.AutoField(primary_key=True)
    area_l_name = models.CharField(max_length=255) # 경기도, 서울특별시 ...

class AreaM(models.Model):
    id = models.AutoField(primary_key=True)
    area_l_id = models.ForeignKey(AreaL, on_delete=models.SET_NULL, null=True, related_name='aream_set') # related_name은 역참조 용도
    area_m_name = models.CharField(max_length=255) # 과천시, 종로구 ...