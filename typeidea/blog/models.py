from django.db import models
from django.contrib.auth.models import User

STATUS_ITEMS = (
    (0, '正常'),
    (1, '删除')
)

class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name='分类名')
    status = models.PositiveIntegerField(default=0, choices=STATUS_ITEMS, verbose_name='状态')
    is_nav = models.BooleanField(default=False, verbose_name='是否为导航')
    owner = models.ForeignKey(User, verbose_name='作者', on_delete=models.CASCADE)
    created_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = verbose_name_plural = '分类'

class Tag(models.Model):
    name = models.CharField(max_length=50, verbose_name='标签名')
    status = models.PositiveIntegerField(default=0, choices=STATUS_ITEMS, verbose_name='状态')
    owner = models.ForeignKey(User, verbose_name='作者', on_delete=models.CASCADE)    
    created_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = verbose_name_plural = '标签'

class Post(models.Model):
    title = models.CharField(max_length=255, verbose_name='标题')
    desc = models.CharField(max_length=1024, verbose_name='摘要')
    content = models.TextField(verbose_name='正文', help_text='正文请使用Markdown格式书写')
    status = models.PositiveIntegerField(default=0, choices=STATUS_ITEMS, verbose_name='状态')
    category = models.ForeignKey(Category, verbose_name='分类', on_delete=models.CASCADE)
    tag = models.ManyToManyField(Tag, verbose_name='标签')
    owner = models.ForeignKey(User, verbose_name='作者', on_delete=models.CASCADE)
    created_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = verbose_name_plural = '文章'
        ordering = ['-created_time']