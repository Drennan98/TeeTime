from django.views import generic
from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Comment
from django.core.paginator import Paginator
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib import messages

# Create your views here.

# Class based views for mapping 
class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by("-created_on")
    model = Post
    template_name = "home.html"
    paginate_by = 5

class PostDetail(generic.DetailView):
    model = Post
    template_name = "post_detail.html"

def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    queryset = Post.objects.filter(status=1)
    return render(request, 'blog/post_detail.html', {'post': post})

def signup(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        confirm_password = request.POST["confirm_password"]

        if password != confirm_password:
            messages.error (request, "The passwords do not match. Please try again.")
            return render (request, "form.html")
        
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already in use. Please try again.")
            return render (request, "form.html")
        
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already in use. Please try again.")
            return render (request, "form.html")
        
        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()

        # The user is sent back to home page upon successful sign-up.
        login(request, user)
        return redirect("home")
    
    return render (request, "home.html")