from django.contrib.auth import logout, login
from django.contrib.auth.views import LoginView
from django.forms import model_to_dict
from django.http import HttpResponse
from django.urls import reverse_lazy
from rest_framework import generics
from rest_framework.response import Response

from .serializers import MovieSerializer
from .views import *
from django.views.generic.base import View
from django.views.generic import ListView, DetailView, TemplateView, CreateView, FormView
from django.views.generic.detail import DataMixin
from rest_framework.views import APIView
from rest_framework import generics
from django.core.paginator import Paginator
from django.shortcuts import render, redirect, get_object_or_404

from .forms import *  # импорт формы из forms.py
from .models import *
from django.http import HttpResponse
from django.db.models import Q


class SearchResult(ListView):
	model = Movie
	template_name = 'movies/searchresult.html'

	def get_queryset(self):
		query = self.request.GET.get('q')
		object_list = Movie.objects.filter(
			Q(title=query)
		)
		return object_list

class Trailer(ListView):
	model = Movie
	template_name = "movies/trailer.html"

class Pay(View):
	def get(self, request):
		return render(request, "movies/pay.html")

class MovieDet(View):
	def get(self, request, slug):
		detail = Movie.objects.get(url=slug)  # get - метод который принимает один объект
		return render(request, 'movies/detail.html', {'movie': detail})


class SeriesDet(View):
	def get(self, request, slug):
		series = Series.objects.get(url=slug)  # get - метод который принимает один объект
		return render(request, 'movies/seriesdetail.html', {'series': series})


class ActorsDet(View):
	def get(self, request, slug):
		detail1 = Actor.objects.get(url=slug)  # get - метод который принимает один объект
		return render(request, 'movies/actorsdetail.html', {'actors': detail1})


def Actors(request):
	actor = Actor.objects.all()
	return render(request, 'movies/actors.html', {'actors': actor, 'title': 'Актеры'})


def Message(request):
	return render(request, 'movies/message_post.html')


def add(request):  # форма добавления фильмов
	if request.method == 'POST':
		form = FormAdd(request.POST)
		if form.is_valid():
			# print(form.cleaned_data, 'Данные переданы через POST запрос!!!')
			try:
				form.save()
				return redirect('about')
			except:
				form.add_error(None, 'Ошибка добавления поста')
	else:
		form = FormAdd()
	return render(request, 'movies/+.html', {'form': form})  # 'form' присваем значение переменной form


def FeedAdd(request):  # форма добавления обратной связи
	if request.method == 'POST':
		form = FeedBack(request.POST)
		if form.is_valid():
			# print(form.cleaned_data, 'Данные переданы через POST запрос!!!')
			try:
				form.save()
				return redirect('about')
			except:
				form.add_error(None, 'Ошибка добавления обратной связи')
	else:
		form = FeedBack()
	return render(request, 'movies/feedback.html', {'form': form})  # 'form' присваем значение переменной form


def Movies(request):  # представление страницы фильмы с пагинацией
	contact_list = Movie.objects.all()
	paginator = Paginator(contact_list, 3)
	page_number = request.GET.get('page')
	page_obj = paginator.get_page(page_number)
	return render(request, 'movies/movies.html', {'page_obj': page_obj})


class SeriesD(ListView):
	model = Series
	template_name = "movies/series.html"
	context_object_name = "movie"


def About(request):  # представление страницы фильмы с пагинацией
	contact_list = Feed.objects.all()
	paginator1 = Paginator(contact_list, 4)

	contact_list = News.objects.all()
	paginator2 = Paginator(contact_list, 1)

	page_number = request.GET.get('page')
	page_obj1 = paginator1.get_page(page_number)

	page_number = request.GET.get('page')
	page_obj2 = paginator2.get_page(page_number)

	return render(request, 'movies/about.html', {'page_obj1': page_obj1, 'page_obj2': page_obj2})


class MovieAPI(APIView):  # API ЗАПРОСЫ
	def get(self, request):  # запрос GET, метод за обработку get запросов, без серилиазатора
		lst = Feed.objects.all().values() # values - набор значений для перед, список из БД
		return Response({'post': list(lst)})  # передача данных в GET запрос для вывоода, возвращение JSON СТРОКИ



	def post(self, request):  # ЗАПРОС POST добавление данных в БД
		post_new = Feed.objects.create(
			name=request.data['name', False],
			email=request.data['email', False],
			text=request.data['text', False],
			time_create=request.data['create', False]
		)
		return Response({'post': model_to_dict(post_new)})


class MovieAPI2(generics.ListAPIView):
	queryset = Movie.objects.all()
	serializer_class = MovieSerializer

class AboutUsView(View):
	def get(self, request):
		info = Info.objects.all()
		famous1 = Famous_actors.objects.all()
		return render(request, "movies/about us.html", {'infos': info, 'famous': famous1})


class Register(DataMixin, CreateView):  # унаследуем от стандартного класса createview
	form_class = RegisterForm  # стандартная форма для регистрации пользователей
	template_name = "movies/reg.html"  # ссылка на шаблон
	success_url = reverse_lazy('auth')  # перенаправление при успешной авторизации на страницу 'auth.html'

	def form_valid(self, form):  # метод вызывается при успешной ПРОВЕРКИ ФОРМЫ регисстрации
		user = form.save()  # сохраняем пользователя в БД
		login(self.request, user)  # ВЫЗЫВАЕМ ФУНКЦИЮ ДЛЯ АВТООИЗАЦИИ ПОЛЬЗОВАТЕЛЯ
		return redirect('about')


class Auth(DataMixin, LoginView):  # LoginView - вся логика авторизации
	form_class =  LoginUserForm
	template_name = "movies/auth.html"

	def get_success_url(self):  # функция вызывается если пользователь верно вел пароль
		return reverse_lazy('about')  # функция перенаправит на главную страницу


def logout_user(request):  # функция выхода из системы
	logout(request)
	return redirect('auth')


def Sales(request):  # представление страницы  с пагинацией
	contact_list = SalesM.objects.all()
	paginator = Paginator(contact_list, 4)
	page_number = request.GET.get('page')
	page_obj = paginator.get_page(page_number)
	return render(request, 'movies/sales.html', {'page_obj': page_obj})


def Newss(request):
	news = News.objects.all()
	famous_actors = Actor.objects.all()
	return render(request, 'movies/news.html', {'newss': news, 'famous': famous_actors})
