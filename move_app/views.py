from django.shortcuts import render
from . import models, serializers
from rest_framework import generics


class DirectorlistAPIView(generics.ListAPIView):
    queryset = models.Director.objects.all()
    serializer_class = serializers.DirectorSerializer

class DirectorDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Director.objects.all()
    serializer_class = serializers.DirectorSerializer
    lookup_field = 'id'


class MovieListAPIView(generics.ListAPIView):
    queryset = models.Movie.objects.all()
    serializer_class = serializers.MovieSerializer


class MovieDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Movie.objects.all()
    serializer_class = serializers.MovieSerializer
    lookup_field = 'id'

class ReviewListAPIView(generics.ListAPIView):
    queryset = models.Review.objects.all()
    serializer_class = serializers.ReviewSerializer

class ReviewDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Review.objects.all()
    serializer_class = serializers.ReviewSerializer
    lookup_field = 'id'