from django.contrib.auth import logout, login
from django.contrib.auth.views import LoginView
from django.http import HttpResponse
from django.urls import reverse_lazy
from rest_framework.response import Response
from .views import *
from django.views.generic.base import View
from django.views.generic import ListView, DetailView, TemplateView, CreateView
from django.views.generic.detail import DataMixin
from rest_framework.views import APIView
from django.core.paginator import Paginator
from django.shortcuts import render, redirect, get_object_or_404

from .forms import * # импорт формы из forms.py
from .models import *

# повторить материал https://www.youtube.com/watch?v=u37FXeVQIpU&list=PLA0M1Bcd0w8xO_39zZll2u1lz_Q-Mwn1F&index=13


def add(request): # форма добавления фильмов, не работает 11.09.2022
	if request.method == 'POST':
		form = FormAdd(request.POST)
		if form.is_valid():
		# print(form.cleaned_data, 'Данные переданы через POST запрос!!!')
			try:
				Movie.objects.create(**form.cleaned_data)
				return redirect('home')
			except:
				form.add_error(None, 'Ошибка добавления поста')
	else:
		form = FormAdd()
	return render(request, 'movies/+.html', {'form': form})# 'form' присваем значение переменной form


def Movies(request): # представление страницы фильмы с пагинацией
	contact_list = Movie.objects.all()
	paginator = Paginator(contact_list, 2)
	page_number = request.GET.get('page')
	page_obj = paginator.get_page(page_number)
	return render(request, 'movies/movies.html', {'page_obj': page_obj})


class Series(ListView):
	model = Series
	template_name = "movies/series.html"
	context_object_name = "movie"


# def show_movie(request, post_id): # представление показание фильмов
# 	movie_show = get_object_or_404(Movie, pk=post_id) # будем брать запись из модели Movie
# 	# pk-первичный ключ соответствует идентификатору
# 	context = {
# 		'movie': movie_show, # ссылка на объект Movie
# 		'title': movie_show.title,
# 		'cat_selected': movie_show.cat_id, # номер
# 	}
# 	return render(request, 'movie/show_movie.html', context=context)


class About(ListView):
	model = Movie
	template_name = "movies/about.html"
	context_object_name = "movie"


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


class Register(DataMixin, CreateView): # унаследуем от стандартного класса createview
	form_class = RegisterForm # стандартная форма для регистрации пользователей
	template_name = "movies/reg.html" # ссылка на шаблон
	success_url = reverse_lazy('auth') # перенаправление при успешной авторизации на страницу 'auth.html'


	def form_valid(self, form): # метод вызывается при успешной ПРОВЕРКИ ФОРМЫ регисстрации
		user = form.save() # сохраняем пользователя в БД
		login(self.request, user) # ВЫЗЫВАЕМ ФУНКЦИЮ ДЛЯ АВТООИЗАЦИИ ПОЛЬЗОВАТЕЛЯ
		return redirect('about')


class Auth(DataMixin, LoginView): # LoginView - вся логика авторизации
	form_class = LoginUserForm
	template_name = "movies/auth.html"

	def get_success_url(self): # функция вызывается если пользователь верно вел пароль
		return reverse_lazy('about') # функция перенаправит на главную страницу


def logout_user(request): # функция выхода из системы
	logout(request)
	return redirect('auth')




class AboutFeedView(TemplateView):
	template_name = "movies/feedback.html"


class AboutDateView(TemplateView):
	template_name = "movies/date.html"


class AboutListView(TemplateView):
	template_name = "movies/list.html"


class News(TemplateView):
	template_name = "movies/news.html"