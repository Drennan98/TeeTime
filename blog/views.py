from django.contrib import messages
from django.views.generic import ListView, DetailView
from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Course, UserProfile, Comment
from .forms import PostForm, CommentForm, EditForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import DeleteView

# Create your views here.

# Class based views for mapping 
class PostList(ListView):
    queryset = Post.objects.filter(status=1).order_by("-created_on")
    template_name = "home/index.html"
    paginate_by = 5

class PostDetail(DetailView):
    model = Post
    template_name = "home/post_detail.html"
    context_object_name = "post"

class Course(ListView):
    model = Course
    template_name = "home/course.html"

class UserProfileView(ListView):
    model = UserProfile
    template_name = "home/user_profile.html"

class CommentListView(ListView):
    model = Comment
    template_name = "home/post_detail.html"

@login_required
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            messages.success(request, 'Post created successfully!')
            return redirect('post_detail', pk=post.pk)
        else:
            return render(request, 'blog/create_post.html', {'form': form})
    else:
        form = PostForm()
        return render(request, 'blog/create_post.html', {'form': form})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comments = post.comments.all()

    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.author = request.user
            new_comment.save()
            return redirect('post_detail', pk=post.pk)
    else:
        comment_form = CommentForm()

    return render(request, 'blog/post_detail.html', {
        'post': post,
        'comments': comments,
        'comment_form': comment_form
    })

@login_required
def delete_comment(request, slug, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    if comment.user == request.user:
        comment.delete()
        messages.success(request, 'Comment successfully deleted.')
        return redirect('post_detail', slug=slug)
    else:
        messages.error(request, 'You are not allowed delete this comment.')
        return redirect('post_detail', slug=slug)
    
def delete_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.user != post.author and not request.user.is_superuser:
        messages.error(request, 'You are not allowed delete this post.')
        return redirect('post_list', pk=post.pk)
    if request.method == 'POST':
        post.delete()
        messages.success(request, 'Post succesfully deleted.')
        response = redirect('create_post')
        return response
    return render(request, 'blog/create_post.html', {'post': post})

def edit_post(request, pk):
    post = get_object_or_404(Post, pk=pk)

    if request.user != post.author and not request.user.is_superuser:
        return redirect('post_list', pk=post.pk)

    if request.method == 'POST':
        form = EditForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            messages.success(request, "Post updated successfully.")
            return redirect('post_detail', pk=post.pk)
        else:
            messages.error(request, "An error occurred.")
    else:
        form = EditForm(instance=post)
    return render(request, 'blog/edit_post.html', {'form': form, 'post': post})
