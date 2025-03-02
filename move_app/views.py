from wsgiref.validate import validator

from django.shortcuts import render
from . import models, serializers
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status


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

    def post(self, request, *args, **kwargs):
        validator = serializers.MovieValiditySerializer(data=request.data)
        if not validator.is_valid():
            return Response(validator.errors, status=status.HTTP_400_BAD_REQUEST)
        title = validator.validated_data.get('title')
        description = validator.validated_data.get('description')
        director_id = validator.validated_data.get('director')
        duration = validator.validated_data.get('duration')
        movie = models.Movie.objects.create(title=title, description=description, director_id=director_id, duration=duration)
        return Response(serializers.MovieSerializer(movie).data, status=status.HTTP_201_CREATED)

class MovieDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Movie.objects.all()
    serializer_class = serializers.MovieSerializer
    lookup_field = 'id'

    def put(self, request, *args, **kwargs):
        movie_detail = self.get_object()
        validator = serializers.MovieValiditySerializer(data=request.data)
        if not validator.is_valid():
            return Response(validator.errors, status=status.HTTP_400_BAD_REQUEST)
        movie_detail.title = validator.validated_data.get('title')
        movie_detail.description = validator.validated_data.get('description')
        movie_detail.director_id = validator.validated_data.get('director')
        movie_detail.duration = validator.validated_data.get('duration')
        movie_detail.save()
        return Response(serializers.MovieSerializer(movie_detail).data, status=status.HTTP_200_OK)



class ReviewListAPIView(generics.ListAPIView):
    queryset = models.Review.objects.all()
    serializer_class = serializers.ReviewSerializer

    def post(self, request, *args, **kwargs):
        validator = serializers.ReviewValiditySerializer(data=request.data)
        if not validator.is_valid():
            return Response(validator.errors, status=status.HTTP_400_BAD_REQUEST)
        text = validator.validated_data.get('text')
        star = validator.validated_data.get('star',5)
        movie_id = validator.validated_data.get('movie_id')
        review = models.Review.objects.create(text=text, star=star, movie_id=movie_id)
        review.save()
        return Response(serializers.ReviewSerializer(review).data, status=status.HTTP_200_OK)


class ReviewDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Review.objects.all()
    serializer_class = serializers.ReviewSerializer
    lookup_field = 'id'

    def put(self, request, *args, **kwargs):
        review_diteil = self.get_object()
        validator = serializers.ReviewValiditySerializer(data=request.data)
        if not validator.is_valid():
            return Response(validator.errors, status=status.HTTP_400_BAD_REQUEST)
        review_diteil.text = validator.validated_data.get('text')
        review_diteil.star = validator.validated_data.get('star')
        review_diteil.movie_id = validator.validated_data.get('movie_id')
        review_diteil.save()
        return Response(serializers.ReviewSerializer(review_diteil).data, status=status.HTTP_200_OK)