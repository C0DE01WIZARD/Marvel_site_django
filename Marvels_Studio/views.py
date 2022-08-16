from django.shortcuts import render
from django.views.generic.base import View
from django.views.generic import ListView
from rest_framework.viewsets import ModelViewSet

from .models import Movie #
from .models import Actor

# Create your views here.


# REST API

def reg(request):
	return render(request, 'movies/regis.html')


class base(View):
	def get(self, request):
		actor = Actor.objects.all()
		return render(request, 'movies/base.html', {'actor_list': actor})


class MoviesView(View):  # создаём класс MoviesView и наследуемся от класса Django (Views)
	def get(self, request):  # создаём метод get которая будет приниать запросы http
		# request - присланная информация от нашего клиента, принимает запросы от браузера
		movies = Movie.objects.all() # с помощью менеджера objects забираем всю информацию
		return render(request, 'movies/movies.html', {'movie_list': movies})  # ключ словарь, записи
# наших фильмов


class Detail(View): # создаём класс Detail и наследуемся от класса Django (Views)
	def get(self, request, pk):  # принимаем get запрос, на который передаётся requset и pk, сюда придёт ID
		# pk некое число которое передаём из URL
		movie = Movie.objects.get(id=pk)  # делаем запрос в БД через модель мовие, метод get который
		# получает одну запись и id нашей записи сравнваем с пришедшим PK
		# в Django id определяется как Pk
		return render(request, 'movies/detail.html', {'movie': movie})



