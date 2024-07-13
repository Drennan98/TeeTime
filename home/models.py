from django.db import models

# Create your models here.

# Golf course model for users


class GolfCourse(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    par = models.IntegerField()
    holes = models.IntegerField()
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
        