from . import views
from django.urls import path

urlpatterns = [
    path('directors/', views.DirectorlistAPIView.as_view(), name='director-list'),
    path('directors/<int:id>/', views.DirectorDetailAPIView.as_view(), name='director-detail'),
    path('movies/', views.MovieListAPIView.as_view(), name='movie-list'),
    path('movies/<int:id>/', views.MovieDetailAPIView.as_view(), name='movie-detail'),
    path('reviews/', views.ReviewListAPIView.as_view(), name='review-list'),
    path('reviews/<int:id>/', views.ReviewDetailAPIView.as_view(), name='review-detail'),


]