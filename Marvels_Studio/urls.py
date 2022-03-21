from django.urls import path
from .import views

urlpatterns = [  # список url
	path('', views.MoviesView.as_view()),
	path('movies/', views.Movies),
	path('<int:pk>/', views.MovieDetailViews.as_view()) # принимаем pk как число

]