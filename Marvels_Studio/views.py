
from django.shortcuts import render
from django.views.generic.base import View
from .models import Movie
# Create your views here.


class MoviesView(View): # создаём класс MoviesView и наследуемся от класса Django Views
	def get(self, request): # создаём метод get которая будет приниать запросы http
		# request - присланная информация от нашего клиента, принимает запросы от браузера
		movies = Movie.objects.all()
		return render(request, 'movies/Home.html', {'movie_list': movies}) # ключ словарь, записи
	# наших фильмов