from . import models
from rest_framework import serializers


class DirectorSerializer(serializers.ModelSerializer):
    movies_count = serializers.SerializerMethodField()

    class Meta:
        model = models.Director
        fields = {"id", "name",'movies_count'}
    def get_movies_count(self, director):
        return director.movies.count()



class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Review
        fields = ("id","text", "movie", "star")

class MovieSerializer(serializers.ModelSerializer):
    director = DirectorSerializer()
    reviews = ReviewSerializer(many=True, read_only=True)
    average_rating = serializers.SerializerMethodField()
    class Meta:
        model = models.Movie
        fields = ("id", "title", "description", "duration", "director", 'reviews', "average_rating")

        def get_average_rating(self, movie):
            reviews = movie.reviews.all()
            if reviews:
                sum_reviews = sum(reviews.star for review in reviews)
                average = sum_reviews / len(reviews)
                return average
            return None
