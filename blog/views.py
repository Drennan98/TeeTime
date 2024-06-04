from django.views.generic import ListView, DetailView
from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Course, UserProfile, Comment
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib import messages

# Create your views here.

# Class based views for mapping 
class PostList(ListView):
    queryset = Post.objects.filter(status=1).order_by("-created_on")
    model = Post
    template_name = "home.html"
    paginate_by = 5

class PostDetail(DetailView):
    model = Post
    template_name = "post_detail.html"

def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    queryset = Post.objects.filter(status=1)
    return render(request, 'blog/post_detail.html', {'post': post})

class CourseListView(ListView):
    model = Course
    template_name = "course.html"

class UserProfileView(ListView):
    model = UserProfile
    template_name = "user_profile.html"

class Comment(ListView):
    model = Comment
    template_name = "post_detail.html"

