from time import timezone
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

# Used for filtering posts based on their status
STATUS = (
    (0, "Draft"),
    (1, "Publish")
)

# Post class with basic structure.
class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='golf_posts')
    updated_on = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
    
# Comment class with basic structure
class Comment(models.Model):
    post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return f"Comment by {self.name} on {self.post}"

# The '-' before "created_on" is used so the most recently published posts will show up first.
class Meta:
    ordering = ['-created_on']

