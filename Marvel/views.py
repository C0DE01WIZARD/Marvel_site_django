from django.http import HttpResponse


def hello(request):
	return HttpResponse('<h1>Привет Рушан наш новый сайт создан</h1>')
