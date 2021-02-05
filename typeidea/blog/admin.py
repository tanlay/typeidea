from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html

from blog.models import Tag, Category, Post

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name','status', 'is_nav', 'created_time')
    fields = ('name', 'status', 'is_nav')

    # def post_count(self, obj):
    #     return obj.post_set.count()
    # post_count.short_description = '文章数量'

    def save_model(self, request, obj, form, change):
        obj.owner = request.user
        return super(CategoryAdmin, self).save_model(request, obj, form, change)

class TagAdmin(admin.ModelAdmin):
    list_display = ('name','status', 'created_time')
    fields = ('name', 'status')

    def save_model(self, request, obj, form, change):
        obj.owner = request.user
        return super(TagAdmin, self).save_model(request, obj, form, change)

class PostAdmin(admin.ModelAdmin):
    # 展示列表字段
    list_display = ['title', 'category', 'status', 'created_time']
    # list_display = ['title', 'category', 'status', 'created_time', 'operator']
    list_display_links = []
    # 配置页面过滤字段
    list_filter = ['category']
    # 配置搜索字段
    search_fields = ['title', 'category__name']
    
    # 动作相关配置，是否展示在顶部
    actions_on_top = True
    # 动作相关配置，是否展示在底部
    #  actions_on_bottom = True

    # 编辑页面
    save_on_top = True

    fields = (
        ('title', 'category'),
        'desc',
        'status',
        'content',
        'tag',
    )

    # 定义编辑按钮，点击进入编辑
    def operator(self, obj):
        return format_html(
            '<a href="{}">编辑</a>',
            reverse('admin:blog_post_change', args=(obj.id,))
        )
    operator.short_description = '操作'

    def save_model(self, request, obj, form, change):
        obj.owner = request.user
        return super(PostAdmin, self).save_model(request, obj, form, change)


admin.site.register(Tag, TagAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
