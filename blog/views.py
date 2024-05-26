from django.views import generic
from django.shortcuts import render, get_object_or_404
from .models import Post, Comment
from django.core.paginator import Paginator

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