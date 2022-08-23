from django.urls import path
from . import views
from Marvels_Studio.views import AboutView
from Marvels_Studio.views import AboutUsView
from Marvels_Studio.views import AboutRegView
from Marvels_Studio.views import AboutFeedView
from Marvels_Studio.views import AboutDateView
from Marvels_Studio.views import AboutPagiView
from Marvels_Studio.views import AboutMoviesView
from Marvels_Studio.views import AboutListView
urlpatterns = [  # список url
	path('', views.MoviesView.as_view()),  # пустая так как главная страница
	#path('<slug:slug>/', views.Detail.as_view()),  # принимаем pk как число int
	path('<int:pk>/', views.Detail.as_view()),  # принимаем pk как число int и передаём аргумент как pk
	path('search/', views.Search.as_view(), name='search'),
	path('base/', views.base.as_view(), name='base'),
	path('reg/', views.reg, name='reg'),
	path('about/', AboutView.as_view(template_name="movies/about.html")),
	path('about_us/', AboutUsView.as_view(template_name="movies/about us.html")),
	path('reg1/', AboutRegView.as_view(template_name="movies/reg.html")),
	path('feed/', AboutFeedView.as_view(template_name="movies/feedback.html")),
	path('date/', AboutDateView.as_view(template_name="movies/date.html")),
	path('pagi/', AboutPagiView.as_view(template_name="movies/pagination.html")),
	path('movie/', AboutMoviesView.as_view(template_name="movies/movieS.html")),
	path('list/', AboutListView.as_view(template_name="movies/list.html"))

]


