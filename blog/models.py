from django.db import models
from user.models import User


class Category(models.Model):
    name = models.CharField("카테고리이름b", max_length=20, blank=False, null=False)
    describtion = models.TextField("설명")

    def __str__(self):
        return self.name


class Article(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField("글 제목", max_length=100, blank=False, null=False)
    category = models.ManyToManyField(to=Category, verbose_name="카테고리")
    content = models.TextField("글 내용", blank=False, null=False)

    def __str__(self):
        return self.title


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    author = models.ForeignKey(User,  on_delete=models.CASCADE)
    writing_time = models.TimeField()
    content = models.TextField("댓글 내용")
