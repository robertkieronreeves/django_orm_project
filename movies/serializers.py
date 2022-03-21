from dataclasses import fields
from re import A
from matplotlib.pyplot import cla
from rest_framework import serializers
from .models import Actor, Movie

class ActorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Actor
        fields = ('name')

class MovieSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Movie
        fields = ('title', 'genre', 'actor')
