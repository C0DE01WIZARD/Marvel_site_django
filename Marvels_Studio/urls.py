from django.urls import path
from .import views

urlpatterns = [  # список url
	path('', views.MoviesView.as_view()),
	path('movies/', views.Movies)

]