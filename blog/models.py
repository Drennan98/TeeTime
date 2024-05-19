from time import timezone
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

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

# The '-' before "created_on" is used so the most recently published posts will show up first.
class Meta:
    ordering = ['-created_on']

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title