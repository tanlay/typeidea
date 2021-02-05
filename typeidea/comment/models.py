from django.db import models
from django.contrib.auth.models import User

from blog.models import Tag, Category, Post

STATUS_ITEMS = (
    (0, '正常'),
    (1, '删除')
)

class Comment(models.Model):
    target = models.ForeignKey(Post, verbose_name='评论目标文章', on_delete=models.CASCADE)
    content = models.CharField(max_length=2000, verbose_name='内容')
    nickname = models.CharField(max_length=50, verbose_name='昵称')
    website = models.URLField(verbose_name='网站')
    email = models.EmailField(verbose_name='邮箱')
    status = models.PositiveIntegerField(default=0, choices=STATUS_ITEMS, verbose_name='状态')
    created_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

    def __str__(self):
        return self.nickname

    class Meta:
        verbose_name = verbose_name_plural = '评论'