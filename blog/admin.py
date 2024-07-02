from django.contrib import admin
from .models import Post, Course, Comment, UserProfile

# Register your models here.

# Basic customization

class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "slug", "status", "created_on")
    list_filter = ("status",)
    search_fields = ["title", "content", "category"]

admin.site.register(Post, PostAdmin)
admin.site.register(Course)
admin.site.register(Comment)
admin.site.register(UserProfile)
