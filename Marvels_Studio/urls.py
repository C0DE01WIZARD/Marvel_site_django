from django.urls import path
from .import views

urlpatterns = [  # список url
	path('', views.MoviesView.as_view()), #пустая так как главная страница
	path('movies/', views.Movies),
	path('<int:pk>/', views.MovieDetailViews.as_view()), # принимаем pk как число int
	path('home/', views.Home.as_view(), name="Home"),
	path('index/', views.Index.as_view())
]