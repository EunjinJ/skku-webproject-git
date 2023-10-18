
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from django.urls import path

from . import views # 현재 경로에 있는 views.py를 가져옴

app_name = 'main'

urlpatterns = [
    path('', views.main, name='main'),
    path('main_seoul', views.main_seoul, name='seoul'),
    path('category', views.category, name='category'),
    path("admin/", admin.site.urls),
    path("board/", include('board.urls')),
    path("main/", include('main.urls')),
    path("user/", include('user.urls')),
    path("search/", include('search.urls'))
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)