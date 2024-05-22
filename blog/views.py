from django.views import generic
from .models import Category, Post

# Create your views here.

# Class based views for mapping 
class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by("-created_on")
    template_name = "index.html"

class PostDetail(generic.DetailView):
    model = Post
    template_name = "post_detail.html"

class CategoryList(generic.CategoryView):
    model = Category
    template_name = "category_list.html"