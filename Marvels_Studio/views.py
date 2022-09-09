from django.contrib.auth.forms import UserCreationForm


from django.urls import reverse_lazy
from rest_framework.response import Response
from Marvels_Studio.views import *
from django.views.generic.base import View
from django.views.generic import ListView, DetailView, TemplateView, CreateView
from django.views.generic.detail import DataMixin
from .forms import * # импорт формы из forms.py
from Marvels_Studio.models import *
from rest_framework.views import APIView
from django.core.paginator import Paginator
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin

# повторить материал https://www.youtube.com/watch?v=u37FXeVQIpU&list=PLA0M1Bcd0w8xO_39zZll2u1lz_Q-Mwn1F&index=13
def add(request): # форма
	if request.method == 'POST':
		form = FormAdd(request.POST)
		if form.is_valid():
			print(form.cleaned_data, 'Данные переданы через POST запрос!!!')
	else:
		form = FormAdd()
	return render(request, 'movies/+.html', {'form': form})# 'form' присваем значение переменной form


# class Movies(DataMixin, ListView):  # создаём класс MoviesView и наследуемся от класса Django (Views)
# 	def get(self, request):  # создаём метод get которая будет приниать запросы http
# 		# request - присланная информация от нашего клиента, принимает запросы от браузера
# 		movies = Movie.objects.all() # с помощью менеджера objects забираем всю информацию
# 		return render(request, 'movies/movies.html', {'movie_list': movies})  # ключ словарь, записи
# # наших фильмов


def Movies(request):
	contact_list = Movie.objects.all()
	paginator = Paginator(contact_list, 1)

	page_number = request.GET.get('page')
	page_obj = paginator.get_page(page_number)
	return render(request, 'movies/movies.html', {'page_obj': page_obj} )



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

# class Search(ListView):


#class MovieAPI(generics.ListAPIView):
	#queryset = Movie.objects.all()
	#serializer_class = MovieSerializer


class MovieAPI(APIView): #API ЗАПРОС
	def get(self, request): # запрос GET
		lst = Movie.objects.all().values()
		return Response({'post': list(lst)}) # передача данных в GET запрос для вывоода

	def post(self, request): # ЗАПРОС POSTб добавление данных в БД
		post_new = Movie.objects.create()
		return Response({'title': 'Тор'})


class AboutUsView(View):
	def get(self, request):
		info = Info.objects.all()
		famous1 = Famous_actors.objects.all()
		return render (request, "movies/about us.html", {'infos': info, 'famous': famous1})


class AboutRegView(TemplateView):
	template_name = "movies/reg.html"


class Register(DataMixin, CreateView):
	form_class = UserCreationForm # стандартная форма для регистрации пользователей
	template_name = "movies/auth.html" # ссылка на шаблон
	success_url = reverse_lazy('login') # перенаправление при успешной авторизации

	# def get_context_data(self, *, object_list=None, **kwargs):
	# 	context = super().get_context_data(**kwargs)
	# 	c_def = self.get_user_context(title="Регистрация")
	# 	return dict(list(context.items()) + list(c_def.items()))


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