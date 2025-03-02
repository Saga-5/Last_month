from django.contrib import admin
from django.views.static import directory_index

from . import models

@admin.register(models.Director)
class DirectorAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(models.Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('title','director','duration')
    search_fields = ('title',"directory__name")
    list_filter = ('director',)

@admin.register(models.Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('movie','text')
    search_fields = ('movie__title',"text")
    list_filter = ('movie',)