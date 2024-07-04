from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from blog.views import PostDetail, PostList, delete_post
from .views import edit_post, delete_post

urlpatterns = [
    path('', PostList.as_view(), name='blog'),
    path('post_detail/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.create_post, name='create_post'),
    path('delete_comment/<int:comment_id>/', views.delete_comment, name='delete_comment'),
    path('post/<int:pk>/delete/', views.delete_post, name='delete_post'),
    path('post/<int:pk>/edit/', views.edit_post, name='edit_post'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)