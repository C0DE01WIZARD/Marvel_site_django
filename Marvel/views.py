from django.http import HttpResponse
from http import HTTPStatus
from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404


def hello(request):
	return HttpResponse('<h1>Привет Рушан наш новый сайт создан</h1>')


def error(request):
	return render(request, 'movies/404.html')


def page_not_found_view(request, exception): # exception - для обработки исключений
	return render(request, 'movies/404.html', status=404)

