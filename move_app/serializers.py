from . import models
from rest_framework import serializers


class DirectorSerializer(serializers.ModelSerializer):
    name = serializers.CharField(min_length=2, max_length=100)
    movies_count = serializers.SerializerMethodField()

    class Meta:
        model = models.Director
        fields = ["id", "name", "movies_count"]  # Используем список, а не множество

    def get_movies_count(self, director):
        return director.movies.count()


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Review
        fields = ("id", "text", "movie", "star")

class ReviewValiditySerializer(serializers.ModelSerializer):
    text = serializers.CharField()
    star = serializers.IntegerField(min_value=1, max_value=5)
    movie = serializers.IntegerField()


class MovieSerializer(serializers.ModelSerializer):
    director = DirectorSerializer()
    reviews = ReviewSerializer(many=True, read_only=True)
    average_rating = serializers.SerializerMethodField()

    class Meta:
        model = models.Movie
        fields = ("id", "title", "description", "duration", "director", "reviews", "average_rating")

    def get_average_rating(self, movie):
        reviews = movie.reviews.all()
        if reviews:
            sum_reviews = sum(review.star for review in reviews)  # Исправлено: правильно суммируем рейтинги
            average = sum_reviews / len(reviews)
            return average
        return None


class MovieValiditySerializer(serializers.Serializer):
    title = serializers.CharField(min_length=2, max_length=100)
    description = serializers.CharField()
    duration = serializers.IntegerField()
    director = serializers.IntegerField()