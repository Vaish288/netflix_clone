from rest_framework import serializers
from .models import *

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ['name']

class ActorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actors
        fields = ['name']

class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model= Video
        fields= ['file']

class MoviesSerializer(serializers.ModelSerializer):
    genres = GenreSerializer(many=True)
    actors = ActorsSerializer(many=True)
    video=VideoSerializer(many=True)
    class Meta:
        model=Movies
        fields = '__all__'

class TVShowsSerializer(serializers.ModelSerializer):
    genres = GenreSerializer(many=True)
    actors = ActorsSerializer(many=True)
    class Meta:
        model= TVShows
        fields = '__all__'

class EpisodeSerializer(serializers.ModelSerializer):
    video=VideoSerializer(many=True)
    class Meta:
        model=Episodes
        fields= '__all__'