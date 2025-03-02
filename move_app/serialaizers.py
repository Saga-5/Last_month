from . import models
from rest_framework import serializers

class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Directory
        fields = {"id", "name"}


class MovieSerializer(serializers.ModelSerializer):
    director = DirectorSerializer()
    class Meta:
        model = models.Movie
        fields = ("id", "title", "description", "duration", "director")

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Review
        fields = ("id","text", "movie")