from django.db import models

# Create your models here.

class Tournament(models.Model):
    name = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField()

class Player(models.Model):
    name = models.CharField(max_length=255)
    score = models.IntegerField()
    tournamet = models.ForeignKey(Tournament, on_delete=models.CASCADE)