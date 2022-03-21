from __future__ import unicode_literals

from django.db import models

# Create your models here.

GENRE_CHOICES = [
    ('CO', 'Comedy'),
    ('AC', 'Action'),
    ('DR', 'Drama'),
    ('HO', 'Horror')
]

class Actor(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Movie(models.Model):
    title = models.CharField(max_length=100)
    genre = models.CharField(max_length=2,
                             choices=GENRE_CHOICES,)
    actor = models.ManyToManyField(Actor, related_name="movies")

    def __str__(self):
        return self.title
