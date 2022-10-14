from django.db import models
from datetime import datetime

# Create your models here.

class Review(models.Model):
    title = models.CharField(max_length=40)
    content = models.TextField()
    movie_name = models.CharField(max_length=40)
    grade = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
