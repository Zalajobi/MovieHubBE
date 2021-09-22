from django.db import models


# Create your models here.
from django.utils import timezone


class Genre(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=150)
    releaseYear = models.IntegerField()
    numberInStock = models.IntegerField()
    dailyRate = models.FloatField()
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    dateCreated = models.DateTimeField(default=timezone.now)
