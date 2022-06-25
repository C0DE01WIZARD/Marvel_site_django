from django.http import HttpResponse
from http import HTTPStatus
from django.shortcuts import render


def hello(request):
	return HttpResponse('<h1>Привет Рушан наш новый сайт создан</h1>')


def error(request):
	return render(request, 'movies/your-template.html')
	# your custom status in this case 204


def index(request):
	return render(request, 'movies/Index.html')

