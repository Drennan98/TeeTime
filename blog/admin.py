from django.contrib import admin
from .models import Post, Course, Comment, UserProfile

# Register your models here.

# Basic customization


class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "slug", "status", "created_on")
    list_filter = ("status",)
    search_fields = ["title", "content", "category"]


class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'post', 'body', 'created_on', 'active')
    search_fields = ('author', 'body')
    list_filter = ('active', 'created_on')


admin.site.register(Post, PostAdmin)
admin.site.register(Course)
admin.site.register(Comment)
admin.site.register(UserProfile)
