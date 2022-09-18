from django.urls import path, re_path
from . import views

from Marvels_Studio.views import *

urlpatterns = [  # список url
	path('news/', views.News.as_view()),  # пустая так как главная страница
	path('', About.as_view(), name='about'),
	path('auth/', Auth.as_view(), name='auth'),
	path('logout/', logout_user, name='logout'),
	path('movie/', Movies, name='movies'),
	path('series/', Series.as_view(), name='series'),
	path('about_us/', views.AboutUsView.as_view(), name="about_us"),
	path('reg/', Register.as_view(template_name="movies/reg.html"), name='reg'),
	path('feed/', AboutFeedView.as_view(template_name="movies/feedback.html")),
	path('date/', AboutDateView.as_view(template_name="movies/date.html")),
	path('list/', AboutListView.as_view(template_name="movies/list.html")),
	path('news/', News.as_view(template_name='movies/news.html')),
	path('add/', views.add, name='add')

]
