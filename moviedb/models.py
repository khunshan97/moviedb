from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Movie(models.Model):
    name = models.CharField(max_length=50)
    genre = models.CharField(max_length=50, default="")
    short_des = models.CharField(max_length=200)
    long_des = models.CharField(max_length=500)
    thumb_url = models.URLField(max_length=200)
    video_url = models.URLField(max_length=200)
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Review(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    rating = models.IntegerField()
    text = models.CharField(max_length=300)
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.movie.name
