from rest_framework import serializers
from .models import Movie


class MovieSerializer(serializers.ModelSerializer): #сериализатор который работает с моделями
	class Meta:
		model = Movie
		fields = ('title', 'year') # поля используемые для сериализации
