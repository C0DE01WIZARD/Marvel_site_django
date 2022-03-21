
from django.shortcuts import render
from django.views.generic.base import View
from .models import Movie
# Create your views here.


class MoviesView(View): # создаём класс MoviesView и наследуемся от класса Django Views
	def get(self, request): # создаём метод get которая будет приниать запросы http
		# request - присланная информация от нашего клиента, принимает запросы от браузера
		movies = Movie.objects.all()
		return render(request, 'movies/Movies.html', {'movie_list': movies}) # ключ словарь, записи
	# наших фильмов


class MovieDetailViews(View):
	def get(self, request, pk): # принимаем get запрос, на который передаётся requset pk
		movie = Movie.objects.get(id=pk) # делаем запрос в БД через модель мовие, метод get который
		# получает одну запись
		return render(request, 'movies/movie_detail.html', {'movie': movie})


def Movies(request):
	return render(request, 'movies/Movies.html')