from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.base import View
from django.views.generic import ListView
from rest_framework.viewsets import ModelViewSet
from rest_framework import generics # импортируем для представления DRF
from .models import Movie #
from .models import Actor
from .serializers import MovieSerializer # REST API
from django.views import View


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
		return render(request, 'movies/movieS.html', {'movie_list': movies})  # ключ словарь, записи
# наших фильмов


class Detail(View): # создаём класс Detail и наследуемся от класса Django (Views)
	def get(self, request, pk):  # принимаем get запрос, на который передаётся requset и pk, сюда придёт ID
		# pk некое число которое передаём из URL
		movie = Movie.objects.get(id=pk)  # делаем запрос в БД через модель мовие, метод get который
		# получает одну запись и id нашей записи сравнваем с пришедшим PK
		# в Django id определяется как Pk
		return render(request, "movies/detail.html", {"movie": movie})

#Поиск фильмов


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


class AboutView(TemplateView):
	template_name = "movies/about.html"


class AboutUsView(TemplateView):
	template_name = "movies/about us.html"


class AboutRegView(TemplateView):
	template_name = "movies/reg.html"


class AboutFeedView(TemplateView):
	template_name = "movies/feedback.html"


class AboutDateView(TemplateView):
	template_name = "movies/date.html"


class AboutPagiView(TemplateView):
	template_name = "movies/pagination.html"


class AboutMoviesView(TemplateView):
	template_name = "movies/movieS.html"


class AboutListView(TemplateView):
	template_name = "movies/list.html"