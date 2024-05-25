from django.views import generic
from .models import Post, Comment
from django.core.paginator import Paginator

# Create your views here.

# Class based views for mapping 
class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by("-created_on")
    template_name = "home.html"
    paginate_by = 5

class PostDetail(generic.DetailView):
    model = Post
    template_name = "post_detail.html"