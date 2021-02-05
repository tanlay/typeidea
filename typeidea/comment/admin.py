from django.contrib import admin
from comment.models import Comment

class CommentAdmin(admin.ModelAdmin):
    list_display = ('target', 'nickname', 'content', 'website', 'created_time')


admin.site.register(Comment, CommentAdmin)