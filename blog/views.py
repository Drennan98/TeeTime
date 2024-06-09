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
    template_name = "home/home.html"
    paginate_by = 5

class PostDetail(DetailView):
    model = Post
    template_name = "home/post_detail.html"

class Course(ListView):
    model = Course
    template_name = "home/course.html"

class UserProfileView(ListView):
    model = UserProfile
    template_name = "home/user_profile.html"

class Comment(ListView):
    model = Comment
    template_name = "home/post_detail.html"
