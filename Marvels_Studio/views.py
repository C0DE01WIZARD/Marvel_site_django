from django.http import HttpResponse
from django.shortcuts import render
from Marvels_Studio.views import *
from django.views.generic.base import View
from django.views.generic import ListView, DetailView,TemplateView
from rest_framework.viewsets import ModelViewSet
from rest_framework import generics # импортируем для представления DRF
from .models import Movie #
from .models import Actor
from .serializers import MovieSerializer # REST API
from Marvels_Studio.models import *


class Movies(View):  # создаём класс MoviesView и наследуемся от класса Django (Views)
	def get(self, request):  # создаём метод get которая будет приниать запросы http
		# request - присланная информация от нашего клиента, принимает запросы от браузера
		movies = Movie.objects.all() # с помощью менеджера objects забираем всю информацию
		return render(request, 'movies/movieS.html', {'movie_list': movies})  # ключ словарь, записи
# наших фильмов


class Detail(View): # создаём класс Detail и наследуемся от класса Django (Views)
	def get(self, request, slug):  # принимаем get запрос, на который передаётся requset и pk, сюда придёт ID
		# pk некое число которое передаём из URL
		movie = Movie.objects.get(url=slug)  # делаем запрос в БД через модель мовие, метод get который
		# получает одну запись и id нашей записи сравнваем с пришедшим PK
		# в Django id определяется как Pk
		return render(request, "movies/detail.html", {"movies": movie})


#def Movies(request, movieid):
	#return HttpResponse(f'<h1> Статьи </h1><p> {movieid}</p>')


class About(View):
	def get(self, request):
		movie2 = Movie.objects.all()
		return render(request, "movies/about.html", {"movie": movie2})

# Поиск фильмов
class Search(ListView):
	paginate_by = 3 #Будем выводить по три фильма

	def get_queryset(self): #метод фильтрации по полю title__icontains чтоб не учитывался регистр
		return Movie.objects.filter(title__icontains=self.request.GET.get("q")) # сравниваем данные которые пришли в GET запросе

	def get_context_data(self, *args, **kwargs):
		context = super().get_context_data(*args, **kwargs)
		context ["q"]=self.request.GET.get("q")
		return context


class MovieAPI(generics.ListAPIView):
	queryset = Movie.objects.all()
	serializer_class = MovieSerializer





class AboutUsView(TemplateView):
	template_name = "movies/about us.html"


class AboutRegView(TemplateView):
	template_name = "movies/reg.html"


class AboutFeedView(TemplateView):
	template_name = "movies/feedback.html"


class AboutDateView(TemplateView):
	template_name = "movies/date.html"


class AboutPagiView(TemplateView):
	template_name = "movies/pagi.html"





class AboutListView(TemplateView):
	template_name = "movies/list.html"


class News(TemplateView):
	template_name = "movies/news.html"