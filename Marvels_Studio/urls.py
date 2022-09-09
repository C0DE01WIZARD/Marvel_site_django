from django.urls import path
from . import views

from Marvels_Studio.views import *

urlpatterns = [  # список url
	path('', views.News.as_view()),  # пустая так как главная страница
# принимаем pk как число int и передаём аргумент как pk
	path('search/', views.Search.as_view(), name='search'),
	path('about/', views.About.as_view(), name='about'),
	path('auth/', views.Auth.as_view(), name='auth'),
	#path('movie/<int:movieid>/', Movies, name='movies'),
	path('movie/', views.Movies.as_view(), name='movies'),
	path('about_us/', views.AboutUsView.as_view(), name="about_us"),
	path('reg/', AboutRegView.as_view(template_name="movies/reg.html")),
	path('feed/', AboutFeedView.as_view(template_name="movies/feedback.html")),
	path('date/', AboutDateView.as_view(template_name="movies/date.html")),
	path('pagi/', AboutPagiView.as_view(template_name="movies/pagi.html")),
	path('list/', AboutListView.as_view(template_name="movies/list.html")),
	path('news/', News.as_view(template_name='movies/news.html')),
	path('add/', views.add, name='add')

]



