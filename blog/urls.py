from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from blog.views import PostDetail, PostList

urlpatterns = [
    path('', PostList.as_view(), name='blog'),
    path('post_detail/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.create_post, name='create_post'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)