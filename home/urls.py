from . import views 
from .views import (
    GolfCourseListView,
    GolfCourseDetailView,
    GolfCourseCreateView,
    GolfCourseUpdateView,
    GolfCourseDeleteView
)

from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from blog.views import PostDetail, PostList

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('home/', views.PostList.as_view(), name='home'),
    path('list/', GolfCourseListView.as_view(), name='golfcourse_list'),
    path('<int:pk/', GolfCourseDetailView.as_view(), name='golfcourse_detail'),
    path('create/', GolfCourseCreateView.as_view(), name='golfcourse_create'),
    path('<int:pk>/update/', GolfCourseUpdateView.as_view(), name='golfcourse_update'),
    path('<int:pk>/delete/', GolfCourseDeleteView.as_view(), name='golfcourse_delete'),
]