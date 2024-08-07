from . import views
from .views import (
    GolfCourseListView,
    GolfCourseDetailView,
    GolfCourseCreateView,
    GolfCourseUpdateView,
    GolfCourseDeleteView,
    golf_courses_list
)

from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from blog.views import PostDetail, PostList
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('blog/', PostList.as_view(), name='blog'),
    path('list/', GolfCourseListView.as_view(), name='golfcourse_list'),
    path(
        '<int:pk>/',
        GolfCourseDetailView.as_view(),
        name='golfcourse_detail'
    ),
    path('create/', GolfCourseCreateView.as_view(), name='golfcourse_create'),
    path(
        '<int:pk>/update/',
        GolfCourseUpdateView.as_view(),
        name='golfcourse_update'
    ),
    path(
        '<int:pk>/delete/',
        GolfCourseDeleteView.as_view(),
        name='golfcourse_delete'
    ),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('golf-courses/', views.golf_courses_list, name='golf-courses'),
    path('home/', views.home_view, name='home'),
    path('', views.home_view, name='home'),
    path(
        'delete/<int:course_id>/',
        views.delete_golfcourse,
        name='delete_golfcourse'
    )
]
