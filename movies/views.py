from django.shortcuts import render
from rest_framework import viewsets
from .serializers import ActorSerializer, MovieSerializer
from .models import Actor, Movie

# Create your views here.

class ActorViewSet(viewsets.ModelViewSet):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer

class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all().order_by('title')
    serializer_class = MovieSerializer

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')