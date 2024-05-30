from django.contrib import admin
from .models import Post, Category, Comment

# Register your models here.

# Basic customization

class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "slug", "status", "created_on", "category")
    list_filter = ("status",)
    search_fields = ["title", "content", "category"]
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Post, PostAdmin)
admin.site.register(Category)
admin.site.register(Comment)
