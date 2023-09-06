from django.db import models
from datetime import date

# Create your models here.
# 게시글(Post)엔 제목(title), 내용(contents)이 존재합니다
class Post(models.Model):
    title = models.CharField(max_length=50)
    writer = models.CharField(max_length=30, default="Anonymous")
    password = models.CharField(max_length=30, blank=True)
    date = models.DateField(auto_now_add=True)
    count = models.IntegerField(default=0)
        # 게시글 Post에 이미지 추가
    mainphoto = models.ImageField(blank=True, null=True)
    contents = models.TextField()

    # 게시글의 제목(title)이 Post object 대신하기
    def __str__(self):
        return self.title