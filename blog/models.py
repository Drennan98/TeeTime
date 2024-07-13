from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from autoslug import AutoSlugField

STATUS = (
    (0, "Draft"),
    (1, "Publish")
)

# This is my blog post model. Users can share posts.


class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = AutoSlugField(
        populate_from='title',
        unique=True,
        always_update=True
    )
    content = models.TextField()
    author = models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name='golf_posts'
    )
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=1)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_on']

# This is my comment model. Users can comment on posts.


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    post = models.ForeignKey(
        Post,
        related_name="comments",
        on_delete=models.CASCADE
    )
    author = models.CharField(max_length=80)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return f"Comment by {self.author} on {self.post}"


# This is my golf course model. Users can compare golf courses.
class Course(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    created_on = models.DateTimeField(auto_now_add=True)
    description = models.TextField()
    rating = models.FloatField()

    def __str__(self):
        return self.name


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)

    def __str__(self):
        return self.user.username
