from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from blog.views import PostDetail, PostList

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('home/', views.PostList.as_view(), name='home'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)