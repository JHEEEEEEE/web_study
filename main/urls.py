from django.contrib import admin
from django.urls import path

from main.views import *

# 이미지를 업로드하자
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    # 웹사이트의 첫화면은 index 페이지이다 + URL이름은 index이다
    path('', index, name='index'),
    # URL:80/contact에 접속하면 contact 페이지 + URL이름은 blog이다
    path('contact/', contact, name='contact'),
    # URL:80/contact/숫자로 접속하면 게시글-세부페이지(posting)
    path('contact/<int:pk>/',posting, name="posting"),

    path('contact/post_create/', post_create),

    path('contact/<int:pk>/remove/', remove_post),

    path('index/info/', info, name='info')
]

# 이미지 URL 설정
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)