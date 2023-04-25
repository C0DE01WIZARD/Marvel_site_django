from rest_framework import serializers
from .models import * # импорт модели MOvie


class MovieSerializer(serializers.ModelSerializer):  # сериализатор который работает с моделями, наследуемся
	class Meta: # вложенный класс
		model = Movie
		fields = ('title', 'year', 'poster', 'actors', 'genres', 'url')  # поля используемые для сериализации


class MovieSerializer2(serializers.ModelSerializer):  # сериализатор который работает с моделями, наследуемся
	class Meta: # вложенный класс
		model = Movie
		fields = ('title', 'year', 'poster', 'actors', 'genres')  # поля используемые для сериализации
