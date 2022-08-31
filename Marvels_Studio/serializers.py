from rest_framework import serializers
from .models import Movie, Genre


class MovieSerializer(serializers.ModelSerializer): #сериализатор который работает с моделями
	class Meta:
		model = Movie
		fields = ('title', 'year', 'poster', 'actors', 'genres', 'url') # поля используемые для сериализации

